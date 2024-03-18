# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/battle/bc_finish_sound_player.py

# Import necessary modules
import SoundGroups
from PlayerEvents import g_playerEvents
from gui.Scaleform.daapi.view.battle.shared.finish_sound_player import FinishSoundPlayer
from gui.battle_control.view_components import IViewComponentsCtrlListener

# Define a dictionary for overriding sound event names
_SOUND_EVENT_OVERRIDES = {
    'end_battle_last_kill': 'bc_end_battle_last_kill',
    'end_battle_capture_base': 'bc_end_battle_capture_base',
    'time_over': 'bc_end_battle_time_over'
}

# Define the BCFinishSoundPlayer class, which inherits from FinishSoundPlayer and IViewComponentsCtrlListener
class BCFinishSoundPlayer(FinishSoundPlayer, IViewComponentsCtrlListener):

    # Constructor
    def __init__(self):
        super(BCFinishSoundPlayer, self).__init__()
        self.__soundID = None  # Initialize the sound ID as None
        g_playerEvents.onRoundFinished += self.__onRoundFinished  # Register the __onRoundFinished method to be called when the round finishes
        return

    # Implement the IViewComponentsCtrlListener interface method
    def detachedFromCtrl(self, ctrlID):
        g_playerEvents.onRoundFinished -= self.__onRoundFinished  # Unregister the __onRoundFinished method when detached from the controller

    # Override the _playSound method from FinishSoundPlayer
    def _playSound(self, soundID):
        self.__soundID = _SOUND_EVENT_OVERRIDES.get(soundID, soundID)  # Get the sound ID from the overrides dictionary or use the provided sound ID

    # Implement the IViewComponentsCtrlListener interface
