# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/ResearchPanel.py


import typing
from bootcamp.Bootcamp import g_bootcamp
from CurrentVehicle import g_currentVehicle
from gui.veh_post_progression.helpers import needToShowCounter
from constants import IGR_TYPE
from debug_utils import LOG_ERROR
from gui import makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import resolveStateTooltip
from gui.Scaleform.daapi.view.meta.ResearchPanelMeta import ResearchPanelMeta
from gui.Scaleform.locale.MENU import MENU
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.shared import event_dispatcher as shared_events
from gui.shared.formatters import text_styles
from gui.shared.formatters.time_formatters import getTimeLeftStr
from gui.shared.tutorial_helper import getTutorialGlobalStorage
from gui.veh_post_progression.models.ext_money import ExtendedMoney
from helpers import i18n, dependency
from nation_change.nation_change_helpers import iterVehiclesWithNationGroupInOrder
from skeletons.gui.game_control import IVehicleComparisonBasket, IIGRController
from skeletons.gui.shared import IItemsCache
from tutorial.control.context import GLOBAL_FLAG
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle


class ResearchPanel(ResearchPanelMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)
    igrCtrl = dependency.descriptor(IIGRController)

    def __init__(self):
        super(ResearchPanel, self).__init__()
        self.__isNavigationEnabled = True

    def _populate(self):
        super(ResearchPanel, self)._populate()
        g_clientUpdateManager.addCallbacks({'stats.vehTypeXP': self.onVehicleTypeXPChanged,
         'stats.eliteVehicles': self.onVehicleBecomeElite})
        self.onCurrentVehicleChanged()
        self.comparisonBasket.onChange += self.__onCompareBasketChanged
        self.comparisonBasket.onSwitchChange += self.onCurrentVehicleChanged


    def _dispose(self):
        super(ResearchPanel, self)._dispose()
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.comparisonBasket.onChange -= self.__onCompareBasketChanged
        self.comparisonBasket.onSwitchChange -= self.onCurrentVehicleChanged


    def setNavigationEnabled(self, isEnabled):
        if self.__isNavigationEnabled != isEnabled:
            self.as_setNavigationEnabledS(isEnabled)
            self.__isNavigationEnabled = isEnabled


    def goToResearch(self):
        if g_currentVehicle.isPresent() and self.__isNavigationEnabled:
            shared_events.showResearchView(g_currentVehicle.item.intCD)
        else:
            LOG_ERROR('Current vehicle is not preset or navigation is disabled')


    def goToPostProgression(self):
        shared_events.showVehPostProgressionView(g_currentVehicle.item.intCD)


    def addVehToCompare(self):
        if g_currentVehicle.isPresent() and not isBattleRoyale(g_currentVehicle.item.tags):
            vehCD = g_currentVehicle.item.intCD
            self.comparisonBasket.addVehicle(vehCD)


    def onCurrentVehicleChanged(self):
        if g_currentVehicle.isPresent():
            xps = self.itemsCache.items.stats.vehiclesXPs
            vehicle = g_currentVehicle.item
            xp = xps.get(vehicle.intCD, 0)
            self.as_updateCurrentVehicleS({'earnedXP': xp,
             'isElite': vehicle.isElite,
             'vehCompareData': self.__get
