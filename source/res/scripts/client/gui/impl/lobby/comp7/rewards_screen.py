# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/impl/lobby/comp7/rewards_screen.py
from collections import namedtuple
import typing
from shared_utils import first, findFirst
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer
from frameworks.wulf.view.array import fillIntsArray, fillViewModelsArray
from gui.impl.backport import BackportTooltipWindow
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.comp7.rewards_screen_model import Type, Rank, RewardsScreenModel
from gui.impl.lobby.comp7 import comp7_shared, comp7_qualification_helpers
from gui.impl.lobby.comp7.comp7_bonus_packer import packRanksRewardsQuestBonuses, packTokensRewardsQuestBonuses, packQualificationRewardsQuestBonuses
from gui.impl.lobby.comp7.comp7_quest_helpers import parseComp7RanksQuestID, parseComp7TokensQuestID, parseComp7PeriodicQuestID
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from helpers import dependency
from skeletons.gui.game_control import IComp7Controller
from skeletons.gui.lobby_context import ILobbyContext
if typing.TYPE_CHECKING:
    from comp7_ranks_common import Comp7Division
    from frameworks.wulf.view.view_event import ViewEvent
    from gui.server_events.event_items import TokenQuest
_MAX_MAIN_REWARDS_COUNT = 4
_MAIN_REWARDS = ('styleProgress', 'dossier_badge', 'dogTagComponents')
_BonusData = namedtuple('_BonusData', ('bonus', 'tooltip'))

