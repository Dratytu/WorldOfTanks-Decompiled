# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/CameraNode.py

import BigWorld # Importing the BigWorld module for creating a user data object

class CameraNode(BigWorld.UserDataObject):
    """
    A class representing a camera node in the game world.
    Inherits from BigWorld.UserDataObject to enable the use of user data properties.
    """

    def __init__(self):
        """
        Initializes the CameraNode instance.
        Calls the constructor of the superclass to set up the user data object.
        """
        BigWorld.UserDataObject.__init__(self) # Calling the constructor of the superclass to set up the user data object
