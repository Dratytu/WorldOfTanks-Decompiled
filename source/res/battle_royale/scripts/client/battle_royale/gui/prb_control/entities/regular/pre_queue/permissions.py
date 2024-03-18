# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/pre_queue/permissions.py

# Import necessary modules and classes
import time_utils  # for getting the current local server timestamp
from helpers import dependency  # for dependency injection
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions  # for inheritance
from gui.periodic_battles.models import PrimeTimeStatus  # for checking prime time status
from skeletons.gui.game_control import IBattleRoyaleController  # for IBattleRoyaleController dependency

# Define the BattleRoyalePermissions class, which inherits from PreQueuePermissions
class BattleRoyalePermissions(PreQueuePermissions):
    # Inject the IBattleRoyaleController dependency
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)

    # Implement the canCreateSquad method
    def canCreateSquad(self):
        # Get the current season from the IBattleRoyaleController
        currentSeason = self.__battleRoyaleController.getCurrentSeason()

        # Get the prime time status
        status, _, _ = self.__battleRoyaleController.getPrimeTimeStatus()

        # Check if prime time is not available
        if status != PrimeTimeStatus.AVAILABLE:
            # Return False if prime time is not available
            return False

        # If there is a current season and the superclass's canCreateSquad method returns True
        if currentSeason and super(BattleRoyalePermissions, self).canCreateSquad():
            # Check if the current season has an active cycle
            if currentSeason.hasActiveCycle(time_utils.getCurrentLocalServerTimestamp()):
                # Return True if there is an active cycle
                return True

        # Return False if prime time is available but no active cycle found
        return False
