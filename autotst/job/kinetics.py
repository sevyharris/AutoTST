from autotst.calculator.gaussian import Gaussian
from autotst.calculator.vibrational_analysis import VibrationalAnalysis, percent_change
from autotst.calculator.statmech import StatMech
from autotst.reaction import Reaction, TS
from autotst.species import Species, Conformer
from autotst.geometry import Bond, Angle, Torsion, CisTrans, ChiralCenter
from cclib.io import ccread
import cclib
from rmgpy.molecule import Molecule as RMGMolecule
from rmgpy.species import Species as RMGSpecies
from rmgpy.reaction import Reaction as RMGReaction, ReactionError
from rmgpy.kinetics import PDepArrhenius, PDepKineticsModel
from rmgpy.data.rmg import RMGDatabase
import rmgpy
from ase.calculators.gaussian import Gaussian as ASEGaussian
from ase.atoms import Atom, Atoms
import ase
import rdkit.Chem.rdDistGeom
import rdkit.DistanceGeometry
from rdkit.Chem.Pharm3D import EmbedLib
from rdkit.Chem import AllChem
from rdkit import Chem
import rdkit
import os
import time
import yaml
from shutil import move, copyfile
import numpy as np
import pandas as pd
import subprocess
import multiprocessing
from multiprocessing import Process, Manager
import logging
FORMAT = "%(filename)s:%(lineno)d %(funcName)s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