class _BaseRewardsView(ViewImpl):
    __slots__ = ('_bonusData',)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(R.views.lobby.comp7.RewardsScreen())
        settings.model = RewardsScreenModel()
        settings.args = args
        settings.kwargs = kwargs
        super(_BaseRewardsView, self).__init__(settings)
        self._bonusData = []

    @property
    def viewModel(self):
        return super(_BaseRewardsView, self).getViewModel()

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipId = event.getArgument('tooltipId')
            if tooltipId is not None:
                bonusData = self._bonusData[int(tooltipId)]
                window = BackportTooltipWindow(bonusData.tooltip, self.getParentWindow())
                window.load()
                return window
        return super(_BaseRewardsView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.lobby.tooltips.AdditionalRewardsTooltip():
            showCount = int(event.getArgument('showCount'))
            showCount += self._getMainRewardsCount()
            bonuses = [ d.bonus for d in self._bonusData[showCount:] ]
            return AdditionalRewardsTooltip(bonuses)
        else:
            return None

    def _initialize(self, *args, **kwargs):
        super(_BaseRewardsView, self)._initialize(*args, **kwargs)
        self._addListeners()

    def _finalize(self):
        self._removeListeners()
        self._bonusData = None
        super(_BaseRewardsView, self)._finalize()
        return

    def _onLoading(self, quests, *args, **kwargs):
        super(_BaseRewardsView, self)._onLoading(*args, **kwargs)
        self._bonusData = []
        bonuses, tooltips = self._packQuestBonuses(quests)
        for idx, (packedBonus, tooltipData) in enumerate(zip(bonuses, tooltips)):
            packedBonus.setTooltipId(str(idx))
            self._bonusData.append(_BonusData(packedBonus, tooltipData))

        self._setModelData()

    def _setModelData(self):
        raise NotImplementedError

    def _packQuestBonuses(self, quests):
        raise NotImplementedError

    def _setRewards(self, model):
        mainRewardsCount = self._getMainRewardsCount()
        bonuses = [ d.bonus for d in self._bonusData ]
        fillViewModelsArray(bonuses[:mainRewardsCount], model.getMainRewards())
        fillViewModelsArray(bonuses[mainRewardsCount:], model.getAdditionalRewards())

    def _getMainRewardsCount(self):
        bonuses = [ d.bonus for d in self._bonusData ]
        mainRewards = [ bonusModel for bonusModel in bonuses if bonusModel.getName() in _MAIN_REWARDS ]
        return min(len(mainRewards), _MAX_MAIN_REWARDS_COUNT)

    def _addListeners(self):
        self.viewModel.onClose += self._onClose

    def _removeListeners(self):
        self.viewModel.onClose -= self._onClose

    def _onClose(self):
        self.destroyWindow()


class RanksRewardsView(_BaseRewardsView):
    __slots__ = ('__division', '__periodicQuests')
    __lobbyCtx = dependency.descriptor(ILobbyContext)

    def __init__(self, *args, **kwargs):
        super(RanksRewardsView, self).__init__(*args, **kwargs)
        quest = first(kwargs['quests'])
        self.__division = parseComp7RanksQuestID(quest.getID())
        self.__periodicQuests = kwargs.get('periodicQuests', [])

    def _packQuestBonuses(self, quests):
        periodicQuest = findFirst(lambda q: parseComp7PeriodicQuestID(q.getID()) == self.__division, self.__periodicQuests)
        return packRanksRewardsQuestBonuses(quest=first(quests), periodicQuest=periodicQuest)

    def _setModelData(self):
        with self.viewModel.transaction() as vm:
            rankValue = comp7_shared.getRankEnumValue(self.__division)
            divisionValue = comp7_shared.getDivisionEnumValue(self.__division)
            vm.setType(self._getType())
            vm.setRank(rankValue)
            vm.setDivision(divisionValue)
            vm.setHasRankInactivity(comp7_shared.hasRankInactivity(self.__division.rank))
            self._setRewards(vm)

    def _onClose(self):
        if self.viewModel.getType() == Type.RANK:
            self.viewModel.setType(Type.RANKREWARDS)
        else:
            self.destroyWindow()

    def _getType(self):
        ranksConfig = self.__lobbyCtx.getServerSettings().comp7RanksConfig
        return Type.RANK if len(ranksConfig.divisionsByRank[self.__division.rank]) == self.__division.index else Type.DIVISION


class TokensRewardsView(_BaseRewardsView):
    __slots__ = ('__tokensCount',)

    def __init__(self, *args, **kwargs):
        super(TokensRewardsView, self).__init__(*args, **kwargs)
        quest = first(kwargs['quests'])
        self.__tokensCount = parseComp7TokensQuestID(quest.getID())

    def _packQuestBonuses(self, quests):
        return packTokensRewardsQuestBonuses(quest=first(quests))

    def _setModelData(self):
        with self.viewModel.transaction() as vm:
            vm.setType(Type.TOKENSREWARDS)
            vm.setTokensCount(self.__tokensCount)
            self._setRewards(vm)

    def _getMainRewardsCount(self):
        return _MAX_MAIN_REWARDS_COUNT


class QualificationRewardsView(_BaseRewardsView):
    __slots__ = ('__divisions',)
    __comp7Controller = dependency.descriptor(IComp7Controller)

    def __init__(self, *args, **kwargs):
        super(QualificationRewardsView, self).__init__(*args, **kwargs)
        self.__divisions = self.__getDivisions(kwargs['quests'])

    def _onClose(self):
        if self.viewModel.getType() == Type.QUALIFICATIONRANK:
            self.viewModel.setType(Type.QUALIFICATIONREWARDS)
        else:
            self.destroyWindow()

    def _setModelData(self):
        with self.viewModel.transaction() as vm:
            maxDivision = first(self.__divisions)
            rankEnumValues = self.__getRanks(self.__divisions)
            maxRankEnumValue = first(rankEnumValues)
            vm.setType(Type.QUALIFICATIONRANK)
            vm.setRank(maxRankEnumValue)
            vm.setDivision(comp7_shared.getDivisionEnumValue(maxDivision))
            vm.setHasRankInactivity(comp7_shared.hasRankInactivity(maxDivision.rank))
            comp7_qualification_helpers.setQualificationBattles(vm.getQualificationBattleList())
            fillIntsArray(rankEnumValues, vm.getRankList())
            self._setRewards(vm)

    def _packQuestBonuses(self, quests):
        return packQualificationRewardsQuestBonuses(quests=quests)

    def __getRanks(self, divisions):
        uniqueRanks = {comp7_shared.getRankEnumValue(division) for division in divisions}
        return sorted(list(uniqueRanks))

    def __getDivisions(self, quests):
        divisions = [ parseComp7RanksQuestID(quest.getID()) for quest in quests ]
        return sorted(divisions, key=lambda d: d.dvsnID)


class RanksRewardsScreenWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, quest, periodicQuests, parent=None):
        super(RanksRewardsScreenWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=RanksRewardsView(quests=(quest,), periodicQuests=periodicQuests), layer=WindowLayer.TOP_WINDOW, parent=parent)


class TokensRewardsScreenWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, quest, parent=None):
        super(TokensRewardsScreenWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=TokensRewardsView(quests=(quest,)), layer=WindowLayer.TOP_WINDOW, parent=parent)


class QualificationRewardsScreenWindow(LobbyNotificationWindow):
    __slots__ = ()

    def __init__(self, quests, parent=None):
        super(QualificationRewardsScreenWindow, self).__init__(wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=QualificationRewardsView(quests=quests), layer=WindowLayer.TOP_WINDOW, parent=parent)
