# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/prb_control/entities/tournament/pre_queue/permissions.py

# Importing the PreQueuePermissions class from the base pre-queue permissions module
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions

# Defining the BattleRoyaleTournamentPermissions class, which inherits from PreQueuePermissions
class BattleRoyaleTournamentPermissions(PreQueuePermissions):

    # Overriding the canCreateSquad method from the base class
    def canCreateSquad(self):
        # Returning False, indicating that squad creation is not allowed
        return False

