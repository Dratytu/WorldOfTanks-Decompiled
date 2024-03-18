# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/lobby/feature/armory_yard_progress_presenter.py

# Import necessary modules and dependencies.
import BigWorld
from armory_yard.gui.shared.gui_items.items_actions import COLLECT_REWARDS
from armory_yard_constants import State
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.gui_items.items_actions import factory
from gui.shared.utils import decorators
from shared_utils import first
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_main_view_model import ArmoryYardMainViewModel, AnimationStatus, ArmoryYardLevelModel, RewardStatus
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_main_view_model import EscSource
from armory_yard.gui.shared.bonus_packers import getArmoryYardBuyViewPacker, packVehicleModel
from armory_yard.gui.shared.bonuses_sorter import bonusesSortKeyFunc

# Dependency injection for easier testing and mocking.
from Event import SuspendableEventSubscriber
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import LobbySimpleEvent, ArmoryYardEvent
from gui.shared.missions.packers.bonus import BACKPORT_TOOLTIP_CONTENT_ID
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents
from gui.impl.backport import createTooltipData
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.server_events.bonuses import getNonQuestBonuses, mergeBonuses, splitBonuses
from helpers import dependency
from skeletons.gui.game_control import IArmoryYardController
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.shared import IItemsCache
from skeletons.gui.shared.utils import IHangarSpace

# Define a class `_InternalState` to manage the internal state of the progress presenter.
class _InternalState(object):
    __NONE = -1
    __REPLAY_ANIMATION = 1
    __BUILDING = 2

    def __init__(self):
        self.__status = self.__NONE

    def reset(self):
        self.__status = self.__NONE

    def setReplayAnimation(self):
        self.__status = self.__REPLAY_ANIMATION

    def setBuilding(self):
        self.__status = self.__BUILDING

    @property
    def isReplayAnimation(self):
        return self.__status == self.__REPLAY_ANIMATION

    @property
    def isBuilding(self):
        return self.__status == self.__BUILDING

    @property
    def isAnimation(self):
        return self.isBuilding or self.isReplayAnimation


# Define a class `_ProgressionTabPresenter` to handle the progression tab presentation logic.
class _ProgressionTabPresenter(object):
    __armoryYardCtrl = dependency.descriptor(IArmoryYardController)
    __settingsCore = dependency.descriptor(ISettingsCore)
    __itemsCache = dependency.descriptor(IItemsCache)
    __hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self, viewModel, stageManager, closeCB):
        self.__viewModel = viewModel
        self.__tooltipData = {}
        self.__stageManager = stageManager
        self._isActiveCollectRewardsBtn = False
        self.__playAnimationLastID = None
        self.__closeCB = closeCB
        self.__eventsSubscriber = SuspendableEventSubscriber()
        self.__parent = None
        self.__state = _InternalState()

    # Implement methods for initialization, finalization, loading, and unloading the view.
    def init(self, parent):
        self.__parent = parent
        self.__eventsSubscriber.subscribeToEvents(
            (self.__armoryYardCtrl.serverSettings.onUpdated, self.__onServerSettingsUpdated),
            (self.__stageManager.onStartStage, self.__onStartStage),
            (self.__stageManager.onFinishStage, self.__onFinishStage),
            (self.__viewModel.onCollectReward, self.__onCollectReward),
            (self.__viewModel.onPlayAnimation, self.__onPlayAnimation),
            (self.__armoryYardCtrl.onProgressUpdated, self.__onProgressUpdate),
            (self.__armoryYardCtrl.onCollectFinalReward, self._checkAndShowFinalRewardWindow),
            (self.__viewModel.onAboutEvent, self.__onAboutEvent),
            (self.__viewModel.onClose, self.__closeView),
            (self.__viewModel.onSkipAnimation, self.__onSkipAnimation),
            (self.__viewModel.onMoveSpace, self.__onMoveSpace),
            (self.__viewModel.onBuyTokens
