# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/avatar_helpers/AvatarSyncData.py

import AccountCommands

class AvatarSyncData(object):
    """
    A class that manages avatar synchronization data.
    """

    def __init__(self):
        """
        Initializes a new instance of the AvatarSyncData class.
        """
        self.__isSynchronized = False  # A flag indicating if the avatar is synchronized.
        self.__subscribers = []  # A list of callback functions to be called when synchronization is complete.
        self.__avatar = None  # The avatar object to be synchronized.
        return

    def setAvatar(self, avatar):
        """
        Sets the avatar object to be synchronized.
        :param avatar: The avatar object.
        """
        self.__avatar = avatar

    def onAvatarBecomePlayer(self):
        """
        Handles the event when the avatar becomes a player.
        """
        self.__isSynchronized = self.__avatar.isSynchronized()  # Sets the synchronization flag based on the avatar's synchronization status.
        if not self.__isSynchronized:
            self.__avatar._doCmdStr(AccountCommands.CMD_GET_AVATAR_SYNC, '', self.__onSyncResponse)  # Requests synchronization if not already synchronized.

    def onAvatarBecomeNonPlayer(self):
        """
        Handles the event when the avatar becomes a non-player.
        """
        pass

    def waitForSync(self, callback):
        """
        Waits for synchronization to complete and calls the provided callback function.
        :param callback: The callback function to be called when synchronization is complete.
        """
        if self.__isSynchronized:
            callback(AccountCommands.RES_CACHE)  # Calls the callback function immediately if synchronization is already complete.
        if callback is not None:
            self.__subscribers.append(callback
