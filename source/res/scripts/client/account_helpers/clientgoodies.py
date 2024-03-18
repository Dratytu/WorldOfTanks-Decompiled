# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/ClientGoodies.py

# Importing necessary modules
import AccountCommands
from functools import partial
from shared_utils.account_helpers.diff_utils import synchronizeDicts

# Defining the ClientGoodies class
class ClientGoodies(object):
    # Initializing the class with syncData parameter
    def __init__(self, syncData):
        # Initializing instance variables
        self.__account = None  # variable to store the account object
        self.__syncData = syncData  # variable to store the syncData object
        self.__cache = {}  # dictionary to store the cache
        self.__ignore = True  # flag to check if the account is ignorable

    # onAccountBecomePlayer method
    def onAccountBecomePlayer(self):
        """
        Method to set the ignore flag to False when the account becomes a player.
        """
        self.__ignore = False

    # onAccountBecomeNonPlayer method
    def onAccountBecomeNonPlayer(self):
        """
        Method to set the ignore flag to True when the account becomes a non-player.
        """
        self.__ignore = True

    # setAccount method
    def setAccount(self, account):
        """
        Method to set the account object.
        """
        self.__account = account

    # synchronize method
    def synchronize(self, isFullSync, diff):
        """
        Method to synchronize the cache with the given diff.

        :param isFullSync: boolean to check if it's a full sync
        :param diff: dictionary containing the diff
        """
        # Handling full sync and updating the cache
        if isFullSync:
            self.__cache.clear()
        # Updating goodiesFull and goodiesDiff
        goodiesFull = diff.get(('goodies', '_r'))
        if goodiesFull:
            self.__cache = dict(goodiesFull)
        goodiesDiff = diff.get('goodies', None)
        if goodiesDiff is not None:
            synchronizeDicts(goodiesDiff, self.__cache.setdefault('goodies', {}))
        # Updating clanReserves if present in diff
        if 'cache' in diff:
            clanReservesDiff = diff['cache'].get('activeOrders', {})
            synchronizeDicts(clanReservesDiff, self.__cache.setdefault('clanReserves', {}))
        # Updating pr2_conversion if present in diff
        pr2ConversionResult = diff.get('pr2_conversion')
        if pr2ConversionResult is not None:
            self.__cache['pr2_conversion'] = pr2ConversionResult

    # getCache method
    def getCache(self, callback=None):
        """
        Method to get the cache and pass it to the callback function.

        :param callback: function to handle the response
        """
        # Checking if the account is ignorable
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        # Waiting for sync and handling the response
        else:
            self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
            return

    # getItems method
    def getItems(self, itemsType, callback):
        """
        Method to get the items of the specified type and pass it to the callback function.

        :param itemsType: string specifying the type of items
        :param callback: function to handle the response
        """
        # Checking if the account is ignorable
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        # Waiting for sync and handling the response
        else:
            self.__syncData.waitForSync(partial(self.__onGetItemsResponse, itemsType, callback))
            return

    # __onGetCacheResponse method
    def __onGetCacheResponse(self, callback, resultID):
        """
        Private method to handle the response of getCache.

        :param callback: function to handle the response
        :param resultID: integer specifying the result ID
        """
        # Handling negative resultID and passing it to the callback
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        # Passing the cache to the callback if it's not None
        else:
            if callback is not None:
                callback(resultID, self.__cache)
            return

    # __onGetItemsResponse method
    def __onGetItemsResponse(self, itemsType, callback, resultID):
        """
        Private method to handle the response of getItems.

        :param itemsType: string specifying the type of items
        :param callback: function to handle the response
        :param resultID: integer specifying the result ID
        """
        # Handling negative resultID and passing it to the callback
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        # Passing the items of the specified type to the callback if it's not None
        else:
            if callback is not None:
                callback(resultID, self.__cache.get(itemsType, None))
            return
