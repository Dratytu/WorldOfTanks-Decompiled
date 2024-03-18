# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/pre_queue/permissions.py

# Import necessary modules and classes
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions
from helpers import time_utils, dependency
from gui.periodic_battles.models import PrimeTimeStatus
from skeletons.gui.game_control import IBattleRoyaleController

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
            return False

        # If there is a current season and the superclass's canCreateSquad method returns True
        if currentSeason and super(BattleRoyalePermissions, self).canCreateSquad():
            # Check if the current season has an active cycle
            if currentSeason.hasActiveCycle(time_utils.getCurrentLocalServerTimestamp()):
                # Return True if there is an active cycle
                return True

        # Return False if prime time is available but no active cycle found
        return False
