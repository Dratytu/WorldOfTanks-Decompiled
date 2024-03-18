# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/ClientGlobalMap.py

# Import necessary modules
from GlobalMapBase import GlobalMapBase, GM_CLIENT_METHOD
from debug_utils import LOG_DEBUG_DEV
import Event

# Define the ClientGlobalMap class that inherits from GlobalMapBase
class ClientGlobalMap(GlobalMapBase):

    # Initialize the class with an optional account parameter
    def __init__(self, account=None):
        self.__account = account
        self.__eManager = Event.EventManager()
        # Call the constructor of the parent class
        GlobalMapBase.__init__(self)
        self.__requestID = 0

    # Clear all event listeners
    def clear(self):
        self.__eManager.clear()

    # Set the account parameter
    def setAccount(self, account=None):
        self.__account = account

    # Get the next available request ID
    def __getNextRequestID(self):
        self.__requestID += 1
        return self.__requestID

    # Call a global map method with the given arguments
    def __callGlobalMapMethod(self, *args):
        requestID = self.__getNextRequestID()
        LOG_DEBUG_DEV('base.callGlobalMapMethod', requestID, args)
        self.__account.base.accountGlobalMapConnector_callGlobalMapMethod(requestID, *args)
        return requestID

    # Handle a global map reply with the given request ID, result code, and result string
    def onGlobalMapReply(self, reqID, resultCode, resultString):
        LOG_DEBUG_DEV('onGlobalMapReply: reqID=%s, resultCode=%s, resultString=%r' % (reqID, resultCode, resultString))

    # Subscribe to global map events
    def subscribe(self):
        return self.__callGlobalMapMethod(GM_CLIENT_METHOD.SUBSCRIBE, 0, '')

    # Unsubscribe from global map events
    def unsubscribe(self):
        return self.__callGlobalMapMethod(GM_CLIENT_METHOD.UNSUBSCRIBE, 0, '')

    # Join a battle with the given battle ID
    def joinBattle(self, battleID):
        return self.__callGlobalMapMethod(GM_CLIENT_METHOD.JOIN_BATTLE, battleID, '')

    # Set the dev mode status
    def setDevMode(self, isOn):
        return self.__callGlobalMapMethod(GM_CLIENT_METHOD.SET_DEV_MODE, int(isOn), '')

    # Send a keep-alive message to the server
    def keepAlive(self):
        return self.__callGlobalMapMethod(GM_CLIENT_METHOD.KEEP_ALIVE, 0, '')

    # Handle a global map update with the given packed operations and packed update
    def onGlobalMapUpdate(self, packedOps, packedUpdate):
        LOG_DEBUG_DEV('onGlobalMapUpdate: packedOps len=%s, packedUpdate len=%s' % (len(packedOps), len(packedUpdate)))
        # Unpack the update if it exists
        if packedUpdate:
            self.unpack(packedUpdate)
        # Unpack the operations if they exist
        elif packedOps:
            self.unpackOps(packedOps)

    # Unpack a battle from the given packed data
    def _unpackBattle(self, packedData):
        LOG_DEBUG_DEV('_unpackBattle: packedData len=%s' % (len(packedData),))
        packedData = GlobalMapBase._unpackBattle(self, packedData)
        return packedData

    # Remove a battle with the given battle ID
    def _removeBattle(self, battleID):
        LOG_DEBUG_DEV('_removeBattle: battleID=%s' % (battleID,))
        GlobalMapBase._removeBattle(self, battleID)

    # Unpack a battle unit from the given packed data
    def _unpackBattleUnit(self, packedData):
        LOG_DEBUG_DEV('_unpackBattleUnit: packedData len=%s' % (len(packedData),))
        packedData = GlobalMapBase._unpackBattleUnit(self, packedData)
        return packedData

    # Remove a battle unit with the given battle ID
    def _removeBattleUnit(self, battleID):
        LOG_DEBUG_DEV('_removeBattleUnit: battleID=%s' % (battleID,))
        GlobalMapBase._removeBattleUnit(self, battleID)
