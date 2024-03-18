# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/Window.py

# This script defines three classes related to creating and managing GUI windows:
#   - Window: A base class for creating a window with a texture.
#   - EscapableWindow: A window that can be closed by pressing the Escape key.
#   - DraggableWindow: A window that can be dragged around the screen.

import BigWorld, GUI, Keys
from PyGUIBase import PyGUIBase
from DraggableComponent import DraggableComponent

# The Window class is a base class for creating a window with a texture.
class Window(PyGUIBase):
    # The factoryString class attribute is a string used to identify the class.
    factoryString = 'PyGUI.Window'

    # The constructor initializes the Window instance with a component.
    def __init__(self, component):
        # Call the constructor of the superclass (PyGUIBase).
        PyGUIBase.__init__(self, component)
        # Store the component in the script attribute of the component.
        component.script = self

    # The onSave method is called when the window data needs to be saved.
    def onSave(self, dataSection):
        # Call the onSave method of the superclass (PyGUIBase).
        PyGUIBase.onSave(self, dataSection)

    # The onLoad method is called when the window data is loaded.
    def onLoad(self, dataSection):
        # Call the onLoad method of the superclass (PyGUIBase).
        PyGUIBase.onLoad(self, dataSection)

    # A static method to create a window with a given texture.
    @staticmethod
    def create(texture):
        # Create a new GUI window with the specified texture.
        c = GUI.Window(texture)
        # Create a new Window instance with the new window as its component.
        return Window(c).component

# The EscapableWindow class is a window that can be closed by pressing the Escape key.
class EscapableWindow(Window):
    # The factoryString class attribute is a string used to identify the class.
    factoryString = 'PyGUI.EscapableWindow'

    # The constructor initializes the EscapableWindow instance with a component.
    def __init__(self, component=None):
        # Call the constructor of the superclass (Window).
        Window.__init__(self, component)
        # Store the component in the script attribute of the component.
        component.script = self
        # Initialize the onEscape attribute to None.
        self.onEscape = None

    # The handleKeyEvent method is called when a key event occurs.
    def handleKeyEvent(self, event):
        # If the event is a key down event...
        if event.isKeyDown():
            # If the key is the Escape key...
            if event.key == Keys.KEY_ESCAPE:
                # If the onEscape attribute is not None...
                if self.onEscape is not None:
                    # Call the onEscape attribute.
                    self.onEscape()
                    # Return True to indicate that the event has been handled.
                    return True
        # Return False to indicate that the event has not been handled.
        return False

# The DraggableWindow class is a window that can be dragged around the screen.
class DraggableWindow(Window, DraggableComponent):
    #
