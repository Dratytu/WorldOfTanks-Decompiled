# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/winback.py

import typing
import AccountCommands

# If type checking is enabled, the following types are expected:
# Callable: The type of the `callback` parameter in the `turnOffBattles` method
# Optional[Any]: The type of the `ext` parameter in the `perform` method of `commandsProxy`
if typing.TYPE_CHECKING:
    from typing import Callable, Optional

class Winback(object):

    def __init__(self, commandsProxy):
        """
        Initialize the Winback class with a given `commandsProxy` object.

        :param commandsProxy: An object that provides functionality for executing commands.
        """
        self.__commandsProxy = commandsProxy

    def turnOffBattles(self, reason, callback=None):
        """
        Turn off battles for winback purposes with a given reason.

        :param reason: A string that represents the reason for turning off battles.
        :param callback: An optional callback function that is called when the command is completed.
        """
        if callback is not None:
            # If a callback is provided, create a proxy function that will call the callback
            # with the given result and error strings.
            proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr)
        else:
            # If no callback is provided, set the proxy to None.
            proxy = None

        # Execute the command to turn off winback battles using the provided `commandsProxy`.
        self.__commandsProxy.perform(AccountCommands.CMD_TURNOFF_WINBACK_BATTLES, reason, proxy)

