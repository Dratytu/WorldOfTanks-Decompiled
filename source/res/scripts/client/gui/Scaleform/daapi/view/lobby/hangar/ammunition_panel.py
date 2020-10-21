# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/ammunition_panel.py
from adisp import process
from account_helpers.settings_core.settings_constants import OnceOnlyHints
from constants import ROLE_TYPE, QUEUE_TYPE, PREBATTLE_TYPE
from CurrentVehicle import g_currentVehicle, g_currentPreviewVehicle
from gui import makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.customization.shared import getEditableStylesExtraNotificationCounter, getItemTypesAvailableForVehicle
from gui.Scaleform.daapi.view.meta.AmmunitionPanelMeta import AmmunitionPanelMeta
from gui.prb_control.entities.listener import IGlobalListener
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.prb_control.dispatcher import g_prbLoader
from gui.shared import event_dispatcher as shared_events
from gui.shared.formatters.icons import roleActionsGroup
from gui.shared.formatters import text_styles
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.gui_items.items_actions.actions import VehicleRepairAction
from helpers import i18n, dependency, int2roman
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.game_control import IBootcampController
from skeletons.gui.shared import IItemsCache
from gui.customization.shared import isVehicleCanBeCustomized
from gui.impl.gen import R
from gui.impl import backport
RESURRECT = 'resurrect'
RESURRECT_MODULE_LABEL = 'h_Resurrect'

