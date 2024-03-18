# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/EntityMarkerComponent.py

# Import necessary modules
import typing
from script_component.DynamicScriptComponent import DynamicScriptComponent
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

# If type checking is enabled, the following types are expected
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.area_marker_ctrl import AreaMarkersController

# Define the EntityMarkerComponent class, which inherits from DynamicScriptComponent
class EntityMarkerComponent(DynamicScriptComponent):
    # Declare a dependency for IBattleSessionProvider using dependency injection
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    # Constructor for EntityMarkerComponent
    def __init__(self):
        # Call the constructor of the parent class
        super(EntityMarkerComponent, self).__init__()
        # Initialize markerID as None
        self.markerID = None
        return

    # onDestroy method, called when the component is destroyed
    def onDestroy(self):
        # Call the onDestroy method of the parent class
        super(EntityMarkerComponent, self).onDestroy()
        # Get the AreaMarkersController instance
        ctrl = self.sessionProvider.shared.areaMarker
        # Remove the marker specified by markerID
        ctrl.removeMarker(self.markerID)
        # Reset markerID to None
        self.markerID = None
        return

    # _onAvatarReady method, called when the avatar is ready
    def _onAvatarReady(self):
        # Call the _onAvatarReady method of the parent class
        super(EntityMarkerComponent, self)._onAvatarReady()
        # Get the AreaMarkersController instance
        ctrl = self.sessionProvider.shared.areaMarker
        # Create a new marker with the entity's matrix and style
        marker = ctrl.createMarker(self.entity.matrix, self.style)
        # Set the entity for the created marker
        marker.setEntity(self.
