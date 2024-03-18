# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/avatar_components/avatar_respawn_mechanic.py

# Importing the ARENA_BONUS_TYPE_CAPS constant from the arena_bonus_type_caps module
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS

# Importing the RespawnDestroyEffect class from the EffectsList module
from helpers.EffectsList import RespawnDestroyEffect

# Importing the LOG_DEBUG_DEV function from the debug_utils module
from debug_utils import LOG_DEBUG_DEV

# Defining the AvatarRespawnMechanic class which inherits from the object class
class AvatarRespawnMechanic(object):
    
    # Defining a read-only property 'respawnEnabled' that returns the value of the __enabled attribute
    @property
    def respawnEnabled(self):
        return self.__enabled

    # Initializing the __enabled attribute with a default value of False
    def __init__(self):
        self.__enabled = False

    # The onBecomePlayer method is called when the avatar becomes a player
    def onBecomePlayer(self):
        # The method checks if any of the arena bonus types have the RESPAWN bonus type cap
        # If so, it sets the __enabled attribute to True, otherwise it remains False
        self.__enabled = BONUS_CAPS.checkAny(self.arenaBonusType, BONUS_CAPS.RESPAWN)
        # If the __enabled attribute is True, the method returns None, otherwise it also returns None
        return None if not self.__enabled else None

    # The handleKey method is called when a key is pressed or released
    def handleKey(self, isDown, key, mods):
        # The method always returns False
        return False

    # The onBecomeNonPlayer method is called when the avatar becomes a non-player
    def onBecomeNonPlayer(self):
        # If the __enabled attribute is True, the method returns None, otherwise it also returns None
        return None if not self.__enabled else None

    # The updateRespawnVehicles method is called to update the respawn vehicles
    def updateRespawnVehicles(self, vehsList):
        # If the __enabled attribute is False, the method returns without doing anything
        if not self.__enabled:
            return
        # The method gets the respawn controller and calls the updateRespawnVehicles method on it
        ctrl = self.guiSessionProvider.dynamic.respawn
        if ctrl is not None:
            ctrl.updateRespawnVehicles(vehsList)
        # The method returns without doing anything
        return

    # The updateRespawnCooldowns method is called to update the respawn cooldowns
    def updateRespawnCooldowns(self, cooldowns):
        # If the __enabled attribute is False, the method returns without doing anything
        if not self.__enabled:
            return
        # The method logs the cooldowns and converts them to a dictionary
        LOG_DEBUG_DEV('updateRespawnCooldowns ', cooldowns)
        cooldowns = {item['vehTypeCompDescr']:item['endOfCooldownPiT'] for item in cooldowns}
        # The method gets the respawn controller and calls the updateRespawnCooldowns method on it
        ctrl = self.guiSessionProvider.dynamic.respawn
        if ctrl is not None:
            ctrl.updateRespawnCooldowns(cooldowns)
        # The method returns without doing anything
        return

    # The updateRespawnInfo method is called to update the respawn information
    def updateRespawnInfo(self, respawnInfo):
        # If the __enabled attribute is False, the method returns without doing anything
        if not self.__enabled:
            return
        # The method gets the respawn controller and calls the updateRespawnInfo method on it
        ctrl = self.guiSessionProvider.dynamic.respawn
        if ctrl is not None:
            ctrl.updateRespawnInfo(respawnInfo)
        # The method returns without doing anything
        return

    # The updateVehicleLimits method is called to update the vehicle limits
    def updateVehicleLimits(self, respawnLimits):
        # If the __enabled attribute is False, the method returns without doing anything
        if not self.__enabled:
            return
        # The method converts
