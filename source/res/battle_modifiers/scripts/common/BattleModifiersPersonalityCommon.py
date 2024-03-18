# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_modifiers/scripts/common/BattleModifiersPersonalityCommon.py

# Import necessary modules for the script
import extension_rules
import battle_modifiers_ext

# Define a function for pre-initialization
def preInit():
    # Call the init() function from the extension_rules module
    extension_rules.init()
    
    # Call the init() function from the battle_modifiers_ext module
    battle_modifiers_ext.init()
