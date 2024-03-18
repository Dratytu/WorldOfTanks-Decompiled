# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/gift_system.py

import logging
import typing
from functools import partial
import AccountCommands
from gui.gift_system.wrappers import GiftsHistoryData
from shared_utils import makeTupleByDict
from shared_utils.account_helpers.diff_utils import synchronizeDicts

_logger = logging.getLogger(__name__)
_CACHE_DIFF_KEY = 'cache'
_GIFT_SYSTEM_KEY = 'giftsData'

def _packEventHistoryData(eventExt):
    """
    Packs event history data into a tuple with GiftsHistoryData.

    :param eventExt: A dictionary containing event history data.
    :return: A tuple with GiftsHistoryData.
    """
    return makeTupleByDict(GiftsHistoryData, {'aggregated': eventExt,
     'detailed': []})


class _RequestHistoryProxy(object):
    """
    A proxy class for requesting event history data.

    :param reqEventIds: A list of event IDs to request.
    :param callback: A callback function to handle the response.
    """

    def __init__(self, reqEventIds, callback):
        self.__reqEventIds = reqEventIds
        self.__callback = callback

    def __call__(self, requestID, resultID, errorStr, ext=None):
        """
        Callback function for handling the response from the server.

        :param requestID: The ID of the request.
        :param resultID: The ID of the result.
        :param errorStr: An error string, if any.
        :param ext: Additional data from the server.
        """
        ext = ext if ext is not None else {}
        for eventID in self.__reqEventIds:
            # Pack the event history data into a tuple
            ext[eventID] = _packEventHistoryData(ext[eventID]) if eventID in ext else None

        # Call the callback function with the result and extended data
        self.__callback((resultID >= AccountCommands.RES_SUCCESS, ext))
        return


class GiftSystem(object):
    """
    A class for managing gift system data.

    :param syncData: An object for synchronizing data.
    :param commandsProxy: An object for sending commands.
    """

    def __init__(self, syncData, commandsProxy):
        self.__cache = {} # The cache for gift system data
        self.__ignore = True # A flag to ignore requests when not a player
        self.__syncData = syncData # The synchronization data object
        self.__commandsProxy = commandsProxy # The commands proxy object

    def onAccountBecomePlayer(self):
        """
        Called when the account becomes a player.
        """
        self.__ignore = False

    def onAccountBecomeNonPlayer(self):
        """
        Called when the account becomes a non-player.
        """
        self.__ignore = True

    def getCache(self, callback=None):
        """
        Gets the gift system data from the cache.

        :param callback: A callback function to handle the response.
        """
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        else:
            # Wait for synchronization and call the callback function with the cache data
            self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
            return

    def requestGiftsHistory(self, reqEventIds, callback):
        """
        Requests the gift history data for the given event IDs.

        :param reqEventIds: A list of event IDs to request.
        :param callback: A callback function to handle the response.
        """
        proxy = _RequestHistoryProxy(reqEventIds, callback)
        # Send the command to request the gift history data
        self.__commandsProxy.perform(AccountCommands.CMD_SYNC_GIFTS, reqEventIds, proxy)

    def synchronize(self, isFullSync, diff):
        """
        Synchronizes the gift system data.

        :param isFullSync: A flag indicating a full synchronization.
        :param diff: The data difference.
        """
        _logger.debug('Synchronize gift system')

