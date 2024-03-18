# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/avatar_components/VehiclesSpawnListStorage.py

import logging
import cPickle
from Event import Event  # Importing Event class from Event module

# Initialize logger for this module
_logger = logging.getLogger(__name__)

class VehiclesSpawnListStorage(object):
    """
    Class representing Vehicles Spawn List Storage component.
    """

    def __init__(self):
        """
        Initialize VehiclesSpawnListStorage object.
        """
        super(VehiclesSpawnListStorage, self).__init__()

        # Initialize Event object to handle spawn list updates
        self.onSpawnListUpdated = Event()

    def handleKey(self, isDown, key, mods):
        """
        Placeholder method for handling key events.

        :param isDown: True if key is pressed, False otherwise.
        :param key: Key code.
        :param mods: Modifier keys (e.g. shift, control).
        """
        pass

    def onBecomePlayer(self):
        """
        Placeholder method for handling becoming a player event.
        """
        pass

    def onBecomeNonPlayer(self):
        """
        Placeholder method for handling becoming a non-player event.
        """
        pass

    def updateSpawnList(self, spawnListData):
        """
        Update the spawn list with new data.

        :param spawnListData: Serialized spawn list data.
        """
        # Convert pickled spawn list data to a list of VehicleSpawnData objects
        spawnList = convertTuplesToVehicleSpawnData(cPickle.loads(spawnListData))

        # Notify subscribers that the spawn list has been updated
        self.onSpawnListUpdated(spawnList)
