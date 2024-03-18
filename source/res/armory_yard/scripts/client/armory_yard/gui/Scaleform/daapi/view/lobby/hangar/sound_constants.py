# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/Scaleform/daapi/view/lobby/hangar/sound_constants.py

from gui.sounds.filters import StatesGroup, States  # Importing state constants for sound settings.
from sound_gui_manager import CommonSoundSpaceSettings  # Importing CommonSoundSpaceSettings class for defining sound spaces.
from shared_utils import CONST_CONTAINER  # Importing CONST_CONTAINER for defining constants container.

class SOUNDS(CONST_CONTAINER):
    # A container for various sound-related constants.
    COMMON_SOUND_SPACE = 'armory_yard'  # The name of the common sound space for the armory yard.
    COMMON_SOUND_INTRO_SPACE = 'armory_yard_intro'  # The name of the common sound space for the armory yard intro.
    COMMON_SOUND_VIDEO_REWARD_SPACE = 'armory_yard_reward_video'  # The name of the common sound space for the reward video in the armory yard.
    STATE_PLACE = 'STATE_hangar_place'  # The entrance state for the armory yard sound space.
    STATE_PLACE_AY = 'STATE_hangar_place_customization'  # The entrance state for the armory yard intro sound space.
    VO_TAPE_RECORDER = 'ay_voiceover_taperecorder_ep_02_stage_{:02d}_start'  # The format string for the voice-over tape recorder sound name.
    FIRST_ENTER = 'armory_yard_enter_first'  # The name of the sound event for the first entry to the armory yard.
    ENTER = 'armory_yard_enter'  # The name of the sound event for entering the armory yard.
    EXIT = 'armory_yard_exit'  # The name of the sound event for exiting the armory yard.


def getStageVoTapeRecorderName
