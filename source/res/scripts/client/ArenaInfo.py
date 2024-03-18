# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/ArenaInfo.py

# Import necessary modules
import BigWorld
from arena_info_components.vehicles_area_marker_info import VehiclesAreaMarkerInfo
from cgf_script.entity_dyn_components import BWEntitiyComponentTracker
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

# Define the set of arena info components
ARENA_INFO_COMPONENTS = {VehiclesAreaMarkerInfo}

# Define the ArenaInfo class, which inherits from BigWorld.Entity,
# BWEntitiyComponentTracker, and VehiclesAreaMarkerInfo
class ArenaInfo(BigWorld.Entity, BWEntitiyComponentTracker, VehiclesAreaMarkerInfo):
    # Define the dependency for IBattleSessionProvider
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    # Initialize the class
    def __init__(self):
        # Initialize all components in the ARENA_INFO_COMPONENTS set
        for comp in ARENA_INFO_COMPONENTS:
            comp.__init__(self)

    # Set the plane trajectory
    def set_planeTrajectory(self, _):
        # Get the avatar (player)
        avatar = BigWorld.player()
        # If the avatar and the plane trajectory exist and the avatar can see the world,
        # update the plane trajectory for the avatar
        if self.planeTrajectory and avatar.userSeesWorld():
            avatar.updatePlaneTrajectory(self.planeTrajectory)

    # Show the carpet bombing effect
    def showCarpetBombing(self, equipmentID, position, hittingDirection, time):
        # Get the avatar (player)
        avatar = BigWorld.player()
        # If the avatar exists, show the carpet bombing effect
        if avatar is not None:
            avatar.showCarpetBombing(equipmentID, position, hittingDirection, time)
        # Return None
        return

    # Called when the entity enters the world
    def onEnterWorld(self, prereqs):
        # Initialize all components in the ARENA_INFO_COMPONENTS set
        for comp in ARENA_INFO_COMPONENTS:
           
