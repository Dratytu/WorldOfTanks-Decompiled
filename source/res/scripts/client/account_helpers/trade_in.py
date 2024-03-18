# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/trade_in.py

import logging
import time
import typing
import AccountCommands

# If type checking is enabled, this code will ensure that the correct types are used
if typing.TYPE_CHECKING:
    from Account import PlayerAccount

_logger = logging.getLogger(__name__)
_SECONDS_IN_DAY = 86400

class TradeIn(object):

    def __init__(self):
        """
        Initialize the TradeIn class. The account attribute is initialized to None.
        """
        self._account = None
        return

    def setAccount(self, account):
        """
        Set the account attribute to the given account object.
        """
        self._account = account

    def addTokenDev(self, tokenID, expiryTimeOffset=_SECONDS_IN_DAY):
        """
        Add a token with the given tokenID and an expiry time offset from the current time.
        The expiry time is calculated by adding the offset to the current time.
        The command is then sent to the account object to add the token.
        """
        currentTime = time.time()
        expiryTime = int(currentTime + expiryTimeOffset)
        self._account._doCmdIntStr(AccountCommands.CMD_TRADE_IN_ADD_TOKEN, expiryTime, tokenID, self._onCmdResponseReceived)

    def removeTokenDev(self, tokenID):
        """
        Remove the token with the given tokenID from the account object.
        """
        self._account._doCmdStr(AccountCommands.CMD_TRADE_IN_REMOVE_TOKEN, tokenID, self._onCmdResponseReceived)

    def _onCmdResponseReceived(self, resultID, requestID, errorStr, errorMsg=None):
        """
        Callback function that is called when a command response is received.
        If the requestID is not valid, an error message is logged.
        """
        if not
