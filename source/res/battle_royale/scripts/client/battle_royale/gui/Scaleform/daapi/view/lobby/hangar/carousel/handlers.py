# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/hangar/carousel/handlers.py

# Import necessary modules and libraries
from logging import getLogger  # Import the getLogger function from the logging module
from stats_params import BATTLE_ROYALE_STATS_ENABLED  # Import the BATTLE_ROYALE_STATS_ENABLED constant
from gui.shared import event_dispatcher as shared_events  # Import shared_events from gui.shared
from gui.impl import backport  # Import the backport module from gui.impl
from gui.impl.gen import R  # Import the R constant from gui.impl.gen
from helpers import dependency  # Import the dependency module from helpers
from gui.Scaleform.locale.MENU import MENU  # Import the MENU constant from gui.Scaleform.locale.MENU
from gui.prb_control import prbDispatcherProperty  # Import prbDispatcherProperty from gui.prb_control
from gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers import SimpleVehicleCMHandler  # Subclass SimpleVehicleCMHandler
from gui.impl.gen.view_models.views.battle_royale.equipment_panel_cmp_rent_states import EquipmentPanelCmpRentStates  # Import EquipmentPanelCmpRentStates from gui.impl.gen.view_models.views.battle_royale.equipment_panel_cmp_rent_states
from skeletons.gui.game_control import IBattleRoyaleRentVehiclesController  # Dependency injection for IBattleRoyaleRentVehiclesController

# Initialize the logger for this module
_logger = getLogger(__name__)  # Create a logger instance for this module

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
        self.vehInvID = int(ctx.inventoryId)  # Set the vehicle inventory ID
        vehicle = self.itemsCache.items.getVehicle(self.vehInvID)  # Get the vehicle instance
        self.vehCD = vehicle.intCD if vehicle is not None else None  # Set the vehicle CD

    # Clear flash values
    def _clearFlashValues(self):
        self.vehInvID = None
        self.vehCD = None

    # Generate context menu options based on the given context
    def _generateOptions(self, ctx=None):
        options = []  # Initialize the options list
        vehicle = self.itemsCache.items.getVehicle(self.getVehInvID())  # Get the vehicle instance
        if vehicle is None:
            return options  # Return an empty options list if there's no vehicle
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
