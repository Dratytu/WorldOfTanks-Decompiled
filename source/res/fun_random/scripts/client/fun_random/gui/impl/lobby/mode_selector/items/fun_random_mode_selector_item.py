# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/mode_selector/items/fun_random_mode_selector_item.py

# Import necessary modules and classes
import typing
import math_utils
from fun_random.gui.feature.fun_constants import FunSubModesState
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunProgressionWatcher, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression, hasAnySubMode, hasMultipleSubModes, avoidSubModesStates
from fun_random.gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_fun_random_model import ModeSelectorFunRandomModel
from fun_random.gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_fun_random_widget_model import SimpleFunProgressionStatus
from fun_random.gui.impl.lobby.common.fun_view_helpers import defineProgressionStatus
from fun_random.gui.impl.lobby.common.fun_view_helpers import getFormattedTimeLeft
from fun_random.gui.impl.lobby.mode_selector.items.fun_random_mode_selector_helpers import createSelectorHelper
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_types import ModeSelectorCardTypes
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_fun_random_widget_model import ModeSelectorFunRandomWidgetModel
from gui.impl.gen.view_models.views.lobby.mode_selector.tooltips.mode_selector_tooltips_constants import ModeSelectorTooltipsConstants
from gui.impl.lobby.mode_selector.items.base_item import ModeSelectorLegacyItem
from gui.impl.lobby.mode_selector.items.items_constants import ModeSelectorRewardID
from helpers import time_utils

# Typing imports
if typing.TYPE_CHECKING:
    from frameworks.wulf import Array
    from fun_random.gui.feature.models.common import FunSubModesStatus
    from fun_random.gui.impl.lobby.mode_selector.items.fun_random_mode_selector_helpers import IModeSelectorHelper

# Define a constant dictionary for progression status mapping
_PROGRESSION_STATUS_MAP = {
    FunRandomProgressionStatus.ACTIVE_RESETTABLE: SimpleFunProgressionStatus.ACTIVE,
    FunRandomProgressionStatus.ACTIVE_FINAL: SimpleFunProgressionStatus.ACTIVE,
    FunRandomProgressionStatus.COMPLETED_RESETTABLE: SimpleFunProgressionStatus.RESETTABLE,
    FunRandomProgressionStatus.COMPLETED_FINAL: SimpleFunProgressionStatus.DISABLED,
    FunRandomProgressionStatus.DISABLED: SimpleFunProgressionStatus.DISABLED
}

class FunRandomSelectorItem(ModeSelectorLegacyItem, FunAssetPacksMixin, FunSubModesWatcher, FunProgressionWatcher):
    # Class attributes
    __slots__ = ('__subModesHelper',)
    _CARD_VISUAL_TYPE = ModeSelectorCardTypes.FUN_RANDOM
    _VIEW_MODEL = ModeSelectorFunRandomModel

    def __init__(self, oldSelectorItem):
        # Initialize the superclass and set up instance variables
        super(FunRandomSelectorItem, self).__init__(oldSelectorItem)
        self.__subModesHelper = None

    @property
    def viewModel(self):
        # Property to access the view model
        return self._viewModel

    # Methods with decorators for handling specific conditions
    @hasMultipleSubModes(defReturn=True)
    def checkHeaderNavigation(self):
        # Method to check header navigation
        return False

    def setDisabledProgression(self):
        # Method to set disabled progression
        with self.viewModel.transaction() as model:
            model.widget.setStatus(SimpleFunProgressionStatus.DISABLED)
            self.__invalidateRewards(model.getRewardList())

    def handleInfoPageClick(self):
        # Method to handle info page click
        self.showSubModesInfoPage()

    @hasMultipleSubModes(defReturn=True)
    def _isInfoIconVisible(self):
        # Method to check if info icon is visible
        return bool(self._funRandomCtrl.getSettings().infoPageUrl)

    def _isNewLabelVisible(self):
        # Method to check if new label is visible
        isEntryPointAvailable = self._funRandomCtrl.subModesInfo.isEntryPointAvailable()
        return super(FunRandomSelectorItem, self)._isNewLabelVisible() and isEntryPointAvailable

    def _getModeStringsRoot(self):
        # Method to get mode strings root
        return self.getModeLocalsResRoot().mode_selector

    def _onInitializing(self):
        # Method called when the item is initializing
        super(FunRandomSelectorItem, self)._onInitializing()
        self.__reloadModeHelper()
        self.__addListeners()
        self.__invalidateAll()

    def _onDisposing(self):
        # Method called when the item is disposing
        self.__removeListeners()
        self.__subModesHelper.clear()
        super(FunRandomSelectorItem, self)._onDisposing()

    # Helper methods
    def __getStatusText(self, status):
        # Method to get status text
        return backport.text(R.strings.fun_random.modeSelector.notStarted()) if not self._bootcamp.isInBootcamp() and status.state in FunSubModesState.BEFORE_STATES else ''

    def __getTimeLeftText(self, status):
        # Method to get time left text
        return getFormattedTimeLeft(time_utils.getTimeDeltaFromNowInLocal(status.rightBorder)) if status