class AmmunitionPanel(AmmunitionPanelMeta, IGlobalListener):
    __slots__ = ('__hangarMessage',)
    bootcampCtrl = dependency.descriptor(IBootcampController)
    itemsCache = dependency.descriptor(IItemsCache)
    service = dependency.descriptor(ICustomizationService)
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(AmmunitionPanel, self).__init__()
        self.__hangarMessage = None
        return

    def update(self):
        self._update()

    @process
    def showRepairDialog(self):
        if g_currentVehicle.isPresent():
            vehicle = g_currentVehicle.item
            yield VehicleRepairAction(vehicle).doAction()

    def showCustomization(self):
        self.service.showCustomization()

    def toRentContinue(self):
        if g_currentVehicle.isPresent():
            vehicle = g_currentVehicle.item
            canBuyOrRent, _ = vehicle.mayObtainForMoney(self.itemsCache.items.stats.money)
            if vehicle.isRentable and vehicle.rentalIsOver and canBuyOrRent:
                shared_events.showVehicleBuyDialog(vehicle)

    def showChangeNation(self):
        if g_currentVehicle.isPresent() and g_currentVehicle.item.hasNationGroup:
            ItemsActionsFactory.doAction(ItemsActionsFactory.CHANGE_NATION, g_currentVehicle.item.intCD)

    def showModuleInfo(self, itemCD):
        if itemCD is not None and int(itemCD) > 0:
            shared_events.showModuleInfo(itemCD, g_currentVehicle.item.descriptor)
        return

    def _populate(self):
        super(AmmunitionPanel, self)._populate()
        self.startGlobalListening()
        g_clientUpdateManager.addMoneyCallback(self.__moneyUpdateCallback)
        g_clientUpdateManager.addCallbacks({'inventory': self.__inventoryUpdateCallBack})

    def _dispose(self):
        self.stopGlobalListening()
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__hangarMessage = None
        super(AmmunitionPanel, self)._dispose()
        return

    def _update(self, onlyMoneyUpdate=False):
        if g_currentVehicle.isPresent():
            hangarMessage = g_currentVehicle.getHangarMessage()
            if onlyMoneyUpdate and self.__hangarMessage == hangarMessage:
                return
            vehicle = g_currentVehicle.item
            state = g_prbLoader.getDispatcher().getFunctionalState()
            isEvent = state.isInPreQueue(QUEUE_TYPE.EVENT_BATTLES) or state.isInUnit(PREBATTLE_TYPE.EVENT)
            if isEvent:
                vehicle = g_currentPreviewVehicle.item or g_currentVehicle.item
            self.__hangarMessage = hangarMessage
            statusId, msg, msgLvl = hangarMessage
            rentAvailable = False
            if statusId in (Vehicle.VEHICLE_STATE.RENTAL_IS_OVER, Vehicle.VEHICLE_STATE.RENTABLE_AGAIN):
                canBuyOrRent, _ = vehicle.mayObtainForMoney(self.itemsCache.items.stats.money)
                rentAvailable = vehicle.isRentable and canBuyOrRent
            if msgLvl == Vehicle.VEHICLE_STATE_LEVEL.RENTABLE:
                msgLvl = Vehicle.VEHICLE_STATE_LEVEL.INFO
            msg, msgLvl = self.__applyGamemodeOverrides(statusId, i18n.makeString(msg), msgLvl)
            msgString = ''
            if statusId != Vehicle.VEHICLE_STATE.UNDAMAGED or msgLvl == Vehicle.VEHICLE_STATE_LEVEL.ACTIONS_GROUP:
                msgString = makeHtmlString('html_templates:vehicleStatus', msgLvl, {'message': msg})
            roleID = ROLE_TYPE.NOT_DEFINED
            if msgLvl == Vehicle.VEHICLE_STATE_LEVEL.ACTIONS_GROUP:
                roleID = vehicle.role
            vehicleLevel = '{}'.format(int2roman(vehicle.level)) if not isEvent else ''
            self.__applyCustomizationNewCounter(vehicle)
            self.__updateDevices(vehicle)
            self.as_updateVehicleStatusS({'message': msgString,
             'rentAvailable': rentAvailable,
             'isElite': vehicle.isElite,
             'tankType': '{}_elite'.format(vehicle.type) if vehicle.isElite else vehicle.type,
             'vehicleLevel': vehicleLevel,
             'vehicleName': '{}'.format(vehicle.shortUserName),
             'actionGroupId': roleID})

    def __inventoryUpdateCallBack(self, *args):
        self.update()

    def __applyCustomizationNewCounter(self, vehicle):
        if vehicle.isCustomizationEnabled() and not self.bootcampCtrl.isInBootcamp():
            availableItemTypes = getItemTypesAvailableForVehicle()
            counter = vehicle.getC11nItemsNoveltyCounter(self.itemsCache.items, itemTypes=availableItemTypes)
            progressiveItemsViewVisited = self.settingsCore.serverSettings.getOnceOnlyHintsSetting(OnceOnlyHints.C11N_PROGRESSION_VIEW_HINT)
            if not progressiveItemsViewVisited and isVehicleCanBeCustomized(vehicle, GUI_ITEM_TYPE.PROJECTION_DECAL):
                counter += 1
            counter += getEditableStylesExtraNotificationCounter()
        else:
            counter = 0
        self.as_setCustomizationBtnCounterS(counter)

    def __moneyUpdateCallback(self, *_):
        self._update(onlyMoneyUpdate=True)

    def __updateDevices(self, vehicle):
        stateWarning = False
        if g_currentVehicle.isPresent():
            stateWarning = vehicle.isBroken
        self.as_setWarningStateS(stateWarning)

    def __isRankedPrbActive(self):
        return False if self.prbEntity is None else bool(self.prbEntity.getModeFlags() & FUNCTIONAL_FLAG.RANKED)

    def __applyGamemodeOverrides(self, statusId, msg, msgLvl):
        return self.__applyRankedOverrides(statusId, msg, msgLvl) if self.__isRankedPrbActive() else (msg, msgLvl)

    def __applyRankedOverrides(self, statusId, msg, msgLvl):
        statusOverrideRes = R.strings.ranked_battles.currentVehicleStatus.dyn(statusId)
        if statusOverrideRes:
            msg = backport.text(statusOverrideRes())
        isRole = statusId in (Vehicle.VEHICLE_STATE.UNDAMAGED, Vehicle.VEHICLE_STATE.ROTATION_GROUP_UNLOCKED)
        if isRole and g_currentVehicle.item.actionsGroup:
            actionsGroupLabel = g_currentVehicle.item.actionsGroupLabel
            msg = text_styles.concatStylesToSingleLine(backport.text(R.strings.menu.roleExp.currentVehicleStatus()), ' ', roleActionsGroup(actionsGroupLabel), backport.text(R.strings.menu.roleExp.actionsGroup.dyn(actionsGroupLabel)()))
            msgLvl = Vehicle.VEHICLE_STATE_LEVEL.ACTIONS_GROUP
        return (msg, msgLvl)