class KineticsJob(Job):
    """
    
    """

    def __init__():
        """
        """

        
    def submit_transitionstate(self, transitionstate, opt_type, restart=False):
        """
        A methods to submit a job for a TS object based on a single calculator
        """
        assert transitionstate, "Please provide a transitionstate to submit a job"
        self.qm_calculator.conformer = transitionstate
        if opt_type.lower() == "shell":
            ase_calculator = self.qm_calculator.get_shell_calc()
            time = "24:00:00"
        elif opt_type.lower() == "center":
            ase_calculator = self.qm_calculator.get_center_calc()
            time = "24:00:00"
        elif opt_type.lower() == "overall":
            ase_calculator = self.qm_calculator.get_overall_calc()
            time = "24:00:00"
        elif opt_type.lower() == "irc":
            ase_calculator = self.qm_calculator.get_irc_calc()
            time = "24:00:00"
            nproc = "14"

        if opt_type.lower() != "irc":
            copy_molecule = transitionstate.rmg_molecule.copy()
            copy_molecule.deleteHydrogens()
            number_of_atoms = len(copy_molecule.atoms)
            if number_of_atoms >= 4:
                nproc = 2
            elif number_of_atoms >= 7:
                nproc = 4
            elif number_of_atoms >= 9:
                nproc = 6
            else:
                nproc = 8

        self.write(transitionstate, ase_calculator)

        label = ase_calculator.label
        scratch = ase_calculator.scratch
        file_path = os.path.join(scratch, label)

        os.environ["COMMAND"] = "g16"  # only using gaussian for now
        os.environ["FILE_PATH"] = file_path

        attempted = False
        if os.path.exists(file_path + ".log"):
            attempted = True
            logging.info("It appears that {} has already been attempted...".format(label))

        if (not attempted) or restart:
            if self.exclude:
                if isinstance(self.exclude, str):
                    command = """sbatch --exclude={2} --job-name="{0}" --output="{0}.slurm.log" --error="{0}.slurm.log" -p {1} -N 1 -n {4} -t {3} --mem=15GB $AUTOTST/autotst/job/submit.sh""".format(
                        label, self.partition, self.exclude, time, nproc)
                elif isinstance(self.exclude, list):
                    exc = ""
                    for e in self.exclude:
                        exc += e
                        exc += ","
                    exc = exc[:-1]
                    command = """sbatch --exclude={2} --job-name="{0}" --output="{0}.slurm.log" --error="{0}.slurm.log" -p {1} -N 1 -n {4} -t {3} --mem=15GB $AUTOTST/autotst/job/submit.sh""".format(
                        label, self.partition, exc, time, nproc)
            else:
                command = """sbatch --job-name="{0}" --output="{0}.slurm.log" --error="{0}.slurm.log" -p {1} -N 1 -n {3} -t {2} --mem=15GB $AUTOTST/autotst/job/submit.sh""".format(
                    label, self.partition, time, nproc)
            subprocess.call(command, shell=True)

        return label

    def calculate_transitionstate(self, transitionstate, vibrational_analysis=True):
        """
        A method to perform the partial optimizations for a transitionstate and arrive
        at a final geometry. Returns True if we arrived at a final geometry, returns false
        if there is an error along the way.
        """

        ts_identifier = "{}_{}_{}".format(
            transitionstate.reaction_label, transitionstate.direction, transitionstate.index)

        for opt_type in ["shell", "overall"]:
            self.qm_calculator.conformer = transitionstate

            if opt_type == "overall":
                 file_path = "{}_{}_{}.log".format(transitionstate.reaction_label, transitionstate.direction, transitionstate.index)
            else:
                 file_path = "{}_{}_{}_{}.log".format(transitionstate.reaction_label, transitionstate.direction, opt_type, transitionstate.index)

            file_path = os.path.join(
                self.directory, 
                "ts", 
                transitionstate.reaction_label, 
                "conformers", 
                file_path
            )


            if not os.path.exists(file_path):
                logging.info(
                    "Submitting {} calculations for {}".format(opt_type.upper(),ts_identifier))
                label = self.submit_transitionstate(
                    transitionstate, opt_type=opt_type.lower())
                while not self.check_complete(label):
                    time.sleep(15)

            else:
                logging.info(
                    "It appears that we already have a complete {} log file for {}".format(opt_type.upper(), ts_identifier))

                complete, converged = self.qm_calculator.verify_output_file(file_path)
                
                if not complete:
                    logging.info(
                        "It seems that the {} file never completed for {} never completed, running it again".format(opt_type.upper(), ts_identifier))
                    label = self.submit_transitionstate(
                        transitionstate, opt_type=opt_type.lower(), restart=True)
                    while not self.check_complete(label):
                        time.sleep(15)

            complete, converged = self.qm_calculator.verify_output_file(file_path)

            if not (complete and converged):
                logging.info(
                    "{} failed the {} optimization".format(ts_identifier, opt_type.upper()))
                global_results[ts_identifier] = False
                return False
            logging.info(
                "{} successfully completed the {} optimization!".format(ts_identifier, opt_type.upper()))
            transitionstate.ase_molecule = self.read(file_path)
            transitionstate.update_coords_from("ase")

        logging.info(
            "Calculations for {} are complete and resulted in a normal termination!".format(ts_identifier))

        got_one = self.validate_transitionstate(
                transitionstate=transitionstate, vibrational_analysis=vibrational_analysis)
        if got_one:
            global_results[ts_identifier] = True
            return True
        else:
            global_results[ts_identifier] = False
            return False

    def calculate_reaction(self, vibrational_analysis=True, restart=False):
        """
        A method to run calculations for all tranitionstates for a reaction
        """

        logging.info("Calculating geometries for {}".format(self.reaction))
        if not restart: 
            if os.path.exists(
                os.path.join(self.directory, "ts", self.reaction.label, self.reaction.label + ".log")):
                logging.info("This reaction has already been run and has a successful validated transition state! :)")
                return True



        if self.conformer_calculator:
            self.reaction.generate_conformers(ase_calculator=self.conformer_calculator)

        currently_running = []
        processes = {}

        for direction, transitionstates in list(self.reaction.ts.items()):

            for transitionstate in transitionstates:

                process = Process(target=self.calculate_transitionstate, args=(
                    transitionstate,))
                processes[process.name] = process

        for name, process in list(processes.items()):
            while len(currently_running) >= 50:
                for running in currently_running:
                    if not running.is_alive():
                        currently_running.remove(name)
            process.start()
            currently_running.append(name)

        while len(currently_running) > 0:
            for name, process in list(processes.items()):
                if not (name in currently_running):
                    continue
                if not process.is_alive():
                    currently_running.remove(name)

        energies = []
        for label, result in global_results.items():
            if not result:
                logging.info("Calculations for {} FAILED".format(label))
            f = "{}.log".format(label)
            path = os.path.join(self.qm_calculator.directory, "ts",
                    self.reaction.label, "conformers", f)
            if not os.path.exists(path):
                logging.info("It appears that {} failed...".format(f))
                continue
            try:
                parser = ccread(path, loglevel=logging.ERROR)
                if parser is None:
                    logging.info(
                        "Something went wrong when reading in results for {}...".format(f))
                    continue
                energy = parser.scfenergies[-1]
            except:
                logging.info(
                    "The parser does not have an scf energies attribute, we are not considering {}".format(f))
                energy = 1e5

            energies.append([energy, transitionstate, f])

        energies = pd.DataFrame(
            energies, columns=["energy", "transitionstate", "file"]).sort_values("energy").reset_index()

        if energies.shape[0] == 0:
            logging.info(
                "No transition state for {} was successfully calculated... :(".format(self.reaction))
            return False

        energies.reset_index(inplace=True)
        lowest_energy_label = energies.iloc[0].file
        logging.info("The lowest energy transition state is {}".format(lowest_energy_label))

        copyfile(
            os.path.join(self.qm_calculator.directory, "ts", self.reaction.label,
                         "conformers", lowest_energy_label),
            os.path.join(self.qm_calculator.directory, "ts",
                         self.reaction.label, self.reaction.label + ".log")
        )
        logging.info("The lowest energy file is {}! :)".format(
            lowest_energy_label + ".log"))
        return True

    def validate_transitionstate(self, transitionstate, vibrational_analysis=True):

        validated = False
        if vibrational_analysis:
            vib = VibrationalAnalysis(
                transitionstate=transitionstate, directory=self.directory)
            validated = vib.validate_ts()
        if not validated:
            logging.info("Could not validate with Vibrational Analysis... Running an IRC to validate instead...")
            label = self.submit_transitionstate(
                transitionstate, opt_type="irc")
            while not self.check_complete(label):
                time.sleep(15)
            result = self.qm_calculator.validate_irc()
            if result:
                logging.info("Validated via IRC")
                return True
            else:
                logging.info(
                    "Could not validate this conformer... trying the next lowest energy conformer")
                return False
        else:
            logging.info("Validated via Vibrational Analysis")
            return True
