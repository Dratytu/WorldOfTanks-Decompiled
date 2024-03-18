# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/ScrollWindow.py

import BigWorld  # Importing BigWorld for playing sounds and handling component scroll positions
import GUI  # Importing GUI for handling key events
from PyGUIBase import PyGUIBase  # Importing PyGUIBase for inheritance and initialization

class ScrollWindow(PyGUIBase):
    """
    A ScrollWindow class that inherits from PyGUIBase and provides scrolling functionality to its component.
    """
    factoryString = 'PyGUI.ScrollWindow'  # A string that identifies the factory used to create this object

    def __init__(self, component):
        """
        Initializes the ScrollWindow instance with a given component.

        :param component: The component to be associated with this ScrollWindow.
        """
        PyGUIBase.__init__(self, component)  # Calling the constructor of the parent class

    def handleKeyEvent(self, event):
        """
        Handles key events for scrolling the window up, down, left, or right.

        :param event: The key event to be handled.
        :return: True if the event is handled, False otherwise.
        """
        c = self.component  # Shortening the reference to the component
        key = event.key  # Storing the key from the event
        down = event.isKeyDown()  # Checking if the key is pressed down

        if down:
            if key == Keys.KEY_JOYDUP or key == Keys.KEY_UPARROW:
                # Scroll up when the up arrow or joypad up button is pressed
                x, y = c.scroll
                y += 0.1
                c.scroll = (x, y)
                BigWorld.playSound('ui/tick')  # Play a sound when scrolling
                return True
            if key == Keys.KEY_JOYDDOWN or key == Keys.KEY_DOWNARROW:
                # Scroll down when the down arrow or joypad down button is pressed
                x, y = c.scroll
                y -= 0.1
                c.scroll = (x, y)
                BigWorld.playSound('ui/tick')  # Play a sound when scrolling
                return True
            if key == Keys.KEY_JOYDRIGHT or key == Keys.KEY_RIGHTARROW:
                # Scroll right when the right arrow or joypad right button is pressed
                x, y = c.scroll
                x += 0.1
                c.scroll = (x, y)
                BigWorld.playSound('ui/tick')  # Play a sound when scrolling
                return True
            if key == Keys.KEY_JOYDLEFT or key == Keys.KEY_LEFTARROW:
                # Scroll left when the left arrow or joypad left button is pressed
                x, y = c.scroll
                x -= 0.1
                c.scroll = (x, y)
                BigWorld.playSound('ui/tick')  # Play a sound when scrolling
                return True

        return False


class ZoomScrollWindow(ScrollWindow):
    """
    A ZoomScrollWindow class that inherits from ScrollWindow and provides zooming functionality to its component.
    """
    factoryString = 'PyGUI.ZoomScrollWindow'  # A string that identifies the factory used to create this object

    def __init__(self, component):
        """
        Initializes the ZoomScrollWindow instance with a given component and sets the initial zoom factor to 1.

        :param component: The component to be associated with this ZoomScrollWindow.
        """
        ScrollWindow.__init__(self, component)  # Calling the constructor of the parent class
        self.zoomFactor = 1  # Initializing the zoom factor

    def updateScrollLimits(self):
        """
        Updates the scroll limits based on the component's dimensions and the current zoom factor.
        """
        c = self.component.children[0][1]  # Shortening the reference to the component's child
        w, h = c.width, c.height  # Storing the width and height of the component's child

        x, y = self.component.maxScroll  # Storing the current maximum scroll position
        x = (w - self.component.width) / 2  # Calculating the new maximum scroll x position
        y = (h - self.component.height) / 2  # Calculating the new maximum scroll y position

        self.component.maxScroll = (x, y)  # Updating the maximum scroll position
        self.component.
