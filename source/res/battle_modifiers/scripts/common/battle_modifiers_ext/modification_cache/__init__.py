# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_modifiers/scripts/common/battle_modifiers_ext/modification_cache/__init__.py

# Import necessary modules for initialization of battle modifiers and constants.
import vehicle_modifications
import constants_modifications

# Initialize the battle modifiers and constants modules.
# This function initializes the necessary data structures and sets up any required
# connections to external systems or data sources.
def init():
    # Initialize the vehicle modifications module.
    vehicle_modifications.init()
    
    # Initialize the constants modifications module.
    constants_modifications.init()
