# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/permissions.py

from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions

class FunRandomPermissions(PreQueuePermissions, FunSubModesWatcher):
    """
    A class representing the permissions for the Fun Random pre-queue. This class is a subclass of PreQueuePermissions and FunSubModesWatcher.
    """

    @hasDesiredSubMode(defReturn=False)
    def canCreateSquad(self):
        """
        A method that checks if the player is allowed to create a squad in the current sub mode.

        Returns:
            bool: True if the player is allowed to create a squad, False otherwise.
        """
        canCreateSquad = super(FunRandomPermissions, self).canCreateSquad()
        # The super() call invokes the parent class's canCreateSquad() method, which checks if the player is allowed to create a squad
        # based on their permissions and the current game mode.

        return canCreateSquad and self.getDesiredSubMode().isSquadAvailable()
        # The method returns True only if the player is allowed to create a squad (as determined by the super() call) and
        # the desired sub mode has squads available.
