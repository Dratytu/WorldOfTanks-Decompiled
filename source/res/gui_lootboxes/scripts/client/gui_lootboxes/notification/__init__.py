# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: gui_lootboxes/scripts/client/gui_lootboxes/notification/__init__.py

# Import necessary modules and classes for handling notifications and actions
from gui.shared.system_factory import registerNotificationsListeners, registerNotificationsActionsHandlers

# Import custom classes for handling lootbox-related notifications and actions
from gui_lootboxes.notification.lootbox_listener import EventLootBoxesListener, LootBoxesBuyAvailableListener
from gui_lootboxes.notification.lootbox_action_handler import _OpenEventLootBoxesShopHandler

# Define a function to register client notification listeners
def registerClientNotificationListener():
    """
    Registers the necessary lootbox-related notification listeners for the client.

    This function registers two notification listeners: EventLootBoxesListener and LootBoxesBuyAvailableListener.
    These listeners will be triggered when specific lootbox-related events occur in the game.

    """
    # Register the listeners using the registerNotificationsListeners function from gui.shared.system_factory
    registerNotificationsListeners((EventLootBoxesListener, LootBoxesBuyAvailableListener))


# Define a function to register client notification handlers
def registerClientNotificationHandler():
    """
    Registers the necessary lootbox-related notification handlers for the client.

    This function registers one notification handler: _OpenEventLootBoxesShopHandler.
    This handler will be triggered when the corresponding notification is received and will perform the appropriate action.

    """
    # Register the handler using the registerNotificationsActionsHandlers function from gui.shared.system_factory
    registerNotificationsActionsHandlers((_OpenEventLootBoxesShopHandler,))
