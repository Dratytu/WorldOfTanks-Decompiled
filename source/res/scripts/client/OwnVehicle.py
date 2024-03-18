# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/OwnVehicle.py

import logging
import BigWorld
from OwnVehicleBase import OwnVehicleBase
from Avatar import PlayerAvatar

# Initialize the logger for this module
_logger = logging.getLogger(__name__)

# Subclass OwnVehicleBase to create OwnVehicle
class OwnVehicle(OwnVehicleBase):

    # Override the _avatar() method from OwnVehicleBase
    def _avatar(self):
        # Get the avatar object from BigWorld.player()
        avatar = BigWorld.player()
        # Check if the avatar is an observer
        if avatar.isObserver():
            # If so, get the vehicle attached to the avatar
            attachedVehicle = avatar.getVehicleAttached()
            # Check if the attached vehicle exists and its ID matches this entity's ID
            if not attachedVehicle or attachedVehicle.id != self.entity.id:
                # If not, return None
                return None
        # If the avatar is not an observer or the attached vehicle matches this entity, return the avatar
        return avatar

    # New method to log messages
    def _doLog(self, msg):
        # Log the message as info level
        _logger.info(msg)

    # New method to get the server time
    def _serverTime(self):
        # Return the server time from BigWorld
        return BigWorld.serverTime()
