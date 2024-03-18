# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/GunMarkerComponent.py

import BigWorld

# Define a new class called GunMarkerComponent that inherits from BigWorld.DynamicScriptComponent
class GunMarkerComponent(BigWorld.DynamicScriptComponent):

    # The set_gunMarker method is defined here
    def set_gunMarker(self, _=None):
        # Assign the value of self.gunMarker to the variable gunMarker
        gunMarker = self.gunMarker
        # Check if gunMarker is None
        if gunMarker is None:
            # If gunMarker is None, return from the function
            return
        else:
            # Assign the player avatar to the variable avatar
            avatar = BigWorld.player()
            # Call the updateGunMarker method on the avatar, passing in the entity id, gunPosition, shotVector, and dispersion of the gunMarker
            avatar.updateGunMarker(self.entity.id, gunMarker.gunPosition, gunMarker.shotVector, gunMarker.dispersion)
            # Return from the function
            return

