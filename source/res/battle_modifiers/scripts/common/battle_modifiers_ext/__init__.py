# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_modifiers/scripts/common/battle_modifiers_ext/__init__.py

# Import necessary modules for initializing battle parameters, remappings cache,
# and modification cache.
import battle_params
import remappings_cache
import modification_cache

# Initialize battle parameters, remappings cache, and modification cache.
def init():
    # Initialize battle parameters module.
    battle_params.init()
    
    # Initialize remappings cache module.
    remappings_cache.init()
    
    # Initialize modification cache module.
    modification_cache.init()
