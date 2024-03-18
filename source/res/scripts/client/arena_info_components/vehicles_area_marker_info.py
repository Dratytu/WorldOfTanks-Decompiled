# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/arena_info_components/vehicles_area_marker_info.py

class VehiclesAreaMarkerInfo(object):
    """
    A class that handles the setting of vehicle area marker parameters in the game world.
    """

    def onEnterWorld(self):
        """
        A method that gets called when the object enters the game world.
        It sets the vehicle area marker parameters.
        """
        self._setVehiclesAreaMarkerParams()

    def onLeaveWorld(self):
        """
        A method that gets called when the object leaves the game world.
        In this case, no specific action is taken when leaving the world.
        """
        pass

    def set_vehiclesAreaMarkerParams(self, _):
        """
        A method that sets the vehicle area marker parameters.
        The underscore parameter is not used in this method.
        """
        self._setVehiclesAreaMarkerParams()

    def _setVehiclesAreaMarkerParams(self):
        """
        A private method that sets the vehicle area marker parameters.
        It uses the session provider to get the area marker controller,
        and sets the vehicle area marker parameters if they are not None
        and the area marker controller is available.
        """
        areaMarkerCtrl = self.sessionProvider.shared.areaMarker
        if self.vehiclesAreaMarkerParams is not None and areaMarkerCtrl:
            areaMarkerCtrl.setVehiclesAreaMarkerParams(self.vehiclesAreaMarkerParams)
        return

