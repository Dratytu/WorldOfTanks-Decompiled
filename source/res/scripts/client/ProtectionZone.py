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
        # Call the constructor of the superclass (BigWorld.Entity)
        super(ProtectionZone, self).__init__(self)
        
        # Initialize the lower-left and upper-right coordinates of the protection zone
        self.__lowerLeft = Math.Vector2(0, 0)
        self.__upperRight = Math.Vector2(0, 0)

    def onEnterWorld(self, prereqs):
        """
        Called when the protection zone is added to the game world.
        """
        # Log a debug message with the protection zone's ID
        LOG_DEBUG('ProtectionZone added ' + str(self.zoneID))
        
        # Calculate the lower-left and upper-right coordinates of the protection zone
        self.__lowerLeft = Math.Vector2(self.position.x - self.lengthX * 0.5, self.position.z - self.lengthZ * 0.5)
        self.__upperRight = Math.Vector2(self.position.x + self.lengthX * 0.5, self.position.z + self.lengthZ * 0.5)
        
        # Get the protection zone component of the game world
        protectionZoneComponent = BigWorld.player().arena.componentSystem.protectionZoneComponent
        
        # If the protection zone component exists
        if protectionZoneComponent is not None:
            # Add the protection zone to the component
            protectionZoneComponent.addProtectionZone(self)
            
            # If the protection zone is active
            if self.isActive:
                # Set the protection zone as active in the component
                protectionZoneComponent.setProtectionZoneActive(self.zoneID, self.isActive)

    def onLeaveWorld(self):
        """
        Called when the protection zone is removed from the game world.
        """
        # Get the protection zone component of the game world
        protectionZoneComponent = BigWorld.player().arena.componentSystem.protectionZoneComponent
        
        # If the protection zone component exists
        if protectionZoneComponent is not None:
            # Remove the protection zone from the component
            protectionZoneComponent.removeProtectionZone(self)

    def set_isActive(self, oldValue):
        """
        Sets the active status of the protection zone.
        """
        # Log a debug message with the new active status
        LOG_DEBUG('ProtectionZone active: ' + str(self.isActive))
        
        # Get the protection zone component of the game world
        protectionZoneComponent = BigWorld.player().arena.componentSystem.protectionZoneComponent
        
        # If the protection zone component exists
        if protectionZoneComponent is not None:
            # Set the protection zone as active in the component
            protectionZoneComponent.setProtectionZoneActive(self.zoneID, self.isActive)

    @property
    def bound(self):
        """
        Gets the bounding coordinates of the protection zone.
        """
        # Return the lower-left and upper-right coordinates of the protection zone
        return (self.__lowerLeft, self.__upperRight)
