# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/battle_control/controllers/quest_progress/quest_progress_ctrl.py

import logging # Importing the logging module for logging messages and errors
import BigWorld # Importing BigWorld for using callbacks
from Event import EventManager, Event # Importing EventManager and Event for managing and triggering events
from account_helpers import AccountSettings # Importing AccountSettings for accessing user settings
from account_helpers.AccountSettings import LAST_SELECTED_PM_BRANCH # Importing LAST_SELECTED_PM_BRANCH constant
from constants import ARENA_PERIOD # Importing ARENA_PERIOD constants
from gui.Scaleform.locale.RES_ICONS import RES_ICONS # Importing RES_ICONS for getting quest icons
from gui.battle_control.arena_info.interfaces import IArenaPeriodController, IArenaVehiclesController # Importing interfaces for implementing arena period and vehicles controllers
from gui.battle_control.arena_info.settings import ARENA_LISTENER_SCOPE as _SCOPE # Importing ARENA_LISTENER_SCOPE constant
from gui.battle_control.battle_constants import BATTLE_CTRL_ID # Importing BATTLE_CTRL_ID constant
from gui.server_events.personal_progress.formatters import DetailedProgressFormatter # Importing DetailedProgressFormatter for formatting quest progress
from gui.server_events.personal_progress.storage import BattleProgressStorage # Importing BattleProgressStorage for storing quest progress
from helpers import dependency # Importing dependency for managing dependencies
from personal_missions import PM_STATE # Importing PM_STATE constants
from shared_utils import first # Importing first function for getting the first item from an iterable
from skeletons.gui.lobby_context import ILobbyContext # Importing ILobbyContext from skeletons
from skeletons.gui.server_events import IEventsCache # Importing IEventsCache from skeletons

_logger = logging.getLogger(__name__) # Creating a logger instance with the current module name

class QuestProgressController(IArenaPeriodController, IArenaVehiclesController): # Defining QuestProgressController class that implements IArenaPeriodController and IArenaVehiclesController interfaces
    eventsCache = dependency.descriptor(IEventsCache) # Declaring a dependency on IEventsCache
    lobbyContext = dependency.descriptor(ILobbyContext) # Declaring a dependency on ILobbyContext

    def __init__(self): # Initializing the QuestProgressController class
        super(QuestProgressController, self).__init__() # Calling the constructor of the superclass
        self._period = ARENA_PERIOD.IDLE # Initializing the period to IDLE
        self._endTime = 0 # Initializing the end time to 0
        self._length = 0 # Initializing the length to 0
        self._callbackID = None # Initializing the callback ID to None
        self.__storage = {} # Initializing the storage as an empty dictionary
        self.__selectedQuest = None # Initializing the selected quest to None
        self.__eManager = EventManager() # Creating an instance of EventManager
        self.__battleCtx = None # Initializing the battle context to None
        self.__isInited = False # Initializing the inited flag to False
        self.__inProgressQuests = {} # Initializing the in-progress quests as an empty dictionary
        self.__needToShowAnimation = False # Initializing the need to show animation flag to False
        self.onConditionProgressUpdate = Event(self.__eManager) # Creating an event for condition progress update
        self.onHeaderProgressesUpdate = Event(self.__eManager) # Creating an event for header progresses update
        self.onFullConditionsUpdate = Event(self.__eManager) # Creating an event for full conditions update
        self.onQuestProgressInited = Event(self.__eManager) # Creating an event for quest progress init
        self.onShowAnimation = Event(self.__eManager) # Creating an event for showing animation
        self.__lastSelectedQuestID = 0 # Initializing the last selected quest ID to 0
        return

    def getInProgressQuests(self): # A method for getting in-progress quests
        return self.__inProgressQuests # Returning the in-progress quests

    def hasQuestsToPerform(self): # A method for checking if there are any quests to perform
        return bool(self.__inProgressQuests) # Returning True if there are any quests, otherwise False

    def getSelectedQuest(self): # A method for getting the selected quest
        return self.__selectedQuest # Returning the selected quest

    def isInited(self): # A method for checking if the controller is initialized
        return self.__isInited # Returning the inited flag

    def selectQuest(self, missionID): # A method for selecting a quest
        self.__selectedQuest = self.__inProgressQuests.get(missionID) # Setting the selected quest to the quest with the given ID
        AccountSettings.setSettings(LAST_SELECTED_PM_BRANCH, self.__selectedQuest.getPMType().branch) # Updating the last selected PM branch in user settings
        if self.__selectedQuest:
            self.__needToShowAnimation = self.__lastSelectedQuestID != self.__selectedQuest.getID() # Setting the need to show animation flag if the selected quest is different from the last selected quest
        self.onFullConditionsUpdate() # Triggering the full conditions update event

    def invalidateArenaInfo(self): # A method for invalidating arena info
        isPersonalMissionsEnabled = self.lobbyContext.getServerSettings().isPersonalMissionsEnabled # Getting the personal missions enabled flag from the lobby context
        if not self.__isInited: # If the controller is not initialized
            lastSelectedBranch = AccountSettings.getSettings(LAST_SELECTED_PM_BRANCH) # Getting the last selected PM branch from user settings
            personalMissions = self.eventsCache.getPersonalMissions() # Getting the personal missions from the events cache
            selectedMissionsIDs = self.__battleCtx.getSelectedQuestIDs() # Getting the selected quest IDs from the battle context
            selectedMissionsInfo =
