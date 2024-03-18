# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bwobsolete_helpers/GraphicsOptions.py

import ResMgr # Import the ResMgr module for accessing game resources
import sys   # Import the sys module for system-specific parameters and functions
import BigWorld # Import the BigWorld module for the game world and related functionalities

# Define the list of texture detail levels using the ResMgr module
tex_detail_levels = ResMgr.openSection('system/data/texture_detail_levels.xml')

def normalMapsCompressed():
    """
    This function checks if normal maps are compressed or not.
    It reads the texture detail levels configuration and returns a boolean value
    based on the format of the normal maps.
    """
    ns = tex_detail_levels.values()[0] # Get the first namespace in the configuration
    return False if ns.readString('format') == 'A8R8G8B8' else True


def compressNormalMaps(state):
    """
    This function compresses normal maps by changing their format to 'A8R8G8B8'.
    It takes a boolean state as an argument, reads the texture detail levels configuration,
    and modifies the format if necessary. Finally, it reloads the textures using BigWorld.
    """
    ns = tex_detail_levels.values()[0] # Get the first namespace in the configuration
    ns.writeString('format', 'A8R8G8B8')  # Change the format of normal maps to 'A8R8G8B8'
    BigWorld.reloadTextures() # Reload the textures in the game world


def optIncludeOptionEnabled(value):
    """
    This function checks if the optinclude option with the given value is enabled or not.
    It reads the optinclude.fxh file and searches for the specified value.
    If found, it returns True if the value is not commented out, and False otherwise.
    If not found, it returns False.
    """
    filename = '../../bigworld/res/shaders/std_effects/optinclude.fxh'
    try:
        f = open(filename, 'r') # Open the file for reading
    except IOError:
        print 'Failed to open %s' % (filename,)
        return

    output = [] # Initialize an empty list to store the lines of the file
    lines = f.readlines() # Read all the lines from the file
    changed = False # Initialize a flag to track if any changes are made
    found = False # Initialize a flag to track if the value is found
    for line in lines:
        if value in line:
            found = True
            if '//' in line:
                return False # The value is found but commented out, so return False
            return True  # The value is found and not commented out, so return True

    return False # The value is not found in the file


def enableOptincludeOption(value, enable):
    """
    This function enables or disables the optinclude option with the given value.
    It reads the optinclude.fxh file, searches for the specified value, and updates it.
    If the value is found, it is either enabled (uncommented) or disabled (commented) based on the enable argument.
    If the value is not found, it is added to the file.
    After updating, the file is written
