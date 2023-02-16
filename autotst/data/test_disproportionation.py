# import rmgpy.data.kinetics
import rmgpy.reaction
import rmgpy.species

import autotst.reaction
# import autotst.calculator.gaussian


reaction_smiles = 'CC(CC[O])OO+[O][O]_CC(CC=O)OO+[O]O'
reaction = autotst.reaction.Reaction(label=reaction_smiles)
reaction.ts['forward'][0].get_molecules()
# reaction.generate_conformers(ase_calculator=Hotbit())
