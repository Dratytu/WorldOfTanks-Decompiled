# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/hangar/carousel/handlers.py

# Import necessary modules and libraries
from logging import getLogger
from stats_params import BATTLE_ROYALE_STATS_ENABLED
from gui.shared import event_dispatcher as shared_events
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from gui.Scaleform.locale.MENU import MENU
from gui.prb_control import prbDispatcherProperty
from gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers import SimpleVehicleCMHandler
from gui.impl.gen.view_models.views.battle_royale.equipment_panel_cmp_rent_states import EquipmentPanelCmpRentStates
from skeletons.gui.game_control import IBattleRoyaleRentVehiclesController

# Initialize the logger for this module
_logger = getLogger(__name__)

# Define a class for VEHICLE constants
class VEHICLE(object):
    # Constants for various vehicle-related actions
    STATS = 'showVehicleStatistics'
    TAKE_TEST_DRIVE = 'takeToRent'
    TAKE_RENT = 'takeToRent'

# Subclass SimpleVehicleCMHandler to create a custom context menu handler for Battle Royale vehicles
class BRVehicleContextMenuHandler(SimpleVehicleCMHandler):
    # Dependency injection for IBattleRoyaleRentVehiclesController
    __rentVehiclesController = dependency.descriptor(IBattleRoyaleRentVehiclesController)

    def __init__(self, cmProxy, ctx=None):
        # Initialize the handlers dictionary with vehicle-related actions
        handlers = {VEHICLE.STATS: 'showVehicleStats',
                    VEHICLE.TAKE_TEST_DRIVE: 'takeToTestDrive',
                    VEHICLE.TAKE_RENT: 'takeToRent'}
        # Call the parent class constructor with the handlers dictionary and context
        super(BRVehicleContextMenuHandler, self).__init__(cmProxy, ctx, handlers)

    # Property for prbDispatcher
    @prbDispatcherProperty
    def prbDispatcher(self):
        return None

    # Getter for the vehicle CD
    def getVehCD(self):
        return self.vehCD

    # Getter for the vehicle inventory ID
    def getVehInvID(self):
        return self.vehInvID

    # Initialize flash values with the given context
    def _initFlashValues(self, ctx):
        self.vehInvID = int(ctx.inventoryId)
        vehicle = self.itemsCache.items.getVehicle(self.vehInvID)
        self.vehCD = vehicle.intCD if vehicle is not None else None

    # Clear flash values
    def _clearFlashValues(self):
        self.vehInvID = None
        self.vehCD = None

    # Generate context menu options based on the given context
    def _generateOptions(self, ctx=None):
        options = []
        vehicle = self.itemsCache.items.getVehicle(self.getVehInvID())
        if vehicle is None:
            return options
        else:
            # If Battle Royale stats are enabled, add a "Show Stats" option
            if BATTLE_ROYALE_STATS_ENABLED:
                options.extend([self._makeItem(VEHICLE.STATS, MENU.contextmenu(VEHICLE.STATS), {'enabled': True})])
            rentState = self.__rentVehiclesController.getRentState(self.vehCD)
            if rentState != EquipmentPanelCmpRentStates.STATE_NORMAL:
                testDriveStates = (EquipmentPanelCmpRentStates.STATE_TEST_DRIVE_AVAILABLE, EquipmentPanelCmpRentStates.STATE_TEST_DRIVE_ACTIVE)
                rentStates = (EquipmentPanelCmpRentStates.STATE_RENT_AVAILABLE, EquipmentPanelCmpRentStates.STATE_RENT_ACTIVE)
                if rentState in testDriveStates:
                    # If the vehicle is available for test drive, add a "Take Test Drive" option
                    days = self.__rentVehiclesController.getNextTestDriveDaysTotal(self.vehCD)
                    text = backport.text(R.strings.menu.battleRoyale.contextMenu.takeTestDrive(), days=days)
                    options.extend([self._makeItem(VEHICLE.TAKE_TEST_DRIVE, text, {'enabled': rentState == EquipmentPanelCmpRentStates.STATE_TEST_DRIVE_AVAILABLE})])
                elif rentState in rentStates:
                    # If the vehicle is available for rent, add a "Take Rent" option
                    isEnough = self.__rentVehiclesController.isEnoughMoneyToPurchase(self.vehCD)
                    isEnabled = rentState == EquipmentPanelCmpRentStates.STATE_RENT_AVAILABLE and isEnough
                    days = self.__rentVehiclesController.getNextRentDaysTotal(self.vehCD)
                    text = backport.text(R.strings.menu.battleRoyale.contextMenu.takeRent(), days=days)
                    options.extend([self._makeItem(VEHICLE.TAKE_RENT, text, {'enabled': isEnabled})])
            return options

    # Handle the "Take Rent" action
    def takeToRent(self):
        self.__rentVehiclesController.purchaseRent(self.vehCD)

    # Handle the "Show Stats" action
    def showVehicleStats(self):
        shared_events.showVehicleStats(self.getVehCD(), 'battleRoyale')
