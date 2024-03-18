# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/AccountSyncData.py

from functools import partial
import AccountCommands
from SyncController import SyncController
from debug_utils import LOG_ERROR, LOG_DEBUG
from persistent_caches import SimpleCache
from live_crc_accountdata import accountDataPersistentHash, accountDataExtractPersistent, accountDataGetDiffForPersistent, accountDataMergePersistent
from shared_utils.account_helpers.diff_utils import synchronizeDicts

# AccountSyncData class is responsible for handling account data synchronization
class AccountSyncData(object):

    def __init__(self):
        # Initialize revision counter, account object, sync controller, ignore flag,
        # isSynchronized flag, syncID, subscribers list, isFirstSync flag, and persistent cache
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
        # Called when the account becomes a player, sets ignore flag to False and
        # initiates synchronization if not already done
        self.__ignore = False
        self._synchronize()

    def onAccountBecomeNonPlayer(self):
        # Called when the account becomes a non-player, sets ignore flag to True
        # and unsynchronizes the data
        self.__ignore = True
        self.__isSynchronized = False

    def setAccount(self, account):
        # Sets the account object and initializes sync controller if account is not None
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
        # Waits for synchronization to complete and calls the provided callback
        # function with the result
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
        # Updates the persistent cache with the provided data
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
        # Initiates synchronization if not already done
        if self.__ignore:
            return
        elif self.__isSynchronized:
            return
        else:
            self.__syncController.request(self.__getNextSyncID(), None)
            return

    def _resynchronize(self):
        # Resynchronizes the data
        LOG_DEBUG('resynchronize')
        if self.__ignore:
            return
        else:
            self.__isSynchronized = False
            self.revision = 0
            self.__clearPersistentCache()
            self.__syncController.request(self.__getNextSyncID(), None)
            return

    def __onSyncResponse(self, syncID, resultID, ext=None):
        # Called when a synchronization response is received
        ext = ext or {}
        if resultID == AccountCommands.RES_NON_PLAYER:
            return
        if syncID != self.__syncID:
            return
        if resultID < 0:
            LOG_ERROR('Data synchronization failed.')
            self._resynchronize()
            return
        if self.revision != ext.get('prevRev', self.revision):
            LOG_ERROR('Incorrect diff received', self.revision, ext['prevRev'])
            self._resynchronize()
            return
        self.revision = ext.get('rev', self.revision)
        self.__isSynchronized = True
        if not self.__account._update(not self.__isFirstSync, ext):
            return
        self.__isFirstSync = False
        self.__notifySubscribers(resultID)

    def __onSyncComplete(self, syncID, data):
        # Called when a synchronization is complete
        if syncID != self.__syncID:

