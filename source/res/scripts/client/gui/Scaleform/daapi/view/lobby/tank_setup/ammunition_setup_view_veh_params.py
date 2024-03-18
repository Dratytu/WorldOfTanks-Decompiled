# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/tank_setup/ammunition_setup_view_veh_params.py

# Importing necessary modules and classes
from gui.Scaleform.daapi.view.lobby.hangar.VehicleParameters import VehicleParameters
from gui.Scaleform.daapi.view.lobby.tank_setup.ammunition_setup_vehicle import g_tankSetupVehicle
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS

# Defining the AmmunitionSetupViewVehicleParams class that inherits from VehicleParameters
class AmmunitionSetupViewVehicleParams(VehicleParameters):

    # Overriding the _createDataProvider method to return a TankSetupParamsDataProvider instance
    def _createDataProvider(self):
        return TankSetupParamsDataProvider(TOOLTIPS_CONSTANTS.VEHICLE_TANK_SETUP_PARAMETERS)

    # Overriding the _getVehicleCache method to return the g_tankSetupVehicle instance
    def _getVehicleCache(self):
        return g_tankSetupVehicle

