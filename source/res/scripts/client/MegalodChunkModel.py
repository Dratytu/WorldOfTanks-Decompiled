# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/MegalodChunkModel.py

import BigWorld # Importing BigWorld module to inherit from UserDataObject

class MegalodChunkModel(BigWorld.UserDataObject):
    """
    A class representing a MegalodChunkModel, which inherits from BigWorld's UserDataObject.
    This class is a user data object that can be used to store and manage data in the game world.
    """

    def __init__(self):
        """
        Initialize the MegalodChunkModel instance.
        Call the constructor of the parent class BigWorld.UserDataObject to set up the object.
        """
        BigWorld.UserDataObject.__init__(self)  # Calling the constructor of the parent class
