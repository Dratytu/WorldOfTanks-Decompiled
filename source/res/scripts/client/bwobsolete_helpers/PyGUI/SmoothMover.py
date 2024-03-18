# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/SmoothMover.py

import BigWorld, GUI, Math, Keys
from PyGUIBase import PyGUIBase  # Importing the PyGUIBase class from PyGUIBase module

class SmoothMover(PyGUIBase):  # Defining a new class SmoothMover that inherits from PyGUIBase
    factoryString = 'PyGUI.SmoothMover'  # A string that identifies the factory that creates this object

    def __init__(self, component):
        PyGUIBase.__init__(self, component)  # Calling the constructor of the parent class

        # Initializing class variables
        self.minScroll = [0, 0]
        self.maxScroll = [0, 0]
        self.scroll = [0, 0]
        self.scrollSpeed = 0.5
        self.scrollTransform = Math.Matrix()
        self.scrollTransform.setIdentity()

    def scrollTo(self, x, y, animate=True):
        # Setting the scroll position to the new position if it's within the allowed range
        self.scroll[0] = max(x, self.minScroll[0])
        self.scroll[0] = min(self.scroll[0], self.maxScroll[0])
        self.scroll[1] = max(y, self.minScroll[1])
        self.scroll[1] = min(self.scroll[1], self.maxScroll[1])

        # Creating a new scroll transform with the new scroll position
        self.scrollTransform.setTranslate((self.scroll[0], self.scroll[1], 0))

        # Setting the component's transform target to the new scroll transform
        self.component.transform.target = self.scrollTransform

        # Setting the component's transform eta to the scroll speed if animate is True, otherwise setting it to 0
        self.component.transform.eta = self.scrollSpeed if animate else 0.0

    def scrollBy(self, x, y):
        # Calling scrollTo with the current scroll position plus the given offsets
        self.scrollTo(self.scroll[0] + x, self.scroll[1] + y)

    def canScrollUp(self):
        # Checking if the current scroll position is greater than the minimum scroll position by a small threshold

