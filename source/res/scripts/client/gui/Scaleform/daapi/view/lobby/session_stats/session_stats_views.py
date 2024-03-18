# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/session_stats/session_stats_views.py

# Import necessary modules and dependencies
from account_helpers.settings_core.settings_constants import SESSION_STATS  # For accessing account stats settings
from constants import ARENA_BONUS_TYPE  # For accessing regular arena bonus type
from gui.Scaleform.daapi.view.lobby.session_stats.shared import (  # For using helper functions
    packLastBattleData,
    packBattleEfficiencyData,
    packTotalData,
    toIntegral,
    toNiceNumber,
    getDeltaAsData,
    getNationIcon
)
from gui.Scaleform.daapi.view.meta.SessionBattleStatsViewMeta import SessionBattleStatsViewMeta  # Base view for battle stats
from gui.Scaleform.daapi.view.meta.SessionVehicleStatsViewMeta import SessionVehicleStatsViewMeta  # Base view for vehicle stats
from gui.impl import backport  # For localization and image loading
from gui.impl.gen import R  # For localization
from gui.shared.formatters import text_styles  # For formatting text
from gui.shared.utils.requesters import REQ_CRITERIA  # For requesting items
from helpers import dependency  # For dependency injection
from skeletons.gui.shared import IItemsCache  # For accessing items cache

_VEH_LIST_LEN = 12  # Number of vehicles to display in the list

class SessionBattleStatsView(SessionBattleStatsViewMeta):
    # Dependency injection for accessing items cache
    itemsCache = dependency.descriptor(IItemsCache)

    def updateData(self):
        # Update the view with the latest data
        self.as_setDataS(self.__makeVO())

    def _populate(self):
        # Override _populate method to set initial data and subscribe to onSyncCompleted event
        super(SessionBattleStatsView, self)._populate()
        self.as_setDataS(self.__makeVO())  # Set initial data
        self.itemsCache.onSyncCompleted += self.__updateViewHandler  # Subscribe to onSyncCompleted event

    def _dispose(self):
        # Unsubscribe from onSyncCompleted event when the view is disposed
        self.itemsCache.onSyncCompleted -= self.__updateViewHandler

    def __updateViewHandler(self, *_):
        # Update the view with the latest data when onSyncCompleted event is triggered
        self.as_setDataS(self.__makeVO())

    def __makeVO(self):
        # Prepare view data based on the account stats
        data = self.itemsCache.items.sessionStats.getAccountStats(ARENA_BONUS_TYPE.REGULAR)
        parameters = SESSION_STATS.getAccountEfficiencyBlock()
        return {
            'collapseLabel': text_styles.middleTitle(backport.text(R.strings.session_stats.label.battleEfficiency())),
            'lastBattle': packLastBattleData(data),
            'total': packTotalData(data),
            'battleEfficiency': packBattleEfficiencyData(data, parameters)
        }

class SessionVehicleStatsView(SessionVehicleStatsViewMeta):
    itemsCache = dependency.descriptor(IItemsCache)

    def updateData(self):
        # Update the view with the latest data
        self.as_setDataS(self.__makeVO)

    def _populate(self):
        # Override _populate method to request vehicles stats, set initial data, and subscribe to onSyncCompleted event
        super(SessionVehicleStatsView, self)._populate()
        self.itemsCache.items.sessionStats.getVehiclesStats(ARENA_BONUS_TYPE.REGULAR, 0)
        self.as_setDataS(self.__makeVO)
        self.itemsCache.onSyncCompleted += self.__updateViewHandler

    def _dispose(self):
        # Unsubscribe from onSyncCompleted event when the view is disposed
        self.itemsCache.onSyncCompleted -= self.__updateViewHandler

    @property
    def __makeVO(self):
        # Prepare view data based on the vehicles stats
        vehIdList = self.itemsCache.items.sessionStats.getStatsVehList(ARENA_BONUS_TYPE.REGULAR)
        vehiclesDict = self.itemsCache.items.getVehicles(REQ_CRITERIA.IN_CD_LIST(vehIdList))
        vehiclesData = []
        vehiclesSortData = []

        if vehiclesDict:
            for intCD, vehicle in vehiclesDict.iteritems():
                data = self.itemsCache.items.sessionStats.getVehiclesStats(ARENA_BONUS_TYPE.REGULAR, intCD)
                vehiclesSortData.append((intCD, (data.battleCnt, vehicle.level, data.averageDamage.value)))
                vehiclesData.append({
                    'intCD': intCD,
                    'icon': vehicle.iconSmall,
                    'label': text_styles.main(vehicle.shortUserName),
                    'level': vehicle.level,
                    'nationIcon': getNationIcon(vehicle.nationID, width=155, height=31),
                    'type': vehicle.type,
                    'total': text_styles.stats(toNiceNumber(data.battleCnt)),
                    'damage': text_styles.stats(toIntegral(data.averageDamage.value)),
                    'wtr': text_styles.stats(toNiceNumber(data.wtr.value)),
                    'delta': getDeltaAsData(data.wtr.delta)
                })

        else:
            vehiclesData.append({
                'intCD': None,
                'icon': backport.image(R.images.gui.maps.icons.library.empty_veh()),
                'total': text_styles.stats(toNiceNumber(None)),
               
