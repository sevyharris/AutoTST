#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################################################################
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
##########################################################################

import os
import itertools
import logging
import numpy

import autotst
from autotst.reaction import Reaction, TS
from autotst.species import Species, Conformer
from autotst.calculator.vibrational_analysis import VibrationalAnalysis
from autotst.data.base import QMData
import rmgpy
from rmgpy.molecule import Molecule as RMGMolecule
from rmgpy.molecule import Atom, getElement
from rmgpy.species import Species as RMGSpecies, TransitionState
from rmgpy.reaction import Reaction as RMGReaction
from rmgpy.kinetics import Arrhenius, Eckart
from rmgpy.statmech import Conformer as RMGConformer, IdealGasTranslation, NonlinearRotor, HarmonicOscillator, LinearRotor


def get_possible_names(reactants, products):

    joinedReactOrders = ['+'.join(order)
                         for order in itertools.permutations(reactants)]
    joinedProdOrders = ['+'.join(order)
                        for order in itertools.permutations(products)]
    fileNames = [
        '_'.join(
            (rJO, pJO)) for rJO in joinedReactOrders for pJO in joinedProdOrders] + [
        '_'.join(
                (pJO, rJO)) for rJO in joinedReactOrders for pJO in joinedProdOrders]

    return fileNames


class InputOutput():
    """
    A class that allows users to read and write .ts and .kinetics files for validated TSs and Reactions
    """

    def __init__(self, reaction=None, rmg_reaction=None, save_directory="."):
        """
        Variables:
        - reaction (Reaction): the reaction of interest
        - save_directory (str): the directory where you want .ts and .kinetics files saved
        """
        self.reaction = reaction
        if reaction:
            self.label = reaction.label
            self.rmg_reaction = reaction.rmg_reaction
        else:
            self.rmg_reaction = rmg_reaction
            self.label = None
        self.save_directory = save_directory

    def copy(self):
        """
        A method to generate a copy of this object
        """
        from copy import deepcopy
        return deepcopy(self)

    def get_qm_data(self, file_path):
        """
        A method to create a QMData object from a log file at file_path

        Variables:
        - file_path (str): the location of the log file you want in
        """

        return QMData().get_qmdata(file_path=file_path)

    def get_label(self, reaction):
        """
        A method to convert an RMGReaction to a reaction label used for writing files
        """
        if isinstance(reaction, Reaction):
            return reaction.label
        assert isinstance(reaction, RMGReaction), "Must provide either an RMGReaction or Reaction object"
        label = ""
        if reaction is None:
            return None
        for reactant in reaction.reactants:
            if isinstance(reactant, RMGMolecule):
                label += reactant.toSMILES()
            elif isinstance(reactant, RMGSpecies):
                if len(RMGSpecies.molecule) > 1:
                    logging.warning("{} has multiple resonance structures. Selecting the first molecule for creating the file path")
                    label += reactant.molecule[0].toSMILES()
                else:
                    label += reactant.molecule[0].toSMILES()
            else:
                logging.warning("No reactants provided...")
                return label
            label += "+"
        label = label.strip("+")
        label += "_"
        
        for product in reaction.products:
            if isinstance(reactant, RMGMolecule):
                label += product.toSMILES()
            elif isinstance(product, RMGSpecies):
                if len(RMGSpecies.molecule) > 1:
                    logging.warning("{} has multiple resonance structures. Selecting the first molecule for creating the file path")
                    label += product.molecule[0].toSMILES()
                else:
                    label += product.molecule[0].toSMILES()
            else:
                logging.warning("No product provided...")
                return None
        return label
        

    def get_ts_file_path(self, save_directory=".", label=None):
        
        assert label, "Please provide a reaction label for saving information"

        return os.path.join(save_directory, label + ".ts")

    def get_kinetics_file_path(self, save_directory=".", label=None):
        
        assert label, "Please provide a reaction label for saving information"

        return os.path.join(save_directory, label + ".kinetics")

    def save_ts(self, reaction, qmData, method="m062x", save_directory="."):
        """
        A method to save the .ts data to a file

        Variables:
        - reaction (Reaction): the reaction of interest
        - method (str): the computational methods that were used
        - qmData (QMData): the data that you want to save
        """
        file_path = self.get_ts_file_path(reaction)
        if not os.path.exists(save_directory):
            try: 
                os.makedirs(save_directory)
            except: 
                logging.info("Writing save directory")
        logging.info("Saving TS result file {}".format(file_path))
        with open(file_path, 'w') as resultFile:
            resultFile.write('rxnLabel = "{0!s}"\n'.format(reaction.label))
            resultFile.write('method = "{0!s}"\n'.format(method))
            resultFile.write("qmData = {0!r}\n".format(qmData))

    def save_kinetics(self, reaction, method="m062x", save_directory="."):
        """
        A method to save the .kinetics data to a file

        Variables:
        - reaction (Reaction): the reaction of interest. Either an RMGReaction or an AutoTST Reaction.
        - method (str): the computational methods that were used
        """
        if not os.path.exists(save_directory):
            try: 
                os.makedirs(save_directory)
            except: 
                logging.info("Writing save directory")
        label = self.get_label(reaction)
        filePath = self.get_kinetics_file_path(save_directory=save_directory, label=label)
        logging.info("Saving kinetics data file {}".format(filePath))
        with open(filePath, 'w') as resultFile:
            if isinstance(reaction, rmgpy.reaction.Reaction):
                assert reaction.kinetics, "No kinetics calclated for this reaction..."
                resultFile.write('method = "{0!s}"\n'.format(method))
                resultFile.write('reaction = {0!r}\n'.format(reaction))
            elif isinstance(reaction, autotst.reaction.Reaction):
                assert reaction.rmg_reaction.kinetics, "No kinetics calclated for this reaction..."
                resultFile.write('method = "{0!s}"\n'.format(method))
                resultFile.write(
                    'reaction = {0!r}\n'.format(reaction.rmg_reaction))

    def read_ts_file(self, path):
        """
        Load the specified transition state data file and return the dictionary of its contents.

        Variables:
        - path (str): the file that you want to read in. It should end with ".kinetics"

        Returns:
        - local_context (dict): the content of the .ts file. Will return None if there is an error
        """

        try:
            with open(path) as resultFile:
                logging.info('Reading existing ts file {0}'.format(path))
                global_context = {'__builtins__': None}
                local_context = {
                    '__builtins__': None,
                    'True': True,
                    'False': False,
                    'QMData': QMData,
                    'array': numpy.array,
                    'int32': numpy.int32,
                }
                exec resultFile in global_context, local_context
        except IOError as e:
            logging.info("Couldn't read ts file {0}".format(path))
            return None
        except (NameError, TypeError, SyntaxError) as e:
            logging.error('The ts file "{0}" was invalid:'.format(path))
            logging.exception(e)
            return None
        if 'rxnLabel' not in local_context:
            logging.error(
                'The ts file "{0}" did not contain a rxnLabel.'.format(path))
            return None
        if 'method' not in local_context:
            logging.error(
                'The ts file "{0}" did not contain a method.'.format(path))
            return None
        if 'qmData' not in local_context:
            logging.error(
                'The ts file "{0}" did not contain thermoData.'.format(path))
            return None
        return local_context

    def read_kinetics_file(self, path):
        """
        Load the specified kinetic data file and return the dictionary of its contents.

        Variables:
        - path (str): the file that you want to read in. It should end with ".kinetics"

        Returns:
        - local_context (dict): the content of the .kinetics file. Will return None if there is an error
        """

        try:
            with open(path) as resultFile:
                logging.info('Reading existing kinetics file {0}'.format(path))
                global_context = {'__builtins__': None}
                local_context = {
                    '__builtins__': None,
                    'True': True,
                    'False': False,
                    'Reaction': RMGReaction,
                    'Species': RMGSpecies,
                    'TransitionState': TransitionState,
                    'Arrhenius': Arrhenius,
                    'Eckart': Eckart,
                    'Conformer': RMGConformer,
                    'IdealGasTranslation': IdealGasTranslation,
                    'NonlinearRotor': NonlinearRotor,
                    'HarmonicOscillator': HarmonicOscillator,
                    'LinearRotor': LinearRotor,
                    'array': numpy.array,
                    'int32': numpy.int32,
                    'Molecule': RMGMolecule
                }
                exec resultFile in global_context, local_context
        except IOError as e:
            logging.error("Couldn't read kinetics file {0}".format(path))
            return None
        except (NameError, TypeError, SyntaxError) as e:
            logging.error('The kinetics file "{0}" was invalid:'.format(path))
            logging.exception(e)
            return None
        if 'method' not in local_context:
            logging.error(
                'The kinetics file "{0}" did not contain a method.'.format(path))
            return None
        if 'Reaction' not in local_context:
            logging.error(
                'The kinetics file "{0}" did not contain a reaction.'.format(path))
            return None
        return local_context
