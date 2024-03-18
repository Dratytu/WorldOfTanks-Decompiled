# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/OfflineEntity.py

import BigWorld # Importing the BigWorld module to inherit from Entity class

class OfflineEntity(BigWorld.Entity):
    """
    OfflineEntity class represents an offline entity in the game world.
    It inherits from BigWorld's Entity class and provides functionality for offline entities.
    """
    inputHandler = None # Class variable to store the input handler

    def __init__(self):
        """
        Initializes the OfflineEntity instance.
        """
        pass

    def prerequisites(self):
        """
        Returns a list of prerequisites required for this offline entity.
        In this case, an empty list is returned, indicating no specific prerequisites.
        """
        return []

    def onEnterWorld(self, prereqs):
        """
        Called when the offline entity enters the game world.
        :param prereqs: A list of prerequisites that must be met before entering the world
        """
        pass

    def onLeaveWorld(self):
        """
        Called when the offline entity leaves the game world.
        """
        pass

    def handleKeyEvent(self, event):
        """
        Handles key events for the offline entity.
        :param event: A key event object
        :return: A boolean value indicating whether the event was handled
        """
        return False

