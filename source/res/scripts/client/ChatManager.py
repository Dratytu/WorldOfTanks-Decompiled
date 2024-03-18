# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/ChatManager.py

# Importing necessary modules
from chat_shared import CHAT_ACTIONS, CHAT_CHANNEL_BATTLE, CHAT_CHANNEL_BATTLE_TEAM
import Event
from Singleton import Singleton

# Defining the ChatManager class
class ChatManager(Singleton):

    # Creating a singleton instance of the class
    @staticmethod
    def instance():
        return ChatManager()

    # Initializing the singleton instance
    def _singleton_init(self):
        # Initializing instance variables
        self.battleTeamChannelID = 0
        self.battleCommonChannelID = 0
        self.playerProxy = None
        # Initializing the dictionary to store chat action callbacks
        self.__chatActionCallbacks = {}
        return

    # Subscribing a callback for a chat action
    def subscribeChatAction(self, callback, action, channelId=None):
        # Getting the list of callbacks for the given action and channel ID
        cbs = self.__getChatActionCallbacks(action, channelId)
        # Adding the new callback to the list
        cbs += callback

    # Unsubscribing a callback from a chat action
    def unsubscribeChatAction(self, callback, action, channelId=None):
        # Getting the list of callbacks for the given action and channel ID
        cbs = self.__getChatActionCallbacks(action, channelId)
        # Removing the specified callback from the list
        cbs -= callback

    # Unsubscribing all callbacks from all chat actions
    def unsubcribeAllChatActions(self):
        # Iterating over all the lists of callbacks and clearing them
        for handlers in self.__chatActionCallbacks.values():
            handlers.clear()

    # Getting the list of callbacks for a given chat action and channel ID
    def __getChatActionCallbacks(self, action, channelId):
        # Using the given action and channel ID as the key for the dictionary
        channelId = channelId if channelId is not None else 0
        key = (action, channelId)
        # If the key is not present in the dictionary, creating a new list of callbacks
        if key not in self.__chatActionCallbacks:
            handlers = self.__chatActionCallbacks[key] = Event.Event()
        else:
            # If the key is present, getting the existing list of callbacks
            handlers = self.__chatActionCallbacks[key]
        # Returning the list of callbacks
        return handlers

    # Switching the player proxy
    def switchPlayerProxy(self, proxy):
        # Cleaning up the existing callbacks
        self.__cleanupMyCallbacks()
        # Setting up the new callbacks
        self.__setProxyChatActionsCallbacks({})
        # Setting the new player proxy
        self.playerProxy = proxy
        # Setting up the new callbacks with the chat action callbacks dictionary
        self.__setProxyChatActionsCallbacks(self.__chatActionCallbacks)
        # Setting up the callbacks for the new player proxy
        self.__setupMyCallbacks()

    # Setting up the chat actions callbacks for the player proxy
    def __setProxyChatActionsCallbacks(self, callbacks):
        # If the player proxy is not None, setting the chat actions callbacks for the player proxy
        if self.playerProxy is not None:
            self.playerProxy.setChatActionsCallbacks(callbacks)
        return

    # Cleaning up the existing callbacks for the old player proxy
    def __cleanupMyCallbacks(self):
        # If the player proxy is not None, cleaning up the chat actions callbacks
        if self.playerProxy is not None:
            self.battleTeamChannelID = 0
            self.battleCommonChannelID = 0
            # Unsubscribing the callback for receiving the channels list
            self.playerProxy.unsubscribeChatAction(self.__onChannelsListReceived, CHAT_ACTIONS.requestChannels)
        return

    # Setting up the callbacks for the new player proxy
    def __setupMyCallbacks(self):
        # If the player proxy is not None, setting up the callback for receiving the channels list
        if self.playerProxy is not None:
            self.playerProxy.subscribeChatAction(self.__onChannelsListReceived, CHAT_ACTIONS.requestChannels)
        return

    # Handling the received channels list
    def __onChannelsListReceived(self, chatActionData):
        # Iterating over the received channels list
        for ch
