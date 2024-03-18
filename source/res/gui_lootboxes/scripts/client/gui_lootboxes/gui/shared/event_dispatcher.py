# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: gui_lootboxes/scripts/client/gui_lootboxes/gui/shared/event_dispatcher.py

import logging # Importing the logging module for logging messages
from gui import SystemMessages # Importing SystemMessages from gui for displaying system messages
from gui.impl import backport # Importing backport from gui.impl for string resources
from gui.impl.gen import R # Importing R from gui.impl.gen for string resources
from gui.shared.notifications import NotificationPriorityLevel # Importing NotificationPriorityLevel from gui.shared.notifications for system message priority level
from helpers import dependency # Importing dependency from helpers for dependency injection
from shared_utils import findFirst # Importing findFirst from shared_utils for finding the first item in an iterable that matches a condition
from skeletons.gui.shared import IItemsCache # Importing IItemsCache from skeletons.gui.shared for items cache

_logger = logging.getLogger(__name__) # Creating a logger instance with the name of the current module

def showLootBoxesWelcomeScreen(parent=None):
    # This function displays the Loot Boxes Welcome Screen window
    # Parameters:
    #   parent (Optional[Window]): The parent window of the Loot Boxes Welcome Screen window
    from gui_lootboxes.gui.impl.lobby.gui_lootboxes.welcome_screen import LootBoxesWelcomeScreenWindow
    window = LootBoxesWelcomeScreenWindow(parent=parent) # Creating an instance of LootBoxesWelcomeScreenWindow with the given parent
    window.load() # Loading the Loot Boxes Welcome Screen window


def showLootBoxOpenErrorWindow(parent=None):
    # This function displays the Loot Box Open Error window
    # Parameters:
    #   parent (Optional[Window]): The parent window of the Loot Box Open Error window
    from gui_lootboxes.gui.impl.lobby.gui_lootboxes.open_box_error import LootBoxesOpenBoxErrorWindow
    window = LootBoxesOpenBoxErrorWindow(parent) # Creating an instance of LootBoxesOpenBoxErrorWindow with the given parent
    window.load() # Loading the Loot Box Open Error window
    SystemMessages.pushMessage(text=backport.text(R.strings.system_messages.lootboxes.open.server_error.DISABLED()), priority=NotificationPriorityLevel.MEDIUM, type=SystemMessages.SM_TYPE.Error) # Displaying a system message with the specified text, priority, and type


def showStorageView(returnPlace=None, initialLootBoxId=0):
    # This function displays the Loot Boxes Storage window
    # Parameters:
    #   returnPlace (Optional[str]): The place to return to after closing the Loot Boxes Storage window. Default is TO_HANGAR
    #   initialLootBoxId (int): The ID of the initially selected loot box in the Loot Boxes Storage window. Default is 0
    from gui_lootboxes.gui.impl.lobby.gui_lootboxes.lootboxes_storage import LootBoxesStorageWindow
    from gui_lootboxes.gui.storage_context.context import ReturnPlaces
    if returnPlace is None:
        returnPlace = ReturnPlaces.TO_HANGAR # Setting the default value of returnPlace to TO_HANGAR if it is None
    window = LootBoxesStorageWindow(returnPlace, initialLootBoxId) # Creating an instance of LootBoxesStorageWindow with the given returnPlace and initialLootBoxId
    window.load() # Loading the Loot Boxes Storage window
    return


@dependency.replace_none_kwargs(itemsCache=IItemsCache)
def showSpecificBoxInStorageView(category=None, lootBoxType=None, returnPlace=None, itemsCache=None):
    # This function displays the Loot Boxes Storage window with a specific loot box selected
    # Parameters:
    #   category (Optional[str]): The category of the loot box to select. Default is None
    #   lootBoxType (Optional[str]): The type of the loot box to select. Default is None
    #   returnPlace (Optional[str]): The place to return to after closing the Loot Boxes Storage window. Default is TO_HANGAR
    #   itemsCache (IItemsCache): The items cache dependency
    from gui_lootboxes.gui.impl.lobby.gui_lootboxes.lootboxes_storage import LootBoxesStorageWindow
    from gui_lootboxes.gui.storage_context.context import ReturnPlaces

    def boxPredicate(lootBox):
        # A predicate function to find a loot box that matches the given category and lootBoxType
        if lootBox.getInventoryCount() == 0:
            return False
        isEqualCategory = lootBox.getCategory() == category if category else True
        isEqualType = lootBox.getType() == lootBoxType if lootBoxType else True
        return isEqualCategory and isEqualType

    boxId = 0
    box = findFirst(boxPredicate, itemsCache.items.tokens.getLootBoxes().itervalues()) # Finding a loot box that matches the given category and lootBoxType
    if box:
        boxId = box.getID() # Setting the boxId to the ID of
