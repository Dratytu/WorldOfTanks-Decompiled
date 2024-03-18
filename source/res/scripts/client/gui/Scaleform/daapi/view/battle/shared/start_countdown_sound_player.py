# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/start_countdown_sound_player.py

import logging
import WWISE
from helpers import dependency
import BattleReplay
from gui.battle_control.battle_constants import COUNTDOWN_STATE
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from gui.battle_control.view_components import IViewComponentsCtrlListener
from skeletons.gui.battle_session import IBattleSessionProvider

# Initialize a logger for this module
_logger = logging.getLogger(__name__)

# Define a constant for the RTPC name
_RTPC = 'RTPC_ext_battle_countdown_timer'

class StartCountdownSoundPlayer(IAbstractPeriodView, IViewComponentsCtrlListener):
    """
    A class that plays a countdown sound during the battle countdown.
    """

    def __init__(self):
        """
        Initialize the StartCountdownSoundPlayer.
        """
        super(StartCountdownSoundPlayer, self).__init__()
        # Get the sound ID for the countdown timer from the arena visitor type
        self.__soundID = dependency.instance(IBattleSessionProvider).arenaVisitor.type.getCountdownTimerSound()
        # Log a warning if the sound ID is not defined
        if not self.__soundID:
            _logger.warning('Countdown sound for this game mode is not defined! ' + 'Please define one ' + 'otherwise remove this player from the list in the corresponded page.py')

    def setCountdown(self, state, timeLeft):
        """
        Called by the battle controller to set the countdown state and time left.

        :param state: The countdown state (e.g. COUNTDOWN_STATE.START)
        :param timeLeft: The time left in the countdown
        """
        if state == COUNTDOWN_STATE.START:
            self.__updateSound(timeLeft)

    def __updateSound(self, timeLeft):
        """
        Update the countdown sound based on the time left.

        :param timeLeft: The time left in the countdown
        """
        if self.__checkNotReplay():
            self.__playSound(timeLeft)

    def __checkNotReplay(self):
        """
        Check if the current battle is not a replay.

        :return: True if the battle is not a replay, False otherwise
        """
        replay = BattleReplay.g_replayCtrl
        return not replay
