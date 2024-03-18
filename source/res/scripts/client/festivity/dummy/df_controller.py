# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/festivity/dummy/df_controller.py

import Event
from festivity.base import FestivityQuestsHangarFlag
from skeletons.gui.game_control import IFestivityController

# Default flags for hangar quests
_DEFAULT_QUESTS_FLAG = FestivityQuestsHangarFlag(None, None, None)

class DummyController(IFestivityController):

    def __init__(self):
        # Initialize the superclass
        super(DummyController, self).__init__()
        # Initialize the state and event manager
        self.__state = None
        self.__em = Event.EventManager()
        # Initialize the event for state change
        self.onStateChanged = Event.Event(self.__em)
        return

    def isEnabled(self):
        # Always return False as this is a dummy controller
        return False

    def getHangarQuestsFlagData(self):
        # Return default flags for hangar quests
        return _DEFAULT_QUESTS_FLAG

