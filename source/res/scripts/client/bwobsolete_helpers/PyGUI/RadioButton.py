# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/RadioButton.py

# Importing necessary modules
import BigWorld, GUI
from Button import Button
from CheckBox import CheckBox

# Defining the RadioButton class that inherits from the CheckBox class
class RadioButton(CheckBox):
    
    # Declaring the factory string
    factoryString = 'PyGUI.RadioButton'
    
    # Constructor for the RadioButton class
    def __init__(self, component):
        # Calling the constructor of the CheckBox class
        CheckBox.__init__(self, component)
        
        # Setting the button style to the radio button style
        self.buttonStyle = Button.RADIOBUTTON_STYLE

    # Static method for creating a radio button
    @staticmethod
    def create(texture, text='', groupName='', **kwargs):
        # Creating the internal component for the radio button
        b = RadioButton(CheckBox.createInternal(texture, text, **kwargs), **kwargs)
        
        # Setting the group name for the radio button
        b.groupName = groupName
        
        # Returning the created radio button component
        return b.component
