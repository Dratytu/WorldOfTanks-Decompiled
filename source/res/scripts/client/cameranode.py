# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/CameraNode.py

import BigWorld # Importing the BigWorld module for creating user data objects

class CameraNode(BigWorld.UserDataObject):
    """
    A class representing a camera node in a 3D scene.
    Inherits from BigWorld.UserDataObject, providing basic functionality.
    """

    def __init__(self):
        """
        Initializes the CameraNode instance.
        Calls the constructor of the superclass BigWorld.UserDataObject.
        """
        BigWorld.UserDataObject.__init__(self) # Initialize the superclass
