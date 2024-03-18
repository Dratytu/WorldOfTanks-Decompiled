# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/SimpleStreamResponseHandler.py

import weakref
import zlib
import cPickle
import AccountCommands
from debug_utils import LOG_CODEPOINT_WARNING, LOG_CURRENT_EXCEPTION

class SimpleStreamResponseHandler(object):
    """
    A simple response handler for stream-based requests.
    
    This class handles the response from a stream-based request and calls the provided callback
    function with the result. If the request fails, it calls the callback with a default value
    and the RES_FAILURE result ID.
    """

    def __init__(self, account, callback, default=None):
        """
        Initializes the SimpleStreamResponseHandler instance.

        :param account: The account object to use for subscribing to the stream.
        :type account: account_helpers.AccountManager
        :param callback: The callback function to call with the result of the request.
        :type callback: function
        :param default: The default value to use if the request fails.
        :type default: object
        """
        self.__accountRef = weakref.ref(account)
        self.__callback = callback
        self.__default = default

    def __call__(self, requestID, resultID, errorStr, ext=None):
        """
        Called when a response is received for the request.

        :param requestID: The ID of the request.
        :type requestID: int
        :param resultID: The ID of the result.
        :type resultID: int
        :param errorStr: The error string, if any.
        :type errorStr: str
        :param ext: Additional extension data.
        :type ext: dict
        """
        ext = ext or {}
        if resultID != AccountCommands.RES_STREAM:
            # If the result ID is not RES_STREAM, call the callback with the result ID and default value.
            self.__callback(resultID, self.__default)
        else:
            # If the result ID is RES_STREAM, subscribe to the stream and call the onStreamComplete method.
            self.__accountRef()._subscribeForStream(requestID, self.__onStreamComplete)

    def __onStreamComplete(self, is
