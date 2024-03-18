# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/hangar/carousel/data_provider.py

# Import necessary modules and classes
from gui import GUI_NATIONS_ORDER_INDEX
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.carousel_data_provider import HangarCarouselDataProvider
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.battle_royale.equipment_panel_cmp_rent_states import EquipmentPanelCmpRentStates
from gui.shared.gui_items.Vehicle import Vehicle, VEHICLE_TYPES_ORDER_INDICES
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleRentVehiclesController

# Define an undefined vehicle type
_UNDEFINED_VEHICLE_TYPE = 'undefined'

# Subclass HangarCarouselDataProvider to create RoyaleCarouselDataProvider
class RoyaleCarouselDataProvider(HangarCarouselDataProvider):
    # Inject IBattleRoyaleRentVehiclesController as a dependency
    __rentVehiclesController = dependency.descriptor(IBattleRoyaleRentVehiclesController)

    # Override getVehiclesIntCDs method
    def getVehiclesIntCDs(self):
        """
        Return a list of vehicle integer CDs from the current list of vehicles.
        """
        vehicledIntCDs = []
        for vehicle in self._vehicles:
            vehicledIntCDs.append(vehicle.intCD)
        return vehicledIntCDs

    # Override _getAdditionalItemsIndexes method
    def _getAdditionalItemsIndexes(self):
        """
        Return an empty list, as there are no additional items in this carousel.
        """
        return []

    # Override _setBaseCriteria method
    def _setBaseCriteria(self):
        """
        Set the base criteria for fetching vehicles from the inventory.
        """
        self._baseCriteria = REQ_CRITERIA.INVENTORY | REQ_CRITERIA.VEHICLE.BATTLE_ROYALE

    # Class method for comparing vehicles
    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        """
        Generate a comparison key for sorting vehicles in the carousel.
        """
        return (vehicle.getCustomState() == Vehicle.VEHICLE_STATE.UNSUITABLE_TO_QUEUE,
         vehicle.isRented,
         not vehicle.isInInventory,
         not vehicle.isEvent,
         not vehicle.isOnlyForBattleRoyaleBattles,
         not vehicle.isFavorite,
         GUI_NATIONS_ORDER_INDEX[vehicle.nationName],
         VEHICLE_TYPES_ORDER_INDICES[vehicle.type],
         vehicle.level,
         tuple(vehicle.buyPrices.itemPrice.price.iterallitems(byWeight=True)),
         vehicle.userName)

    # Method to check if telecom rentals are enabled
    def _isTelecomRentalsEnabled(self):
        """
        Check if telecom rentals are enabled for the battle royale mode.
        """
        return False

    # Override _buildVehicle method
    def _buildVehicle(self, vehicle):
        """
        Build a dictionary containing vehicle properties for the carousel.
        """
        result = super(RoyaleCarouselDataProvider, self)._buildVehicle(vehicle)

        # Get vehicle state and rent state
        state, _ = vehicle.getState()
        if vehicle.isOnlyForBattleRoyaleBattles:
            rentState = self.__rentVehiclesController.getRentState(vehicle.intCD)

            # Set test drive and rent-related properties
            isTestDriveEnabled = rentState == EquipmentPanelCmpRentStates.STATE_TEST_DRIVE_AVAILABLE
            rentLeft = self.__rentVehiclesController.getFormatedRentTimeLeft(vehicle.intCD)
            isRentActive = rentState in (EquipmentPanelCmpRentStates.STATE_TEST_DRIVE_ACTIVE, EquipmentPanelCmpRentStates.STATE_RENT_ACTIVE)

            # Set background lock and rent availability properties
            isBgLocked = result.get('lockBackground', False)
            isRentAvailable = rentState in (EquipmentPanelCmpRentStates.STATE_TEST_DRIVE_AVAILABLE, EquipmentPanelCmpRentStates.STATE_RENT_AVAILABLE)

            # Set vehicle properties based on the state
            vState, _ = vehicle.getState()
            result.update({'label': vehicle.shortUserName,
             'tooltip': TOOLTIPS_CONSTANTS.BATTLE_ROYALE_VEHICLE,
             'level': 0,
             'tankType': vehicle.type,
             'xpImgSource': '',
             'debutBoxesImgSource': '',
             'isUseRightBtn': True,
             'isTestDriveEnabled': isTestDriveEnabled,
             'lockBackground': isBgLocked or isRentAvailable,
             'rentLeft': rentLeft if isRentActive else ''})

            # Set info-related properties if the vehicle is not in a battle
            if vState not in (Vehicle.VEHICLE_STATE.IN_PREBATTLE,
             Vehicle.VEHICLE_STATE.DAMAGED,
             Vehicle.VEHICLE_STATE.DESTROYED,
             Vehicle.VEHICLE_STATE.EXPLODED,
             Vehicle.VE
