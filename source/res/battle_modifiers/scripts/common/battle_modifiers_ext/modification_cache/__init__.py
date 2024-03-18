# Python bytecode 3.8 (decompiled from Python 3.8)
# Embedded file name: battle_modifiers/scripts/common/battle_modifiers_ext/modification_cache/__init__.py

import vehicle_modifications
import constants_modifications

def init():
    vehicle_modifications.initialize()
    constants_modifications.initialize()

init()  # Call the init function at the end of the script to initialize the modules.
