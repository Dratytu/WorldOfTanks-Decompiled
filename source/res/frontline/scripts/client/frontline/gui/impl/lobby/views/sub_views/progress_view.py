# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: frontline/scripts/client/frontline/gui/impl/lobby/views/sub_views/progress_view.py

# Import necessary helpers and modules
from helpers import dependency
from frameworks.wulf import ViewFlags, ViewSettings
from frontline.gui.frontline_bonus_packers import packBonusModelAndTooltipData
from frontline.gui.frontline_helpers import geFrontlineState
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineState
from frontline.gui.impl.gen.view_models.views.lobby.views.progress_view_model import ProgressViewModel
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyVehiclesUrl
from gui.battle_pass.battle_pass_decorators import createBackportTooltipDecorator, createTooltipContentDecorator
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.shared.event_dispatcher import showShop, closeFrontlineContainerWindow
from skeletons.gui.game_control import IEpicBattleMetaGameController
from uilogging.epic_battle.constants import EpicBattleLogKeys, EpicBattleLogActions, EpicBattleLogButtons
from uilogging.epic_battle.loggers import EpicBattleLogger

# Define the ProgressView class, which inherits from ViewImpl
class ProgressView(ViewImpl):
    # Define a dependency for the IEpicBattleMetaGameController
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)

    # Define additional slots for the class
    __slots__ = ('__tooltipItems', '__frontlineLevel', '__frontlineProgress', '__maxLevel', '__uiEpicBattleLogger')

    # Initialize the ProgressView class with a layoutID and optional kwargs
    def __init__(self, layoutID=R.views.frontline.lobby.ProgressView(), **kwargs):
        # Create ViewSettings with the given layoutID, ViewFlags, and ProgressViewModel
        settings = ViewSettings(layoutID, ViewFlags.LOBBY_TOP_SUB_VIEW, ProgressViewModel())
        settings.kwargs = kwargs

        # Initialize instance variables
        self.__tooltipItems = {}
        self.__frontlineLevel, self.__frontlineProgress = self.__epicController.getPlayerLevelInfo()
        self.__maxLevel = self.__epicController.getMaxPlayerLevel()
        self.__uiEpicBattleLogger = EpicBattleLogger()

        # Initialize the superclass with the created settings
        super(ProgressView, self).__init__(settings)

    # Implement the getTooltipData method
    def getTooltipData(self, event):
        tooltipId = event.getArgument('tooltipId')
        return self.__tooltipItems.get(tooltipId)

    # Implement the createToolTip method with a backport tooltip decorator
    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(ProgressView, self).createToolTip(event)

    # Implement the createToolTipContent method with a tooltip content decorator
    @createTooltipContentDecorator()
    def createToolTipContent(self, event, contentID):
        return None

    # Implement the viewModel property to return the viewModel
    @property
    def viewModel(self):
        return super(ProgressView, self).getViewModel()

    # Implement the _onLoading method
    def _onLoading(self, *args, **kwargs):
        super(ProgressView, self)._onLoading(*args, **kwargs)
        self._fillModel()

    # Implement the _fillModel method
    def _fillModel(self):
        # Perform model-filling operations within a transaction
        with self.viewModel.transaction() as tx:
            nextLevelExp = self.__epicController.getPointsProgressForLevel(self.__frontlineLevel)
            tx.setLevel(self.__frontlineLevel)
            tx.setIsMaxLevel(self.__frontlineLevel == self.__maxLevel)
            tx.setNeededPoints(nextLevelExp)
            tx.setCurrentPoints(self.__frontlineProgress)
            self._updateFrontlineState(tx)

    # Implement the _updateFrontlineState method
    def _updateFrontlineState(self, model):
        state, nextStateDate, secondsToState = geFrontlineState()
        model.setPendingDate(int(nextStateDate))
        model.setCountdownSeconds(secondsToState)
        model.setFrontlineState(state.value)
        isActive = state is FrontlineState.ACTIVE or state is FrontlineState.FROZEN
        model.setIsShopBannerVisible(isActive and self.__epicController.hasVehiclesToRent())
        if isActive:
            bonuses = self.__epicController.getLevelRewards(self.__frontlineLevel + 1)
            rewards = model.getRewards()
            packBonusModelAndTooltipData(bonuses, rewards, self.__tooltipItems)

    # Implement the _getEvents method
    def _getEvents(self):
        return (
            (self.viewModel.onShopClick, self.__onShopClick),
            (self.__epicController.onUpdated, self.__onEpicUpdated),
            (self.__epicController.onEventEnded, self.__onEventEnded)
        )

    # Implement the __onShopClick method
    def __onShopClick(self):
        self.__uiEpicBattleLogger.log(EpicBattleLogActions.CLICK.value, item=EpicBattleLogButtons.SHOP.value, parentScreen=EpicBattleLogKeys.PROGRESS_VIEW.value)
        showShop(getBuyVehiclesUrl())
        closeFrontlineContainerWindow()

    # Implement the __onEventEnded method
    def __onEventEnded(self):
        self.__frontlineLevel, self.__frontlineProgress = self.__epicController.getPlayerLevelInfo()
        self._fillModel()

    # Implement the __onEpicUpdated method
    def __onE
