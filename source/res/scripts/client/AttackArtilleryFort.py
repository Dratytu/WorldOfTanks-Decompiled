# Python bytecode 2.7 (decompiled from Python 2.7)

# Embedded file name: scripts/client/AttackArtilleryFort.py

# Import necessary modules
import BigWorld
import Math
from AreaOfEffect import AreaOfEffect
from account_helpers.settings_core.settings_constants import GRAPHICS
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore

# Define the AttackArtilleryFort class, which inherits from AreaOfEffect
class AttackArtilleryFort(AreaOfEffect):
    
    # Declare dependency for ISettingsCore
    __settingsCore = dependency.descriptor(ISettingsCore)
    
    # Define a property for areaColor
    @property
    def areaColor(self):
        # Get the arenaDP from the sessionProvider
        arenaDP = self.sessionProvider.getArenaDP()
        # Check if arenaDP is not None and if it's not the ally team
        if arenaDP is not None and not arenaDP.isAllyTeam(self.team):
            # If color blind setting is enabled and enemyAreaColorBlind is not None
            if self.__settingsCore.getSetting(GRAPHICS.COLOR_BLIND) and self._equipment.enemyAreaColorBlind is not None:
                # Return enemyAreaColorBlind
                return self._equipment.enemyAreaColorBlind
            # Otherwise, return enemyAreaColor
            return self._equipment.enemyAreaColor
        # If it's the ally team or arenaDP is None, return the superclass's areaColor
        else:
            return super(AttackArtilleryFort, self).areaColor

    # Define a property for _direction
    @property
    def _direction(self):
        # Return a Math.Vector3 object with x=1, y=0, z=0
        return Math.Vector3(1, 0, 0)

    # Define a method for _showMarker
    def _showMarker(self):
        # Calculate delay as strikeTime -
