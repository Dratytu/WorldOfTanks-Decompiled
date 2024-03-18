# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/util/fun_mixins.py

# Import necessary modules and libraries
import logging
import typing
from adisp import adisp_async, adisp_process
from fun_random_common.fun_constants import UNKNOWN_EVENT_ID
from fun_random.gui.fun_gui_constants import SELECTOR_BATTLE_TYPES
from fun_random.gui.feature.util.fun_helpers import notifyCaller
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression, hasAnySubMode, hasSingleSubMode, hasSpecifiedSubMode
from fun_random.gui.shared.events import FunEventType, FunEventScope
from fun_random.gui.shared.event_dispatcher import showFunRandomInfoPage, showFunRandomProgressionWindow, showFunRandomModeSubSelectorWindow
from gui.impl import backport
from gui.shared.utils import SelectorBattleTypesUtils as selectorUtils
from helpers import dependency
from shared_utils import first
from skeletons.gui.game_control import IFunRandomController

# If typing module is available, use its features for type checking
if typing.TYPE_CHECKING:
    from fun_random.gui.feature.models.common import FunSubModesStatus
    from fun_random.gui.feature.models.progressions import FunProgression
    from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode
    from skeletons.gui.battle_session import IClientArenaVisitor

# Initialize the logger for this module
_logger = logging.getLogger(__name__)

# Define FunAssetPacksMixin class
class FunAssetPacksMixin(object):
    """
    A mixin class that provides methods for accessing fun random mode assets.
    """
    
    # Dependency injection for IFunRandomController
    _funRandomCtrl = dependency.descriptor(IFunRandomController)

    @classmethod
    def getModeAssetsPointer(cls):
        """
        Return the assets pointer for the fun random mode.
        """
        return cls._funRandomCtrl.getAssetsPointer()

    @classmethod
    def getModeIconsResRoot(cls):
        """
        Return the icons resource root for the fun random mode.
        """
        return cls._funRandomCtrl.getIconsResRoot()

    @classmethod
    def getModeLocalsResRoot(cls):
        """
        Return the locals resource root for the fun random mode.
        """
        return cls._funRandomCtrl.getLocalsResRoot()

    @classmethod
    def getModeNameKwargs(cls):
        """
        Return a dictionary with the mode name keyword argument for the fun random mode.
        """
        return {'modeName': cls.getModeUserName()}

    @classmethod
    def getModeUserName(cls):
        """
        Return the user-friendly name of the fun random mode.
        """
        return backport.text(cls.getModeLocalsResRoot().userName())

    @classmethod
    def getModeDetailedUserName(cls, **kwargs):
        """
        Return the detailed user-friendly name of the fun random mode with optional keyword arguments.
        """
        return backport.text(cls.getModeLocalsResRoot().detailedUserName(), modeName=cls.getModeUserName(), **kwargs)

    @classmethod
    def getPrebattleConditionIcon(cls):
        """
        Return the prebattle condition icon for the fun random mode.
        """
        return backport.image(cls.getModeIconsResRoot().battle_type.c_32x32.fun_random())

# Define FunProgressionWatcher class
class FunProgressionWatcher(object):
    """
    A class that provides methods for watching fun random progression events.
    """
    
    # Dependency injection for IFunRandomController
    _funRandomCtrl = dependency.descriptor(IFunRandomController)

    @classmethod
    @hasActiveProgression()
    def showActiveProgressionPage(cls):
        """
        Show the active progression page for the fun random mode.
        """
        showFunRandomProgressionWindow()

    @classmethod
    def getActiveProgression(cls):
        """
        Return the active progression for the fun random mode.
        """
        return cls._funRandomCtrl.progressions.getActiveProgression()

    def startProgressionListening(self, updateMethod, tickMethod=None):
        """
        Start listening for progression updates and ticks with the given methods.
        """
        self._funRandomCtrl.subscription.addListener(FunEventType.PROGRESSION_UPDATE, updateMethod)
        if tickMethod is not None:
            self._funRandomCtrl.subscription.addListener(FunEventType.PROGRESSION_TICK, tickMethod)
        return

    def stopProgressionListening(self, updateMethod, tickMethod=None):
        """
        Stop listening for progression updates and ticks with the given methods.
        """
        self._funRandomCtrl.subscription.removeListener(FunEventType.PROGRESSION_UPDATE, updateMethod)
        if tickMethod is not None:
            self._funRandomCtrl.subscription.removeListener(FunEventType.PROGRESSION_TICK, tickMethod)
        return

# Define FunSubModesWatcher class
class FunSubModesWatcher(object):
    """
    A class that provides methods for watching fun random sub-mode events.
    """
    
    # Dependency injection for IFunRandomController
    _funRandomCtrl = dependency.descriptor(IFunRandomController)

    @classmethod
    def getBattleSubMode(cls, arenaVisitor=None):
        """
        Return the battle sub-mode for the fun random mode.
        """
        return cls._funRandomCtrl.subModesHolder.getBattleSubMode(arenaVisitor)

    @classmethod
    def getSubModes(cls, subModesIDs=None, isOrdered=False):
        """
        Return the sub-modes for
