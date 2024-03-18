# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/epicBattle/after_battle_reward_view_helpers.py

import logging
from collections import namedtuple
from itertools import chain
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController  # Interface for Epic Battle meta-game controller
from skeletons.gui.server_events import IEventsCache  # Interface for server events cache
from skeletons.gui.shared import IItemsCache  # Interface for shared items cache
from epic_constants import EPIC_BATTLE_LEVEL_IMAGE_INDEX  # Constants for Epic Battle level images

_logger = logging.getLogger(__name__)  # Logger instance

ProgressionLevelIconVO = namedtuple('MetaLevelVO', ('seasonLevel', 'playerLevel', 'bgImageId'))  # Named tuple for progression level VO

@dependency.replace_none_kwargs(eventsCache=IEventsCache)  # Inject IEventsCache instance
def getQuestBonuses(questsProgressData, questIDs, currentLevelQuestID, eventsCache=None):
    """
    Returns a list of bonuses for the given quests.
    :param questsProgressData: List of dictionaries containing quest progress data
    :param questIDs: List of quest IDs
    :param currentLevelQuestID: ID of the current level quest
    :param eventsCache: IEventsCache instance (optional)
    :return: List of bonuses
    """
    allQuests = eventsCache.getAllQuests()  # Get all quests from the events cache
    currentLevelQuest = allQuests.get(currentLevelQuestID, None)  # Get the current level quest
    bonuses = []  # Initialize an empty list for bonuses
    if currentLevelQuest and questsProgressData:
        # Iterate through the quests progress data and the given quest IDs
        for questID in questIDs:
            for q in questsProgressData:
                if questID in q:
                    bonuses.extend(allQuests.get(q).getBonuses())  # Add bonuses to the list
    return bonuses


@dependency.replace_none_kwargs(eventsCache=IEventsCache, itemsCache=IItemsCache)  # Inject IEventsCache and IItemsCache instances
def getFinishBadgeBonuses(questsProgressData, finishQuestID, eventsCache=None, itemsCache=None):
    """
    Returns a list of badge bonuses for the given finish quest.
    :param questsProgressData: List of dictionaries containing quest progress data
    :param finishQuestID: ID of the finish quest
    :param eventsCache: IEventsCache instance (optional)
    :param itemsCache: IItemsCache instance (optional)
    :return: List of badge bonuses
    """
    allQuests = eventsCache.getAllQuests()  # Get all quests from the events cache
    finishQuest = allQuests.get(finishQuestID, None)  # Get the finish quest
    if finishQuest is None:
        return []  # Return an empty list if the finish quest is not found
    elif finishQuestID in questsProgressData:
        return finishQuest.getBonuses()  # Return badge bonuses if the finish quest is in progress
    elif all((b.isAchieved for b in chain.from_iterable((d.getBadges() for d in finishQuest.getBonuses('dossier'))))):
        return finishQuest.getBonuses()  # Return badge bonuses if all dossier badges are achieved
    else:
        return finishQuest.getBonuses() if all((t.getNeededCount() <= itemsCache.items.tokens.getTokenCount(t.getID()) for t in finishQuest.accountReqs.getTokens())) else []  # Return badge bonuses if the player has enough tokens


@dependency.replace_none_kwargs(epicController=IEpicBattleMetaGameController)  # Inject IEpicBattleMetaGameController instance
def getProgressionIconVO(cycleNumber, playerLevel, epicController=None):
    """
    Returns a named tuple with progression level data.
    :param cycleNumber: Cycle number
    :param playerLevel: Player level
    :param epicController: IEpicBattleMetaGameController instance (optional)
    :return: Named tuple with progression level data
    """
    playerLevelStr = str(playerLevel) if playerLevel is not None else None  # Convert player level to string if it's not
