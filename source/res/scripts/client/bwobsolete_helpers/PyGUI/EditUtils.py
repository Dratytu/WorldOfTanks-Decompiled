# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/EditUtils.py

# This module contains utility functions for working with BigWorld and GUI components

import BigWorld, GUI, Math, ResMgr # Import necessary modules

def setup():
    # Initialize the camera to CursorCamera and set the cursor to the default one
    BigWorld.camera(BigWorld.CursorCamera())
    BigWorld.setCursor(GUI.mcursor())
    GUI.mcursor().visible = True # Make the cursor visible


def clearAll():
    # Clear all GUI roots
    while len(GUI.roots()):
        GUI.delRoot(GUI.roots()[0])


def clone(component):
    # Purge the temporary clone file and save the given component to it
    ResMgr.purge('gui/temp_clone.gui', True)
    component.save('gui/temp_clone.gui')
    # Load the saved component from the temporary clone file
    return GUI.load('gui/temp_clone.gui')


weatherWindow = None # Global variable to store the weather window

def weather():
    global weatherWindow # Declare weatherWindow as global
    setup() # Set up the camera and cursor
    # Load the weather window and add it as a root
    weatherWindow = GUI.load('gui/weather_window.gui')
    GUI.addRoot(weatherWindow)
    return weatherWindow


def saveWeather():
    if weatherWindow: # If the weather window exists
        weatherWindow.save('gui/weather_window.gui') # Save the weather window
