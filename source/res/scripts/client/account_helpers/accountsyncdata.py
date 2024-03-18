# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/AccountSyncData.py

from functools import partial
import AccountCommands
from SyncController import SyncController
from debug_utils import LOG_ERROR, LOG_DEBUG
from persistent_caches import SimpleCache
from live_crc_accountdata import accountDataPersistentHash, accountDataExtractPersistent, accountDataGetDiffForPersistent, accountDataMergePersistent
from shared_utils.account_helpers.diff_utils import synchronizeDicts

# AccountSyncData class is responsible for handling data synchronization for an account.
class AccountSyncData(object):

    def __init__(self):
        # Initializes the AccountSyncData object with various attributes.
        # revision: The current revision of the synchronized data.
        # __account: The account associated with this synchronization data.
        # __syncController: The sync controller used to manage synchronization requests and responses.
        # __ignore: A flag to ignore synchronization requests when the account is not a player.
        # __isSynchronized: A flag to indicate if the data is currently synchronized.
        # __syncID: A unique identifier for each synchronization request.
        # __subscribers: A list of callback functions to be called when synchronization is complete.
        # __isFirstSync: A flag to indicate if this is the first time synchronization is happening.
        # __persistentCache: A persistent cache for storing synchronized data.
        self.revision = 0
        self.__account = None
        self.__syncController = None
        self.__ignore = True
        self.__isSynchronized = False
        self.__syncID = 0
        self.__subscribers = []
        self.__isFirstSync = True
        self.__persistentCache = SimpleCache('account_caches', 'data')
        self.__persistentCache.data = None
        self.__persistentCache.isDirty = False

    def onAccountBecomePlayer(self):
        # Called when the account becomes a player.
        # Sets the ignore flag to False and starts the synchronization process.
        self.__ignore = False
        self._synchronize()

    def onAccountBecomeNonPlayer(self):
        # Called when the account becomes a non-player.
        # Sets the ignore flag to True and resets the synchronized flag.
        self.__ignore = True
        self.__isSynchronized = False

    def setAccount(self, account):
        # Sets the account associated with this synchronization data.
        # If the account is not None, sets the persistent cache's account and creates a new sync controller.
        # If the account is None, destroys the current sync controller and notifies subscribers of the non-player status.
        self.__account = account
        if self.__syncController is not None:
            self.__syncController.destroy()
            self.__syncController = None
        self.__savePersistentCache()
        if account is not None:
            self.__persistentCache.setAccount(account)
            self.__syncController = SyncController(account, self.__sendSyncRequest, self.__onSyncResponse, self.__onSyncComplete)
        else:
            self.__notifySubscribers(AccountCommands.RES_NON_PLAYER)

    def waitForSync(self, callback):
        # Waits for synchronization to complete before calling the provided callback function.
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER)
            return
        elif self.__isSynchronized:
            callback(AccountCommands.RES_CACHE)
            return
        else:
            if callback is not None:
                self.__subscribers.append(callback)
            return

    def updatePersistentCache(self, ext, isFullSync):
        # Updates the persistent cache with the provided data.
        # If the data contains a cache, merges it with the persistent cache and sets the dirty flag.
        # If the data does not contain a cache, synchronizes it with the persistent cache and sets the dirty flag.
        if ext.pop('__cache', None) is not None:
            if not self.__persistentCache.data:
                desc, cacheData = self.__persistentCache.data = self.__persistentCache.get()
                if accountDataPersistentHash(cacheData) != desc:
                    LOG_ERROR('Local account data cache is corrupted: resync')
                    self._resynchronize()
                    return False
                self.__persistentCache.data = cacheData
                self.__persistentCache.isDirty = False
            else:
                cacheData = self.__persistentCache.data
            if cacheData is None:
                LOG_ERROR("Incorrect cache state while syncing data: server said to use cache but I don't have any")
                self._resynchronize()
                return False
            accountDataMergePersistent(ext, cacheData)
            if synchronizeDicts(accountDataGetDiffForPersistent(ext), self.__persistentCache.data)[1]:
                self.__persistentCache.isDirty = True
        else:
            if self.__persistentCache.data is None:
                self.__persistentCache.data = {}
            synchronizeDicts(accountDataGetDiffForPersistent(ext), self.__persistentCache.data)
            self.__persistentCache.isDirty = True
        return True

    def _synchronize(self):
        # Starts the synchronization process if the ignore flag is False and the data is not already synchronized.
        if self.__ignore:
            return
        elif self.__isSynchronized:
            return
        else:
            self.__syncController.request(self.__getNextSyncID(), None)
            return

    def _resynchronize(self):
        # Resynchronizes the data if the persistent cache is corrupted or the data is in an incorrect state.
        if self.__ignore:
            return
        else:
            self.__isSynchronized = False
            self.revision = 0
            self.__clearPersistentCache()
            self.__syncController.request(self.__getNextSyncID(), None)
            return

    def __onSyncResponse(self, syncID, result
