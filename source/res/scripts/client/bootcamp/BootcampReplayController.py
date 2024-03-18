# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bootcamp/BootcampReplayController.py

# Import the LOG_DEBUG_DEV_BOOTCAMP utility function for logging debug messages
from debug_utils_bootcamp import LOG_DEBUG_DEV_BOOTCAMP

# Import the BattleReplay module, which contains the replay controller
import BattleReplay

# Define a constant list of bootcamp replay event names
BOOTCAMP_REPLAY_EVENTS = ('bootcampMarkers_onTriggerActivated', 'bootcampMarkers_onTriggerDeactivated', 'bootcampMarkers_showMarker', 'bootcampMarkers_hideMarker', 'bootcampHint_show', 'bootcampHint_hide', 'bootcampHint_complete', 'bootcampHint_close', 'bootcampHint_onHided')

class BootcampReplayControllerQueue:

    def __init__(self, name):
        # Initialize the queue with a name, data list, and callback
        self.__name = name
        self.__data = []
        self.__callback = None

    def init(self):
        # Register the queue's callback method with the replay controller
        BattleReplay.g_replayCtrl.setDataCallback(self.__name, self.replayCallbackeMethod)

    def fini(self):
        # Unregister the queue's callback method from the replay controller
        BattleReplay.g_replayCtrl.delDataCallback(self.__name, self.replayCallbackeMethod)
        self.__callback = None

    def replayCallbackeMethod(self, binData):
        # Callback method for handling replay data
        if self.__callback is not None:
            # If there's a callback, call it with the replay data
            return self.__callback(binData)
        else:
            # If there's no callback, store the replay data in the queue
            self.__data.append(binData)
            return

    def setDataCallback(self, callback):
        # Set the queue's callback and process any stored replay data
        self.__callback = callback
        for binData in self.__data:
            callback(binData)

        self.__data = []

    def delDataCallback(self, callback):
        # Unregister the specified callback if it matches the queue's callback
        if callback is not self.__callback:
            LOG_DEBUG_DEV_BOOTCAMP('Multiple callback unsubscribe:', self.__name)
            return
        else:
            self.__callback = None
            return


class BootcampReplayController:

    def __init__(self):
        # Initialize the replay controller with a dictionary of queues
        self.__queues = {}
        for name in BOOTCAMP_REPLAY_EVENTS:
            self.__queues[name] = BootcampReplayControllerQueue(name)

    def init(self):
        # Initialize all the queues in the replay controller
        for quque in self.__queues.itervalues():
            quque.init()

    def fini(self):
        # Uninitialize all the queues in the replay controller
        for quque in self.__queues.itervalues():
            quque.fini()

    def setDataCallback(self, eventName, callback):
        # Set the callback for a specific event queue
        if eventName not in self.__queues:
            LOG_DEBUG_DEV_BOOTCAMP('Failed to set replay data callback:', eventName)
            return
        queue = self.__queues[eventName]
        queue.setDataCallback(callback)

    def delDataCallback(self, eventName, callback):
        # Unregister a specific callback from an event queue
        if eventName
