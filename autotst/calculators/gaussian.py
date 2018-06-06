#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
#
#   AutoTST - Automated Transition State Theory
#
#   Copyright (c) 2015-2018 Prof. Richard H. West (r.west@northeastern.edu)
#
#   Permission is hereby granted, free of charge, to any person obtaining a
#   copy of this software and associated documentation files (the 'Software'),
#   to deal in the Software without restriction, including without limitation
#   the rights to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell copies of the Software, and to permit persons to whom the
#   Software is furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#
################################################################################

import os
import itertools
import logging
import numpy as np

from autotst.reaction import AutoTST_Reaction, AutoTST_TS
from autotst.molecule import AutoTST_Molecule
from autotst.calculators.vibrational_analysis import Vibrational_Analysis
from autotst.calculators.calculator import AutoTST_Calculator

from ase.io.gaussian import read_gaussian, read_gaussian_out
from ase.calculators.gaussian import Gaussian


class AutoTST_Gaussian(AutoTST_Calculator):

    def __init__(self,
                 autotst_reaction,
                 mem="5GB",
                 nprocshared=20,
                 scratch=".",
                 method="m062x",
                 basis="6-311+g(2df,2p)",
                 store_directory="."):
        """
        A method to create all of the calculators needed for AutoTST

        :params:
        autotst_reaction: (AutoTST_Reaction) The reaction of interest
        scratch: (str) The directory that you would like to use for calculations
        """

        self.reaction = autotst_reaction
        self.mem = mem
        self.nprocshared = nprocshared
        self.scratch = scratch
        self.method = method
        self.basis = basis
        self.store_directory = store_directory

        self.get_reactant_and_product_calcs(self.mem, self.nprocshared, self.scratch, self.method, self.basis)

        self.shell_calc = self.get_shell_calc(self.mem, self.nprocshared, self.scratch, self.method, self.basis)
        self.center_calc = self.get_center_calc(self.mem, self.nprocshared, self.scratch, self.method, self.basis)
        self.overall_calc = self.get_overall_calc(self.mem, self.nprocshared, self.scratch, self.method, self.basis)
        self.irc_calc = self.get_irc_calc(self.mem, self.nprocshared, self.scratch, self.method, self.basis)

        self.completed_irc = False

    def __repr__(self):
        return '<AutoTST Gaussian Calculators "{0}">'.format(self.reaction.label)

    def reactants_or_products_calc(self, autotst_mol, mem="5GB", nprocshared=20, scratch=".", method="m062x", basis="6-311+g(2df,2p)"):
        "A method that creates a calculator for a reactant or product"

        autotst_mol.rmg_molecule.updateMultiplicity()

        label = autotst_mol.rmg_molecule.toSMILES().replace("(", "left").replace(")", "right")

        calc = Gaussian(mem=mem,
                        nprocshared=nprocshared,
                        label=label,
                        scratch=scratch,
                        method=method,
                        basis=basis,
                        extra="opt=(verytight,gdiis) freq IOP(2/16=3)",
                        multiplicity = autotst_mol.rmg_molecule.multiplicity
                        )
        del calc.parameters['force']

        return calc

    def get_reactant_and_product_calcs(self, mem="5GB", nprocshared=20, scratch=".", method="m062x", basis="6-311+g(2df,2p)"):
        "A method that collects all of the calculators for reactants and prods"

        self.reactant_calcs = {}
        self.product_calcs = {}

        for reactant in self.reaction.reactant_mols:
            calc = self.reactants_or_products_calc(reactant, mem, nprocshared, scratch, method, basis)
            self.reactant_calcs[reactant] = calc

        for product in self.reaction.product_mols:
            calc = self.reactants_or_products_calc(product, mem, nprocshared, scratch, method, basis)
            self.product_calcs[product] = calc


    def get_shell_calc(self, mem="5GB", nprocshared=20, scratch=".", method="m062x", basis="6-311+g(2df,2p)"):
        "A method to create a calculator that optimizes the reaction shell"

        indicies = []
        for i, atom in enumerate(self.reaction.ts.rmg_ts.atoms):
            if not (atom.label == ""):
                indicies.append(i)

        combos = ""
        for combo in list(itertools.combinations(indicies, 2)):
            a,b = combo
            combos += "{0} {1} F\n".format(a+1,b+1)

        self.reaction.ts.rmg_ts.updateMultiplicity()

        label = self.reaction.label.replace("(", "left").replace(")", "right") + "_shell"

        calc = Gaussian(mem=mem,
                        nprocshared=nprocshared,
                        label=label,
                        scratch=scratch,
                        method=method,
                        basis=basis,
                        extra="Opt=(ModRedun,Loose) Int(Grid=SG1)",
                        multiplicity = self.reaction.ts.rmg_ts.multiplicity,
                        addsec = [combos[:-1]])

        del calc.parameters['force']
        return calc

    def get_center_calc(self, mem="5GB", nprocshared=20, scratch=".", method="m062x", basis="6-311+g(2df,2p)"):
        "A method to create the calculator to perform the reaction center opt"

        indicies = []
        for i, atom in enumerate(self.reaction.ts.rmg_ts.atoms):
            if (atom.label == ""):
                indicies.append(i)

        combos = ""
        for combo in list(itertools.combinations(indicies, 2)):
            a,b = combo
            combos += "{0} {1} F\n".format(a+1,b+1)

        self.reaction.ts.rmg_ts.updateMultiplicity()

        label = self.reaction.label.replace("(", "left").replace(")", "right") + "_center"

        calc = Gaussian(mem=mem,
                        nprocshared=nprocshared,
                        label=label,
                        scratch=scratch,
                        method=method,
                        basis=basis,
                        extra="opt=(ts,calcfc,noeigentest,ModRedun)",
                        multiplicity = self.reaction.ts.rmg_ts.multiplicity,
                        addsec = [combos[:-1]])

        del calc.parameters['force']
        return calc

    def get_overall_calc(self, mem="5GB", nprocshared=20, scratch=".", method="m062x", basis="6-311+g(2df,2p)"):
        "A method to create the calculator to perform the full TS optimization"

        self.reaction.ts.rmg_ts.updateMultiplicity()

        label = self.reaction.label.replace("(", "left").replace(")", "right") + "_overall"

        calc = Gaussian(mem=mem,
                        nprocshared=nprocshared,
                        label=label,
                        scratch=scratch,
                        method=method,
                        basis=basis,
                        extra="opt=(ts,calcfc,noeigentest) freq",
                        multiplicity = self.reaction.ts.rmg_ts.multiplicity)

        del calc.parameters['force']
        return calc

    def get_irc_calc(self, mem="5GB", nprocshared=20, scratch=".", method="m062x", basis="6-311+g(2df,2p)"):
        "A method to create the IRC calculator object"

        self.reaction.ts.rmg_ts.updateMultiplicity()
        label = self.reaction.label.replace("(", "left").replace(")", "right") + "_irc"

        calc = Gaussian(mem=mem,
                        nprocshared=nprocshared,
                        label=label,
                        scratch=scratch,
                        method=method,
                        basis=basis,
                        extra="irc=(calcall)",
                        multiplicity = self.reaction.ts.rmg_ts.multiplicity)

        del calc.parameters['force']
        return calc


    def calculate(self, autotst_object, calc):

        """
        A method to perform a calculation given a calculator and an AutoTST
        object. If the corresponding log file already exists, we will skip it

        :params:
        autotst_object: (AutoTST_Molecule, AutoTST_TS, AutoTST_Reaction) an
        AutoTST object that you want to run calculations on
        calc: (ase.calculators.calculator) the calculator that you want to run
        """

        short_file_name = calc.label.replace("left", "(").replace("right", ")") + ".log"
        old_long_file_name = os.path.join(calc.scratch, calc.label + ".log")
        new_long_file_name = os.path.join(calc.scratch, calc.label.replace("left", "(").replace("right", ")") + ".log")

        if isinstance(autotst_object, AutoTST_Molecule):

            # Seeing if the file exists
            if not os.path.exists(new_long_file_name):
                # File doesn't exist, running calculations
                logging.info("Starting calculation for {}...".format(short_file_name))
                try:
                    calc.calculate(autotst_object.ase_molecule)
                    # reading in results
                    autotst_object.ase_molecule = read_gaussian_out(old_long_file_name)
                    autotst_object.update_from_ase_mol()
                    return autotst_object, True
                except: #TODO: add error for seg fault
                    # first calc failed, trying it once more
                    logging.info("Failed first attempt for {}. Trying it once more...".format(short_file_name))
                    try:
                        calc.calculate(autotst_object.ase_molecule)
                        autotst_object.ase_molecule = read_gaussian_out(old_long_file_name)
                        autotst_object.update_from_ase_mol()
                        return autotst_object, True
                    except: #TODO: add error for seg fault
                        logging.info("{} failed first and second attempt...".format(short_file_name))
                        return autotst_object, False

            else:
                # We found an old file... it should be fixed
                logging.info("Found previous file for {}, verifying it...".format(new_long_file_name))
                if self.verify_output_file(new_long_file_name):
                    logging.info("Old output file verified, reading it in...")
                    autotst_object.ase_molecule = read_gaussian_out(new_long_file_name)
                    autotst_object.update_from_ase_mol()
                    return autotst_object, True

                else:
                    logging.info("Could not verify output file, attempting to run one last time...")
                    try:
                        calc.calculate(autotst_object.ase_molecule)
                        autotst_object.ase_molecule = read_gaussian_out(old_long_file_name)
                        autotst_object.update_from_ase_mol()
                        return autotst_object, True

                    except: #TODO: add error for seg fault
                        logging.info("{} failed... again...".format(short_file_name))
                        return autotst_object, False

        elif isinstance(autotst_object, AutoTST_Reaction):

            # Seeing if the file exists
            if not os.path.exists(new_long_file_name):
                # File doesn't exist, running calculations
                logging.info("Starting calculation for {}...".format(short_file_name))
                try:
                    calc.calculate(autotst_object.ts.ase_ts)
                    # reading in results
                    autotst_object.ts.ase_ts = read_gaussian_out(old_long_file_name)
                    autotst_object.ts.update_from_ase_ts()
                    return autotst_object, True
                except: #TODO: add error for seg fault
                    # first calc failed, trying it once more
                    logging.info("Failed first attempt for {}. Trying it once more...".format(short_file_name))
                    try:
                        calc.calculate(autotst_object.ts.ase_ts)
                        autotst_object.ts.ase_ts = read_gaussian_out(old_long_file_name)
                        autotst_object.ts.update_from_ase_ts()
                        return autotst_object, True
                    except: #TODO: add error for seg fault
                        logging.info("{} failed first and second attempt...".format(short_file_name))
                        return autotst_object, False

            else:
                # We found an old file... it should be fixed
                logging.info("Found previous file for {}, verifying it...".format(new_long_file_name))
                if self.verify_output_file(new_long_file_name):
                    logging.info("Old output file verified, reading it in...")
                    autotst_object.ts.ase_ts = read_gaussian_out(new_long_file_name)
                    autotst_object.ts.update_from_ase_ts()
                    return autotst_object, True

                else:
                    logging.info("Could not verify output file, attempting to run one last time...")
                    try:
                        calc.calculate(autotst_object.ts.ase_ts)
                        autotst_object.ts.ase_ts = read_gaussian_out(old_long_file_name)
                        autotst_object.ts.update_from_ase_ts()
                        return autotst_object, True

                    except: #TODO: add error for seg fault
                        logging.info("{} failed... again...".format(short_file_name))
                        return autotst_object, False

        elif isinstance(autotst_object, AutoTST_TS):

            # Seeing if the file exists
            if not os.path.exists(new_long_file_name):
                # File doesn't exist, running calculations
                logging.info("Starting calculation for {}...".format(short_file_name))
                try:
                    calc.calculate(autotst_object.ase_ts)
                    # reading in results
                    autotst_object.ase_ts = read_gaussian_out(old_long_file_name)
                    autotst_object.update_from_ase_ts()
                    return autotst_object, True
                except: #TODO: add error for seg fault
                    # first calc failed, trying it once more
                    logging.info("Failed first attempt for {}. Trying it once more...".format(short_file_name))
                    try:
                        calc.calculate(autotst_object.ase_ts)
                        autotst_object.ase_ts = read_gaussian_out(old_long_file_name)
                        autotst_object.update_from_ase_ts()
                        return autotst_object, True
                    except: #TODO: add error for seg fault
                        logging.info("{} failed first and second attempt...".format(short_file_name))
                        return autotst_object, False

            else:
                # We found an old file... it should be fixed
                logging.info("Found previous file for {}, verifying it...".format(new_long_file_name))
                if self.verify_output_file(new_long_file_name):
                    logging.info("Old output file verified, reading it in...")
                    autotst_object.ase_ts = read_gaussian_out(new_long_file_name)
                    autotst_object.update_from_ase_ts()
                    return autotst_object, True

                else:
                    logging.info("Could not verify output file, attempting to run one last time...")
                    try:
                        calc.calculate(autotst_object.ase_ts)
                        autotst_object.ase_ts = read_gaussian_out(old_long_file_name)
                        autotst_object.update_from_ase_ts()
                        return autotst_object, True

                    except: #TODO: add error for seg fault
                        logging.info("{} failed... again...".format(short_file_name))
                        return autotst_object, False


    def verify_output_file(self, path):
        "A method to verify output files and make sure that they successfully converged, if not, re-running them"

        f = open(path, "r")
        file_lines = f.readlines()[-5:]
        verified = False
        for file_line in file_lines:
            if " Normal termination" in file_line:
                verified = True

        return verified

    def run_reactants_and_products(self):
        "A method to run the calculations for all reactants and products"

        bools = []
        for mol, calc in self.reactant_calcs.iteritems():
            mol, bool = self.calculate(mol, calc)
            self.fix_io_file(calc)
            bools.append(bool)

        for mol, calc in self.product_calcs.iteritems():
            mol, bool = self.calculate(mol, calc)
            self.fix_io_file(calc)
            bools.append(bool)

        return np.array(bools).all()

    def run_shell(self):
        "A method to run the shell optimization with the reaction center frozen"
        logging.info("Running shell optimization with center frozen...")
        self.reaction, bool = self.calculate(self.reaction, self.shell_calc)
        logging.info("Shell optimization complete!")
        return bool

    def run_center(self):
        "A method to run the reaction center optimization with the shell frozen"
        logging.info("Running center optimization with shell frozen...")
        self.reaction, bool = self.calculate(self.reaction, self.center_calc)
        logging.info("Center optimization complete!")
        return bool

    def run_overall(self):
        "A method to run the optimization of the entire TS"
        logging.info("Running overall optimization...")
        self.reaction, bool = self.calculate(self.reaction, self.overall_calc)
        logging.info("Overall optimization complete!")
        return bool

    def run_irc(self):
        "A method to run the IRC calculation"
        logging.info("Running IRC calculation")
        try:
            self.irc_calc.calculate(self.reaction.ts.ase_ts)
        except:
            # This normally fails because of an issue with ase's `read_results` method.
            pass
        logging.info("IRC calc complete!")

    def validate_irc(self): #TODO: need to add more verification here
        logging.info("Validating IRC file...")
        irc_path = os.path.join(self.irc_calc.scratch, self.irc_calc.label + ".log")
        if not os.path.exists(irc_path):
            logging.info("It seems that the file was `fixed`, reading in the `fixed` version.")
            irc_path = irc_path.replace("left", "(").replace("right", ")")

            if not os.path.exists(irc_path):
                logging.info("It seems that the IRC claculation has not been run.")
                irc_path = False

        if irc_path:
            f = open(irc_path, "r")
            file_lines = f.readlines()[-5:]

            for file_line in file_lines:
                if " Normal termination" in file_line:
                    logging.info("IRC successfully validated")
                    self.validated_irc = True
                else:
                    logging.info("IRC could not be validated")
                    self.validated_irc = False
        else:
            self.validated_irc = False

        return self.validated_irc


    def run_all(self, vibrational_analysis=True):
        """
        A method that is designed to run all of the automated quantum
        calculations for AutoTST. These can be run independently as well.

        :params:
        vibrational_analysis: (bool) A bool to tell AutoTST if you want to use
        vibrational analysis instead of IRC calcs to speed up calculations

        :returns:
        result: (bool) A bool to tell you if an AutoTST run successfully
        converged on a verified TS.
        """
        result = False
        r_and_p = self.run_reactants_and_products()
        if not r_and_p:
            return result
        shell = self.run_shell()
        self.fix_io_file(self.shell_calc)
        if not shell:
            return result
        center = self.run_center()
        self.fix_io_file(self.center_calc)
        if not center:
            return result
        overall = self.run_overall()
        self.fix_io_file(self.overall_calc)
        if not overall:
            return result

        vib = Vibrational_Analysis(reaction=self.reaction, scratch=self.scratch)
        logging.info("Performing Vibrational Analysis...")
        if vibrational_analysis and vib.validate_ts():
            logging.info("Vibrational analysis successful! Successfully arrived at a TS.")
            result = True
        elif vibrational_analysis and not vib.validate_ts():
            logging.info("Could not validate via vibrational analysis... \nRunning IRC instead...")
            self.run_irc()
            result = self.validate_irc()
        else:
            logging.info("Running without vibrational analysis... \nRunning IRC instead...")
            self.run_irc()
            result = self.validate_irc()

        self.fix_io_file(self.irc_calc)

        if result:
            logging.info("Arrived at a TS!")
            return result

        else:
            logging.info("Could not arrive at a TS!")
            return result

    def fix_io_file(self, calc):
        """
        A method that removes the `left` and `right` text from a log, ase, and
        com files and turns it back into a smiles structure
        """
        old_log_file = calc.label + ".log"
        old_log_path = os.path.join(calc.scratch, old_log_file)
        if os.path.exists(old_log_path):
            new_log_path = old_log_path.replace("left", "(").replace("right", ")")
            os.rename(old_log_path, new_log_path)

        old_ase_file = calc.label + ".ase"
        old_ase_path = os.path.join(calc.scratch, old_ase_file)
        if os.path.exists(old_ase_path):
            new_ase_path = old_ase_path.replace("left", "(").replace("right", ")")
            os.rename(old_ase_path, new_ase_path)

        old_com_file = calc.label + ".com"
        old_com_path = os.path.join(calc.scratch, old_com_file)
        if os.path.exists(old_com_path):
            new_com_path = old_com_path.replace("left", "(").replace("right", ")")
            os.rename(old_com_path, new_com_path)


    def fix_io_files(self):
        """
        A method that removes the `left` and `right` text from a log, ase, and
        com files and turns it back into a smiles structure for ALL files.
        """
        for calc in self.reactant_calcs.values:
            self.fix_io_file(calc)

        for calc in self.product_calcs.values:
            self.fix_io_file(calc)

        self.fix_io_file(self.shell_calc)
        self.fix_io_file(self.center_calc)
        self.fix_io_file(self.overall_calc)
