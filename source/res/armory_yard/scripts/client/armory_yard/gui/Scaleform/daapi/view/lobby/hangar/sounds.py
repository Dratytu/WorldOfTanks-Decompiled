# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/Scaleform/daapi/view/lobby/hangar/sounds.py

import WWISE # Import the WWISE library for sound management
from gui.impl.gen import R # Import the R class for accessing resources
from gui.impl.lobby.video.video_sound_manager import IVideoSoundManager, SoundManagerStates # Import the IVideoSoundManager interface and SoundManagerStates enum
from shared_utils import CONST_CONTAINER # Import the CONST_CONTAINER class

# Define a class for storing constants related to the Armory Yard sounds
class ArmoryYardSounds(CONST_CONTAINER):
    VIDEO_EP2_ARMOUR = 'ay_ep_02_video_stage_09' # Constant for the Armory Yard EP2 Armour video sound
    VIDEO_EP2_GUN = 'ay_ep_02_video_stage_22' # Constant for the Armory Yard EP2 Gun video sound
    VIDEO_EP2_TURRET = 'ay_ep_02_video_stage_29' # Constant for the Armory Yard EP2 Turret video sound
    VIDEO_EP2_TRACKS = 'ay_ep_02_video_stage_32' # Constant for the Armory Yard EP2 Tracks video sound
    VIDEO_EP2_REWARD = 'ay_ep_02_video_stage_38' # Constant for the Armory Yard EP2 Reward video sound
    VIDEO_EP2_INTRO = 'ay_ep_02_video_stage_00' # Constant for the Armory Yard EP2 Intro video sound
    VIDEO_PAUSE = 'ay_video_pause' # Constant for the video pause sound
    VIDEO_RESUME = 'ay_video_resume' # Constant for the video resume sound
    VIDEO_STOP = 'ay_video_stop' # Constant for the video stop sound


# Define a class for controlling the sounds of Armory Yard videos
class ArmoryYardVideoSoundControl(IVideoSoundManager):
    # Define a dictionary that maps video IDs to sound constants
    __VIDEO_TO_SOUND = {'ay_ep2_armour': ArmoryYardSounds.VIDEO_EP2_ARMOUR,
     'ay_ep2_gun': ArmoryYardSounds.VIDEO_EP2_GUN,
     'ay_ep2_turret': ArmoryYardSounds.VIDEO_EP2_TURRET,
     'ay_ep2_tracks': ArmoryYardSounds.VIDEO_EP2_TRACKS,
     'ay_ep2_reward': ArmoryYardSounds.VIDEO_EP2_REWARD,
     'ay_ep2_intro': ArmoryYardSounds.VIDEO_EP2_INTRO}

    def __init__(self, videoID):
        # Initialize the object with a video ID
        self.__videoID = videoID
        self.__state = None # Initialize the state variable to None
        return

    @property
    def videoSoundEvent(self):
        # Return the sound constant associated with the video ID
        return self.__getMapping().get(self.__videoID)

    def start(self):
        # Play the sound associated with the video ID
        sound = self.videoSoundEvent
        if sound:
            WWISE.WW_eventGlobal(sound)
            self.__state = SoundManagerStates.PLAYING

    def stop(self):
        # Stop the sound if it is currently playing
        if self.__state != SoundManagerStates.STOPPED:
            WWISE.WW_eventGlobal(ArmoryYardSounds.VIDEO_STOP)
            self.__state = SoundManagerStates.STOPPED

    def pause(self):
        # Pause the sound
        WWISE.WW_eventGlobal(ArmoryYardSounds.VIDEO_PAUSE)
        self.__state = SoundManagerStates.PAUSE

    def unpause(self):
        # Resume the sound
        WWISE.WW_event
