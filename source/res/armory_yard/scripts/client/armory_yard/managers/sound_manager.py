# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/managers/sound_manager.py

import WWISE
from armory_yard.gui.Scaleform.daapi.view.lobby.hangar.sound_constants import SOUNDS

class ArmorySoundManager(object):
    """
    This class is responsible for managing sounds in the Armory Yard.
    """
    __slots__ = ('__isFirstEntrance',)

    def __init__(self):
        """
        Initialize the ArmorySoundManager instance.
        """
        self.__isFirstEntrance = True

    def clear(self):
        """
        Reset the ArmorySoundManager instance to its initial state.
        """
        self.__isFirstEntrance = True

    def onSoundModeChanged(self, isArmorySoundMode):
        """
        This method is called when the sound mode is changed.

        :param isArmorySoundMode: A boolean indicating whether the Armory sound mode is enabled.
        """
        if isArmorySoundMode:
            if self.__isFirstEntrance:
                # Play the FIRST_ENTER sound if it's the first entrance.
                self.__isFirstEntrance = False
                WWISE.WW_eventGlobal(SOUNDS.FIRST_ENTER)
            else:
                # Play the ENTER sound if it's not the first entrance.
                WWISE.WW_eventGlobal(SOUNDS.ENTER)
        else:
            # Play the EXIT sound when exiting the Armory sound mode.
            WWISE.WW_eventGlobal(SOUNDS.EXIT)
