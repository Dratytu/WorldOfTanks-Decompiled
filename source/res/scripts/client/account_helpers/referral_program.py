# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/referral_program.py

# Import necessary modules
from functools import partial
import typing
import AccountCommands
from shared_utils.account_helpers.diff_utils import synchronizeDicts

# If type checking is enabled, define the required types for the variables and functions
if typing.TYPE_CHECKING:
    from typing import Callable, Dict, Optional

# Define constants
RP_PDATA_KEY = 'refProgram'

# Define the ReferralProgram class
class ReferralProgram(object):

    # Initialize the class with syncData
    def __init__(self, syncData):
        self.__account = None  # Type: Optional[Account]
        self.__cache = {}  # Type: Dict[str, Any]
        self.__ignore = True  # Type: bool
        self.__syncData = syncData  # Type: Any
        return

    # Set the account object
    def setAccount(self, account):
        self.__account = account

    # Called when the account becomes a player
    def onAccountBecomePlayer(self):
        self.__ignore = False

    # Called when the account becomes a non-player
    def onAccountBecomeNonPlayer(self):
        self.__ignore = True

    # Get the cache of referral program data
    def getCache(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        else:
            self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
            return

    # Synchronize the referral program data
    def synchronize(self, isFullSync, diff):
        if isFullSync and self.__cache:
            self.__cache.clear()
        if RP_PDATA_KEY in diff:
            synchronizeDicts(diff[RP_PDATA_KEY], self.__cache.setdefault(RP_PDATA_KEY, {}))

    # Callback for getting the cache of referral program data
    def __onGetCacheResponse(self, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        else:
            if callback is not None:
                callback(resultID, self.__cache)
            return

    # Collect points for the referral program
    def collectRPPgbPoints(self, callback):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(requestID, resultID, errorStr)
        else:
            proxy = None
        self.__account._doCmdInt(AccountCommands.CMD_COLLECT_RP_PGB_POINTS, 0, proxy)
        return

    # Increment the recruit delta by a given value
    def incrementRecruitDelta(self, deltaInc, callback):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(requestID, resultID, errorStr)
        else:
            proxy = None
        self.__account._doCmdInt(AccountCommands.CMD_RP_INCREMENT_RECRUIT_DELTA, deltaInc, proxy)
        return

    # Reset the recruit delta to its initial value
    def resetRecruitDelta(self, callback):
        if callback is not None:
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(requestID, resultID, errorStr)
        else:
            proxy = None
        self.__account._doCmdInt(AccountCommands.CMD_RP_RESET_RECRUIT_DELTA, 0, proxy)
        return
