# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/battle_pass/battle_pass_package.py

# Import necessary modules
from collections import OrderedDict
import typing
from battle_pass_common import BattlePassConsts
from gui.battle_pass.battle_pass_award import BattlePassAwardsManager
from gui.battle_pass.battle_pass_constants import MIN_LEVEL
from gui.battle_pass.battle_pass_helpers import chaptersIDsComparator
from helpers import dependency
from helpers.dependency import replace_none_kwargs
from skeletons.gui.game_control import IBattlePassController
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache

# Define the BattlePassPackage class
class BattlePassPackage(object):
    # Define class variables
    __slots__ = ('__seasonID', '__chapterID')
    __eventsCache = dependency.descriptor(IEventsCache)
    __itemsCache = dependency.descriptor(IItemsCache)
    __battlePass = dependency.descriptor(IBattlePassController)
    __TOP_PRIORITY_REWARDS_COUNT = 7

    # Initialize the class
    def __init__(self, chapterID):
        # Set the season ID and chapter ID
        self.__seasonID = self.__battlePass.getSeasonID()
        self.__chapterID = chapterID

    # Define methods for getting the price, levels count, current level, top priority rewards, and other information related to the battle pass chapter
    def getPrice(self):
        return self.__getPriceBP(self.__battlePass.getBattlePassCost(self.__chapterID))

    def getCompoundPrice(self):
        return self.__battlePass.getBattlePassCost(self.__chapterID)

    def getLevelsCount(self):
        pass

    def getCurrentLevel(self):
        return self.__battlePass.getLevelInChapter(chapterID=self.__chapterID)

    def getTopPriorityAwards(self):
        maxLevel = self.__battlePass.getMaxLevelInChapter(chapterId=self.__chapterID)
        bonuses = []
        if self.hasBattlePass():
            bonuses.extend(self.__battlePass.getPackedAwardsInterval(self.__chapterID, MIN_LEVEL, maxLevel, awardType=BattlePassConsts.REWARD_PAID))
        bonuses = BattlePassAwardsManager.uniteTokenBonuses(bonuses)
        return BattlePassAwardsManager.sortBonuses(bonuses)[:self.__TOP_PRIORITY_REWARDS_COUNT]

    # Define other methods for getting information related to the battle pass chapter
    def getNowAwards(self):
        fromLevel = 1
        curLevel = self.getCurrentLevel()
        bonuses = []
        if self.hasBattlePass():
            bonuses.extend(self.__battlePass.getPackedAwardsInterval(self.__chapterID, fromLevel, curLevel, awardType=BattlePassConsts.REWARD_PAID))
        bonuses = BattlePassAwardsManager.uniteTokenBonuses(bonuses)
        return BattlePassAwardsManager.sortBonuses(bonuses)

    def getFutureAwards(self):
        bonuses = []
        if self.hasBattlePass():
            fromLevel = self.getCurrentLevel() + 1
            toLevel = self._getMaxLevel()
            bonuses.extend(self.__battlePass.getPackedAwardsInterval(self.__chapterID, fromLevel, toLevel, awardType=BattlePassConsts.REWARD_PAID))
        bonuses = BattlePassAwardsManager.uniteTokenBonuses(bonuses)
        return BattlePassAwardsManager.sortBonuses(bonuses)

    def getSeasonID(self):
        return self.__seasonID

    def isDynamic(self):
        return False

    def isVisible(self):
        return True

    def isLocked(self):
        return False

    def hasBattlePass(self):
        return True

    def setLevels(self, value):
        pass

    def getChapterID(self):
        return self.__chapterID

    def getChapterState(self):
        return self.__battlePass.getChapterState(chapterID=self.__chapterID)

    def isBought(self):
        return self.__battlePass.isBought(chapterID=self.__chapterID)

    def isExtra(self):
        return self.__battlePass.isExtraChapter(chapterID=self.__chapterID)

    def getExpireTime(self):
        return self.__battlePass.getChapterExpiration(self.__chapterID)

    def _getMaxLevel(self):
        return self.__battlePass.getMaxLevelInChapter(self.__chapterID)

    def __getPriceBP(self, battlePassCost):
        return next(next(battlePassCost.itervalues()).itervalues()) if self.hasBattlePass() else 0

# Define the PackageAnyLevels class
class PackageAnyLevels(BattlePassPackage):
    __slots__ = ('__dynamicLevelsCount',)

