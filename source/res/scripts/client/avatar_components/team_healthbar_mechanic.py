# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/avatar_components/team_healthbar_mechanic.py

import arena_bonus_type_caps

# TeamHealthbarMechanic class handles the mechanics of displaying team health bars
class TeamHealthbarMechanic(object):

    def __init__(self):
        # Initializes the object with the following attributes:
        # - __enabled: a boolean indicating whether the team health bars are enabled
        # - __lastTeamHealthPercentage: the last known team health percentage
        self.__enabled = False
        self.__lastTeamHealthPercentage = None
        return

    def handleKey(self, isDown, key, mods):
        # Handles key presses, returns False to indicate that the key press was not handled
        return False

    def onBecomePlayer(self):
        # Called when the avatar becomes a player, checks if the team health bars are enabled
        self.__enabled = arena_bonus_type_caps.ARENA_BONUS_TYPE_CAPS.checkAny(self.arenaBonusType, arena_bonus_type_caps.BONUS_CAPS.TEAM_HEALTH_BAR)
        if not self.__enabled:
            # If not enabled, returns without updating the last team health percentage
            return
        else:
            # If enabled, resets the last team health percentage and updates the team health bars
            self.__lastTeamHealthPercentage = None
            self.arena.updateTeamHealthPercent(self.__lastTeamHealthPercentage)
            return

    def onBecomeNonPlayer(self):
        # Called when the avatar becomes a non-player, resets the last team health percentage
        if not self.__enabled:
            return
        else:
            self.__lastTeamHealthPercentage = None
            return

    def updateTeamsHealthPercentage(self, teamsHealthPercentage):
        # Called to update the team health percentage, only updates if the team health bars are enabled
        if not self.__enabled:

