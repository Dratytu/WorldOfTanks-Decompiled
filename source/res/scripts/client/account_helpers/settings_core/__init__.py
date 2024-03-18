# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/settings_core/__init__.py

# Import necessary classes and interfaces
from skeletons.account_helpers.settings_core import ISettingsCache, ISettingsCore

# The getSettingsCoreConfig function initializes the SettingsCore and SettingsCache instances
def getSettingsCoreConfig(manager):
    # Import the SettingsCache class
    from account_helpers.settings_core.SettingsCache import SettingsCache
    
    # Import the SettingsCore class
    from account_helpers.settings_core.SettingsCore import SettingsCore
    
    # Create an instance of SettingsCache
    cache = SettingsCache()
    
    # Register the cache instance with the manager, with a finalizer function 'fini'
    manager.addInstance(ISettingsCache, cache, finalizer='fini')
    
    # Create an instance of SettingsCore
    core = SettingsCore()
    
    # Register the core instance with the manager, with a finalizer function 'fini'
    manager.addInstance(ISettingsCore, core, finalizer='fini')
    
    # Initialize the cache instance
    cache.init()
    
    # Initialize the core instance
    core.init()


# The longToInt32 function converts a long integer to a 32-bit signed integer
def longToInt32(value):
    # Check if the value is within the range of a 32-bit signed integer
    if 2147483648L <= value <= 4294967295L:
        # Clear the most significant bit to ensure the value is a 32-bit signed integer
        value &= 2147483647
        # Convert the value to an integer
        value = int(value)
        # Invert the bits of the value
        value = ~value
        # Add 1 to the inverted value to get the two's complement representation
        value ^= 2147483647
    # Return the resulting value
