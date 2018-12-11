# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/storage/__init__.py
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.storage.forsell.for_sell_view import StorageCategoryForSellView
from gui.Scaleform.daapi.view.lobby.storage.forsell.forsell_cm_handlers import ForSellCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inhangar.all_vehicles_tab import AllVehiclesTabView
from gui.Scaleform.daapi.view.lobby.storage.inhangar.in_hangar_view import StorageCategoryInHangarView
from gui.Scaleform.daapi.view.lobby.storage.inhangar.in_hangar_view import StorageVehicleFilterPopover
from gui.Scaleform.daapi.view.lobby.storage.inhangar.inhangar_cm_handlers import VehiclesRegularCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inhangar.inhangar_cm_handlers import VehiclesRestoreCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inhangar.restore_vehicles_tab import RestoreVehiclesTabView
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_cm_handlers import ModulesShellsCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_cm_handlers import EquipmentCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_cm_handlers import BattleBoostersCMHandler
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_view import InventoryCategoryStorageView
from gui.Scaleform.daapi.view.lobby.storage.inventory.modules_tab import ModulesTabView
from gui.Scaleform.daapi.view.lobby.storage.inventory.regular_items_tab import RegularItemsTabView
from gui.Scaleform.daapi.view.lobby.storage.inventory.select_vehicle_popover import VehicleSelectPopover
from gui.Scaleform.daapi.view.lobby.storage.inventory.shells_tab import ShellsTabView
from gui.Scaleform.daapi.view.lobby.storage.personalreserves.boosters_cm_handlers import PersonalReservesCMHandler
from gui.Scaleform.daapi.view.lobby.storage.personalreserves.boosters_view import StorageCategoryPersonalReservesView
from gui.Scaleform.framework import ViewSettings, ViewTypes, ScopeTemplates, GroupedViewSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE

def getContextMenuHandlers():
    return ((CONTEXT_MENU_HANDLER_TYPE.STORAGE_FOR_SELL_ITEM, ForSellCMHandler),
     (CONTEXT_MENU_HANDLER_TYPE.STORAGE_MODULES_SHELLS_ITEM, ModulesShellsCMHandler),
     (CONTEXT_MENU_HANDLER_TYPE.STORAGE_EQUIPMENT_ITEM, EquipmentCMHandler),
     (CONTEXT_MENU_HANDLER_TYPE.STORAGE_BONS_ITEM, BattleBoostersCMHandler),
     (CONTEXT_MENU_HANDLER_TYPE.STORAGE_VEHICLES_REGULAR_ITEM, VehiclesRegularCMHandler),
     (CONTEXT_MENU_HANDLER_TYPE.STORAGE_VEHICLES_RESTORE_ITEM, VehiclesRestoreCMHandler),
     (CONTEXT_MENU_HANDLER_TYPE.STORAGE_PERSONAL_RESERVE_ITEM, PersonalReservesCMHandler))


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.storage.storage_view import StorageView
    return (ViewSettings(VIEW_ALIAS.LOBBY_STORAGE, StorageView, 'storageView.swf', ViewTypes.LOBBY_SUB, VIEW_ALIAS.LOBBY_STORAGE, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(STORAGE_CONSTANTS.FOR_SELL_VIEW, StorageCategoryForSellView, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(STORAGE_CONSTANTS.IN_HANGAR_VIEW, StorageCategoryInHangarView, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(STORAGE_CONSTANTS.IN_HANGAR_ALL_VEHICLES_TAB, AllVehiclesTabView, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(STORAGE_CONSTANTS.IN_HANGAR_RESTORE_VEHICLES_TAB, RestoreVehiclesTabView, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(STORAGE_CONSTANTS.STORAGE_VIEW, InventoryCategoryStorageView, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(STORAGE_CONSTANTS.STORAGE_REGULAR_ITEMS_TAB, RegularItemsTabView, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(STORAGE_CONSTANTS.STORAGE_MODULES_TAB, ModulesTabView, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(STORAGE_CONSTANTS.STORAGE_SHELLS_TAB, ShellsTabView, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     ViewSettings(STORAGE_CONSTANTS.PERSONAL_RESERVES_VIEW, StorageCategoryPersonalReservesView, None, ViewTypes.COMPONENT, None, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.STORAGE_VEHICLES_FILTER_POPOVER, StorageVehicleFilterPopover, 'vehiclesFiltersPopoverView.swf', ViewTypes.WINDOW, VIEW_ALIAS.STORAGE_VEHICLES_FILTER_POPOVER, VIEW_ALIAS.STORAGE_VEHICLES_FILTER_POPOVER, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.STORAGE_VEHICLE_SELECTOR_POPOVER, VehicleSelectPopover, 'storageVehicleSelectorPopover.swf', ViewTypes.WINDOW, VIEW_ALIAS.STORAGE_VEHICLE_SELECTOR_POPOVER, VIEW_ALIAS.STORAGE_VEHICLE_SELECTOR_POPOVER, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (StoragePackageBusinessHandler(),)


class StoragePackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = ((VIEW_ALIAS.LOBBY_STORAGE, self.loadViewByCtxEvent), (VIEW_ALIAS.STORAGE_VEHICLES_FILTER_POPOVER, self.loadViewByCtxEvent), (VIEW_ALIAS.STORAGE_VEHICLE_SELECTOR_POPOVER, self.loadViewByCtxEvent))
        super(StoragePackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)