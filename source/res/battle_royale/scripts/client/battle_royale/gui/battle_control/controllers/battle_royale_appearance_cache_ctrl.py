# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/battle_control/controllers/battle_royale_appearance_cache_ctrl.py

import BigWorld
from gui.battle_control.controllers.appearance_cache_ctrls import getWholeVehModels
from gui.battle_control.controllers.appearance_cache_ctrls.default_appearance_cache_ctrl import DefaultAppearanceCacheController
from items.vehicles import VehicleDescriptor

class BattleRoyaleAppearanceCacheController(DefaultAppearanceCacheController):
    # Class variable to store vehicle type names that are forced to be precached
    FORCED_CACHED_VEHICLES = ('germany:G24_VK3002DB_SH', 'france:F43_AMC_35_SH', 'china:Ch24_Type64_SH')
    # Class variable to store equipment vehicle type names
    EQUIPMENT_VEHICLES = ('germany:G00_Bomber_SH', 'china:Ch00_ClingeBot_SH')

    def arenaLoadCompleted(self):
        # Call the superclass's arenaLoadCompleted method
        super(BattleRoyaleAppearanceCacheController, self).arenaLoadCompleted()
        # Precache extra resources based on game settings and arena vehicles
        self._precacheExtraResources()

    def _precacheExtraResources(self):
        # Check if the game is running on minimum settings
        isMinSettings = not BigWorld.canToDowngradePreset()
        # Set to store vehicle descriptor names that have been precached
        cachedDescs = set()
        if isMinSettings:
            # Add the player's vehicle descriptor name to the cachedDescs set
            playerVehicleDescr = BigWorld.player().vehicleTypeDescriptor
            cachedDescs.add(playerVehicleDescr.name)
            # Load the player's vehicle appearance resources
            self._appearanceCache.loadResources(playerVehicleDescr.makeCompactDescr(), getWholeVehModels(playerVehicleDescr))
            # Loop through equipment vehicle type names
            for vehicleTypeName in BattleRoyaleAppearanceCacheController.EQUIPMENT_VEHICLES:
                # Create a vehicle descriptor for the current type name
                descr
