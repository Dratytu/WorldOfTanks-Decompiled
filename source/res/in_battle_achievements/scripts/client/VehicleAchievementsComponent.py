# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: in_battle_achievements/scripts/client/VehicleAchievementsComponent.py

import logging
import BigWorld  # Imported but not used in this class
from dossiers2.custom.records import DB_ID_TO_RECORD as ID2NAME  # Import the mapping of achievement IDs to their names

logger = logging.getLogger(__name__)  # Create a logger for this module

class VehicleAchievementsComponent(BigWorld.DynamicScriptComponent):  # Inherit from BigWorld's DynamicScriptComponent

    def __init__(self):
        super(VehicleAchievementsComponent, self).__init__()  # Call the parent class constructor
        logger.debug('[IN_BATTLE_ACHIEVEMENTS] VehicleAchievementsComponent has been initialized')  # Debug message indicating the component has been initialized

    def setSlice_achievements(self, changePath, oldValue):
        """
        Called when the 'achievements' slice is changed.

        :param changePath: A tuple representing the start and end indices of the changed slice
        :param oldValue: The previous value of the 'achievements' slice
        """
        logger.debug('[IN_BATTLE_ACHIEVEMENTS] self.setSlice_achievements: achievements: %s, changePath: %s', self.achievements, changePath)  # Debug message with the new and changed slices

        startIndex, endIndex = changePath[-1]  # Unpack the start and end indices from the changePath tuple
        receivedAchievements = self.achievements[startIndex:endIndex]  # Get the received achievements from the new slice
        revokedAchievements = oldValue  # Get the revoked achievements from the old slice

        logger.debug('[IN_BATTLE_ACHIEVEMENTS] Received: %s - Revoked: %s', ', '.join([ID2NAME[item][1] for item in receivedAchievements
