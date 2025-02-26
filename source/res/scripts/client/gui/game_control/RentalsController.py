# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/game_control/RentalsController.py
from operator import itemgetter
from sys import maxint
import copy
import typing
import BigWorld
import Event
from constants import RentType, SEASON_NAME_BY_TYPE, IS_RENTALS_ENABLED
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.money import Money
from helpers import dependency
from helpers import time_utils
from skeletons.gui.game_control import IRentalsController, ISeasonsController, IEpicBattleMetaGameController
from skeletons.gui.shared import IItemsCache
from rent_common import SeasonRentDuration, calculateSeasonRentPrice
from season_common import GameSeason
RENT_TYPE_WEIGHTS = {RentType.TIME_RENT: 0,
 RentType.SEASON_CYCLE_RENT: 1,
 RentType.SEASON_RENT: 2}

class RentalsController(IRentalsController):
    itemsCache = dependency.descriptor(IItemsCache)
    seasonsController = dependency.descriptor(ISeasonsController)
    epicController = dependency.descriptor(IEpicBattleMetaGameController)

    def __init__(self):
        super(RentalsController, self).__init__()
        self.onRentChangeNotify = Event.Event()
        self.__rentNotifyTimeCallback = None
        self.__vehiclesForUpdate = []
        return

    def fini(self):
        self._stop()
        super(RentalsController, self).fini()

    def onLobbyInited(self, event):
        if self.isEnabled():
            self.itemsCache.onSyncCompleted += self.__onSyncCompleted
            self.epicController.onUpdated += self._update
            if self.__rentNotifyTimeCallback is None:
                self.__startRentTimeNotifyCallback()
        return

    def onAvatarBecomePlayer(self):
        self._stop()

    def onDisconnected(self):
        self._stop()

    def isEnabled(self):
        return IS_RENTALS_ENABLED

    def _stop(self):
        self.onRentChangeNotify.clear()
        if self.isEnabled():
            self.__clearRentTimeNotifyCallback()
            self.__vehiclesForUpdate = None
            self.itemsCache.onSyncCompleted -= self.__onSyncCompleted
            self.epicController.onUpdated -= self._update
        return

    def __onSyncCompleted(self, _, invalidItems):
        if invalidItems and GUI_ITEM_TYPE.VEHICLE not in invalidItems:
            return
        self._update()

    def _update(self, *args):
        self.__clearRentTimeNotifyCallback()
        self.__startRentTimeNotifyCallback()

    def filterRentPackages(self, rentPrices):
        filteredRentPrices = {}
        if self.isEnabled():
            for rentType, packagesToFilter in rentPrices.iteritems():
                if rentType == RentType.SEASON_RENT:
                    filteredRentPrices[rentType] = self.__filterSeasonCyclePackages(packagesToFilter, self.__seasonFilter)
                if rentType == RentType.SEASON_CYCLE_RENT:
                    filteredRentPrices[rentType] = self.__filterSeasonCyclePackages(packagesToFilter, self.__cycleFilter)
                filteredRentPrices[rentType] = copy.deepcopy(packagesToFilter)

        return filteredRentPrices

    def getRentPackagesInfo(self, rentPrices, currentRentInfo):
        seasonRent = currentRentInfo.getActiveSeasonRent()
        hasAvailableRentPackages = False
        mainRentType = None
        mainRentTypeWeight = float('-inf')
        seasonType = None
        if self.isEnabled():
            for rentType, packages in self.filterRentPackages(rentPrices).iteritems():
                if packages:
                    if rentType == RentType.TIME_RENT:
                        if mainRentType is None:
                            mainRentType = RentType.TIME_RENT
                            hasAvailableRentPackages = True
                    elif rentType == RentType.SEASON_RENT:
                        if seasonRent:
                            if seasonRent.duration == SeasonRentDuration.SEASON_CYCLE:
                                hasAvailableRentPackages = True
                        else:
                            hasAvailableRentPackages = True
                    elif rentType == RentType.SEASON_CYCLE_RENT:
                        if not seasonRent:
                            hasAvailableRentPackages = True
                    if hasAvailableRentPackages:
                        rentTypeWeight = RENT_TYPE_WEIGHTS.get(rentType, 0)
                        if rentTypeWeight > mainRentTypeWeight:
                            mainRentType = rentType
                            mainRentTypeWeight = rentTypeWeight
                            seasonType = packages.itervalues().next().get('seasonType', None)

        return (hasAvailableRentPackages, mainRentType, seasonType)

    def getRentPriceOfPackage(self, vehicle, rentType, packageID, package):
        rentPrice = package.get('cost', (0, 0))
        if rentType == RentType.SEASON_RENT:
            seasonType = package.get('seasonType', None)
            cycleRentPrice = package.get('defaultCycleCost', (0, 0))
            season = self.seasonsController.getCurrentSeason(seasonType)
            if season is not None and season.getSeasonID() == packageID:
                numCycles = len(season.getAllCycles())
                cycleOrdinalNumber = season.getCycleOrdinalNumber()
                if vehicle.isRented:
                    activeSeasonRent = vehicle.currentSeasonRent
                    if activeSeasonRent and activeSeasonRent.duration == SeasonRentDuration.SEASON_CYCLE and activeSeasonRent.seasonID == season.getCycleID() and cycleOrdinalNumber + 1 <= numCycles:
                        cycleOrdinalNumber += 1
                rentPrice = calculateSeasonRentPrice(cycleRentPrice, rentPrice, cycleOrdinalNumber - 1, numCycles)
        return Money.makeFromMoneyTuple(rentPrice)

    @staticmethod
    def getDeltaPeriod(delta):
        if delta == float('inf'):
            return time_utils.ONE_DAY
        if delta > time_utils.ONE_DAY:
            period = time_utils.ONE_DAY
        elif delta > time_utils.ONE_HOUR:
            period = time_utils.ONE_HOUR
        else:
            period = delta
        return delta % period or period

    @staticmethod
    def __filterSeasonCyclePackages(packagesToFilter, filterFunc):
        filteredPackages = {}
        for packageID, package in packagesToFilter.iteritems():
            seasonType = package.get('seasonType', None)
            if filterFunc(packageID, seasonType, package):
                filteredPackages[packageID] = package

        return filteredPackages

    def __startRentTimeNotifyCallback(self):
        if not self.itemsCache.isSynced():
            return
        self.__vehiclesForUpdate = []
        rentedVehicles = []
        for itemCD in set(self.itemsCache.items.inventory.getIventoryVehiclesCDs()).union(self.itemsCache.items.shop.getVehicleRentPrices().keys()):
            item = self.itemsCache.items.getItemByCD(itemCD)
            if item.isRented or item.isRentPromotion:
                rentedVehicles.append(item)

        notificationList = []
        for vehicle in rentedVehicles:
            delta = vehicle.rentLeftTime
            if delta > 0:
                notificationList.append((vehicle.intCD, self.getDeltaPeriod(delta), vehicle.isRentPromotion))

        nextRentNotification = maxint
        if notificationList:
            _, nextRentNotification, forceUpdate = min(notificationList, key=itemgetter(1))
            for item in notificationList:
                if item[1] == nextRentNotification or forceUpdate:
                    self.__vehiclesForUpdate.append(item[0])

            nextRentNotification = max(nextRentNotification, 0)
        for seasonType in SEASON_NAME_BY_TYPE:
            currentSeason = self.seasonsController.getCurrentSeason(seasonType)
            if currentSeason:
                now = time_utils.getCurrentLocalServerTimestamp()
                if currentSeason.hasActiveCycle(now):
                    nextCycleChange = currentSeason.getCycleEndDate()
                else:
                    nextCycleChange = currentSeason.getCycleStartDate()
                delta = int(time_utils.getTimeDeltaFromNow(time_utils.makeLocalServerTime(nextCycleChange)))
                if delta > 0:
                    nextRentNotification = min(nextRentNotification, self.getDeltaPeriod(delta)) + 1

        if not notificationList and nextRentNotification == maxint:
            return
        self.__rentNotifyTimeCallback = BigWorld.callback(nextRentNotification, self.__notifyRentTime)

    def __notifyRentTime(self):
        self.__rentNotifyTimeCallback = None
        self.onRentChangeNotify(self.__vehiclesForUpdate)
        self.__startRentTimeNotifyCallback()
        return

    def __clearRentTimeNotifyCallback(self):
        if self.__rentNotifyTimeCallback is not None:
            BigWorld.cancelCallback(self.__rentNotifyTimeCallback)
            self.__rentNotifyTimeCallback = None
        return

    def __seasonFilter(self, seasonID, seasonType, package):
        currentSeason = self.seasonsController.getCurrentSeason(seasonType)
        if currentSeason is None or currentSeason.getSeasonID() != seasonID:
            return False
        else:
            numCycles = len(currentSeason.getAllCycles())
            if not currentSeason.getCycleInfo():
                return False
            currentCycleNumber = currentSeason.getCycleOrdinalNumber()
            if currentCycleNumber >= numCycles:
                return False
            cyclesWithinSeasonRentIsActive = package.get('cycles', [])
            currentCycleID = self.seasonsController.getCurrentCycleID(seasonType)
            return currentCycleID in cyclesWithinSeasonRentIsActive

    def __cycleFilter(self, cycleID, seasonType, _):
        return self.seasonsController.isSeasonCycleActive(cycleID, seasonType)
