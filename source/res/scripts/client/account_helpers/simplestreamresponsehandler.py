# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/SimpleStreamResponseHandler.py

import weakref
import zlib
import cPickle
import AccountCommands
from debug_utils import LOG_CODEPOINT_WARNING, LOG_CURRENT_EXCEPTION

class SimpleStreamResponseHandler(object):
    """
    A simple response handler for stream-based account commands.
    
    This class handles the response from account server for stream-based commands.
    It takes care of decompression and deserialization of the data.
    """
    
    def __init__(self, account, callback, default=None):
        """
        Initializes the response handler.
        
        :param account: The account object to which the handler is attached.
        :type account: accounts.Account
        :param callback: The callback function to be called when the response is received.
        :type callback: function
        :param default: The default value to be passed to the callback function in case of failure.
        :type default: object
        """
        self.__accountRef = weakref.ref(account)
        self.__callback = callback
        self.__default = default

    def __call__(self, requestID, resultID, errorStr, ext=None):
        """
        Callback function for the response.
        
        :param requestID: The ID of the request.
        :type requestID: int
        :param resultID: The ID of the result.
        :type resultID: int
        :param errorStr: The error string, if any.
        :type errorStr: str
        :param ext: Additional data.
        :type ext: dict
        """
        ext = ext or {}
        if resultID != AccountCommands.RES_STREAM:
            # If the result ID is not RES_STREAM, call the callback function with the given result ID and default value.
            self.__callback(resultID, self.__default)
        else:
            # If the result ID is RES_STREAM, subscribe the account for the stream and set the onStreamComplete function as the callback.
            self.__accountRef()._subscribeForStream(requestID, self.__onStreamComplete)

    def __onStreamComplete(self, isSuccess, data):
        """
        Callback function for the
