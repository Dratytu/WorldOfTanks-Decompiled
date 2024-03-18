# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/CheckBox.py

import BigWorld, GUI
from Button import Button # Import the Button class from the Button module

class CheckBox(Button):
    factoryString = 'PyGUI.CheckBox' # A string used for factory creation

    def __init__(self, component):
        Button.__init__(self, component) # Initialize the CheckBox class by calling the Button class constructor
        self.buttonStyle = Button.CHECKBOX_STYLE # Set the button style to checkbox style

    def onBound(self):
        self.buttonIcon = self.component.box # Set the button icon to the box component
        self.buttonLabel = self.component.label # Set the button label to the label component
        self._updateVisualState() # Call the private method _updateVisualState

    @staticmethod
    def createInternal(texture, text='', **kwargs):
        c = GUI.Window('') # Create a new GUI window
        c.materialFX = GUI.Simple.eMaterialFX.BLEND # Set the material effect to blend
        c.widthMode = GUI.Simple.eSizeMode.CLIP # Set the width mode to clip
        c.heightMode = GUI.Simple.eSizeMode.CLIP # Set the height mode to clip
        c.horizontalPositionMode = GUI.Simple.ePositionMode.CLIP # Set the horizontal position mode to clip
        c.verticalPositionMode = GUI.Simple.ePositionMode.CLIP # Set the vertical position mode to clip
        box = GUI.Simple(texture) # Create a new GUI simple object
        box.size = (0, 0) # Set the size to 0, 0
        box.horizontalPositionMode = GUI.Simple.ePositionMode.CLIP # Set the horizontal position mode to clip
        box.verticalPositionMode = GUI.Simple.ePositionMode.CLIP # Set the vertical position mode to clip
        box.horizontalAnchor = GUI.Simple.eHAnchor.LEFT # Set the horizontal anchor to left
        box.position.x = -1 # Set the x position to -1
        box.materialFX = GUI.Simple.eMaterialFX.BLEND # Set the material effect to blend
        box.widthMode = GUI.Simple.eSizeMode.PIXEL # Set the width mode to pixel
        box.heightMode = GUI.Simple.eSizeMode.PIXEL # Set the height mode to pixel
        box.width = 20 # Set the width to 20
        box.height = 20 # Set the height to 20
        c.addChild(box, 'box') # Add the box to the window
        label = GUI.Text(text) # Create a new GUI text object
        label.horizontalPositionMode = GUI.Simple.ePositionMode.CLIP # Set the horizontal position mode to clip
        label.verticalPositionMode = GUI.Simple.ePositionMode.CLIP # Set the vertical position mode to clip
        label.horizontalAnchor = GUI.Simple.eHAnchor.RIGHT # Set the horizontal anchor to right
        label.position.
