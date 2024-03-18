# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/ProtectionZone.py

import BigWorld
import Math
from debug_utils import LOG_DEBUG

class ProtectionZone(BigWorld.Entity):
    """
    A class representing a protection zone in a game world.
    """

    def __init__(self):
        """
        Initializes a new ProtectionZone instance.
        """
        super(ProtectionZone, self).__init__(self)
        self.__lowerLeft = Math.Vector2(0, 0)  # The lower-left coordinate of the protection zone.
        self.__upperRight = Math.Vector2(0, 0)  # The upper-right coordinate of the protection zone.

    def onEnterWorld(self, prereqs):
        """
        Called when the protection zone is added to the game world.
        """
        LOG_DEBUG('ProtectionZone added ', self.zoneID)
        self.__lowerLeft = Math.Vector2(self.position.x - self.lengthX * 0.5, self.position.z - self.lengthZ * 0.5)
        self.__upperRight = Math.Vector2(self.position.x + self.lengthX * 0.5, self.position.z + self.lengthZ * 0.5)
        protectionZoneComponent = BigWorld.player().arena.componentSystem.protectionZoneComponent
        if protectionZoneComponent is not None:
            protectionZoneComponent.addProtectionZone(self)
            if self.isActive:
                protectionZoneComponent.setProtectionZoneActive(self.zoneID, self.isActive)
        return

    def onLeaveWorld(self):
        """
        Called when the protection zone is removed from the game world.
        """
        protectionZoneComponent = BigWorld.player().arena.componentSystem.protectionZoneComponent
        if protectionZoneComponent is not None:
            protectionZoneComponent.removeProtectionZone(self)
        return

    def set_isActive(self, oldValue):
        """
        Sets the active status of the protection zone.
        """
        LOG_DEBUG('ProtectionZone active: ' + str(self.isActive))
        protectionZoneComponent = BigWorld.player().arena.componentSystem.protectionZoneComponent
        if protectionZoneComponent is not None:
            protectionZoneComponent.setProtectionZoneActive(self.zoneID, self.isActive)
        return

    @property
    def bound(self):
        """
        Gets the bounding coordinates of the protection zone.
        """
        return (self.__lowerLeft, self.__upperRight)
