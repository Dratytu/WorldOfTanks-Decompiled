# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/ExampleDestructible.py

import BigWorld  # Import the BigWorld module for creating entities
from debug_utils import LOG_DEBUG, LOG_ERROR  # Import logging functions for debug and error messages
from constants import DESTRUCTIBLE_MATKIND  # Import constants for destructible material kinds

class ExampleDestructible(BigWorld.Entity):
    """
    ExampleDestructible is a class that represents a destructible entity in the game world.
    It inherits from BigWorld.Entity and has various methods for handling damage and health changes.
    """
    __MATKINDS_ALL = range(DESTRUCTIBLE_MATKIND.NORMAL_MIN, DESTRUCTIBLE_MATKIND.DAMAGED_MAX + 1)
    __MODEL_NAME = 'content/MilitaryEnvironment/mleSU_83_02_OpelBlitz/normal/lod0/mleSU_83_02_OpelBlitz_01.model'

    def __init__(self):
        """
        Initialize the ExampleDestructible object.
        Set the __materialDisabler attribute to None.
        """
        self.__materialDisabler = None
        return

    def prerequisites(self):
        """
        Return a list containing the name of the model required for this destructible entity.
        """
        return [self.__MODEL_NAME]

    def showDamage(self, componentID, isShotDamage):
        """
        Log a debug message indicating that damage has been shown on a specific component of the destructible entity.
        """
        LOG_DEBUG('ExampleDestructible.showDamage %d %b', componentID, isShotDamage)

    def set_health(self, prev):
        """
        Log a debug message indicating that the health of the destructible entity has been changed.
        Call the __onHealthChanged method.
        """
        LOG_DEBUG('ExampleDestructible.set_health %d' % self.health)
        self.__onHealthChanged()

    def onEnterWorld(self, prereqs):
        """
        Called when the destructible entity is added to the game world.
        If any of the required models failed to load, log an error message and return.
        Otherwise, set the model attribute to the loaded model, add a motor to it, and create a material disabler.
        Set the matDisabler attribute of the model to the material disabler and set the __materialDisabler attribute to it.
        Call the __onHealthChanged method.
        """
        if prereqs.failedIDs:
            LOG_ERROR('Failed
