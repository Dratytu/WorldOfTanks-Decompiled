# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/ArtilleryEquipment.py

import math_utils
import BigWorld

# Define the ArtilleryEquipment class that inherits from BigWorld.UserDataObject
class ArtilleryEquipment(BigWorld.UserDataObject):
    # Define a read-only property for launchVelocity
    @property
    def launchVelocity(self):
        return self.__launchVelocity

    def __init__(self):
        # Call the constructor of BigWorld.UserDataObject
        BigWorld.UserDataObject.__init__(self)

        # Extract yaw and pitch from the instance's __dict__
        launch_dir = math_utils.createRotationMatrix((self.__dict__['yaw'], self.__dict__['pitch'], 0)).applyToAxis(2)

        # Normalize the launch direction
        launch_dir.normalise()

        # Calculate and store the launch velocity
        self.__launchVelocity = launch_dir * self.speed
