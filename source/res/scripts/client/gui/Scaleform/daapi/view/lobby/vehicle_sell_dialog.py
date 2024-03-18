# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_sell_dialog.py

# Import necessary modules and classes
import typing
from account_helpers.AccountSettings import AccountSettings
from goodies.goodie_constants import GOODIE_VARIETY
from gui import SystemMessages, makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.customization.shared import TYPES_ORDER
from gui.Scaleform.daapi.view.meta.VehicleSellDialogMeta import VehicleSellDialogMeta
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES
from gui.goodies.demount_kit import isDemountKitApplicableTo, getDemountKitForOptDevice
from gui.impl import backport
from gui.impl.gen import R
from gui.shared import event_dispatcher
from gui.shared.formatters import text_styles, getRoleTextWithLabel
from gui.shared.formatters.tankmen import formatDeletedTankmanStr
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import getCrewCount
from gui.shared.gui_items.processors import plugins
from gui.shared.gui_items.processors.vehicle import VehicleSeller, getCustomizationItemSellCountForVehicle
from gui.shared.items_cache import CACHE_SYNC_REASON
from gui.shared.money import Currency, MONEY_UNDEFINED
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE
from gui.shared.tooltips.formatters import packActionTooltipData
from gui.shared.tooltips.formatters import packItemActionTooltipData
from gui.shared.utils import decorators
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA
from gui.shop import showBuyGoldForEquipment
from helpers import int2roman, dependency
from items import ITEM_TYPES
from items.components.c11n_constants import ItemTags
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup
from post_progression_common import TankSetupGroupsId
from skeletons.gui.game_control import IRestoreController, IWotPlusController
from skeletons.gui.goodies import IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

# Define some constants
_DK_CURRENCY = GOODIE_VARIETY.DEMOUNT_KIT_NAME
_WP_CURRENCY = 'wotPlusVSD'
_SETTINGS_KEY = 'vehicleSellDialog'
_SETTINGS_OPEN_ENTRY = 'isOpened'
_INVENTORY_SHELLS = 'inventoryShells'
_BARRACKS_DROP_DOWN_DATA_PROVIDER = [{'label': R.strings.menu.barracks.btnUnload()}, {'label': R.strings.menu.barracks.btnDissmiss()}]

class VehicleSellDialog(VehicleSellDialogMeta):
    # Declare class variables
    __itemsCache = dependency.descriptor(IItemsCache)
    __restore = dependency.descriptor(IRestoreController)
    __goodiesCache = dependency.descriptor(IGoodiesCache)
    __wotPlus = dependency.descriptor(IWotPlusController)

    # Initialize the class
    def __init__(self, ctx=None):
        super(VehicleSellDialog, self).__init__()
        self.__vehInvID = ctx.get('vehInvID', 0)
        self.__vehicle = None
        self.__nationGroupVehicles = list()
        self.__controlNumber = None
        self.__enteredControlNumber = None
        self.__income = _VSDMoney()
        self.__accountMoney = _VSDMoney()
        self.__isCrewDismissal = False
        self.__vehicleSellPrice = MONEY_UNDEFINED
        self.__items = list()
        self.__otherVehicleShells = set()
        self.__isDemountKitEnabled = False
        return

    # Handle selection changes
    def onSelectionChanged(self, itemID, toInventory, currency):
        item = self.__items[itemID]
        item.toInventory = toInventory
        item.removeCurrency = currency
        self.__updateTotalCost()
        self.__updateSubmitButton()

    # Set the crew dismissal option
    def setCrewDismissal(self, checkTankman):
        self.__isCrewDismissal = checkTankman
        if self.__useCtrlQuestion:
            self.__sendControlQuestion()
            self.as_visibleControlBlockS(True)
            self.setUserInput('')
        else:
            self.as_visibleControlBlockS(False)
            self.setUserInput(self.__controlNumber)

    # Set the user input
    def setUserInput(self, userInput):
        self.__enteredControlNumber = userInput
        self.__updateSubmitButton()

    # Sell the vehicle
    def sell(self):
        shells = []
        eqs = []
        optDevicesToSell = []
        inventory = []
        customizationItems = []
        boosters = []
        sellMap = {FITTING_TYPES.SHELL: shells,
         _INVENTORY_SHELLS: inventory,
         FITTING_TYPES.EQUIPMENT: eqs,
         FITTING_TYPES.OPTIONAL_DEVICE: optDevicesToSell,
         FITTING_TYPES.MODULE: inventory,
         FITTING_
