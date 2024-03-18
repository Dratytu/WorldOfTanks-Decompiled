# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/ReplayEvents.py

import Event

# Define a class named _ReplayEvents, which inherits from the object class
class _ReplayEvents(object):
    
    # Define a property method isPlaying, which returns the value of the private attribute __isPlaying
    @property
    def isPlaying(self):
        return self.__isPlaying

    # Define a property method isRecording, which returns the value of the private attribute __isRecording
    @property
    def isRecording(self):
        return self.__isRecording
    
    # Constructor method for the _ReplayEvents class
    def __init__(self):
        # Initialize the onTimeWarpStart event using Event.Event()
        self.onTimeWarpStart = Event.Event()
        # Initialize the onTimeWarpFinish event using Event.Event()
        self.onTimeWarpFinish = Event.Event()
        # Initialize the onPause event using Event.Event()
        self.onPause = Event.Event()
        # Initialize the onMuteSound event using Event.Event()
        self.onMuteSound = Event.Event()
        # Initialize the onWatcherNotify event using Event.Event()
        self.onWatcherNotify = Event.Event()
        # Initialize the onReplayTerminated event using Event.Event()
        self.onReplayTerminated = Event.Event()
        # Initialize the __isPlaying attribute with a value of False
        self.__isPlaying = False
        # Initialize the __isRecording attribute with a value of False
        self.__isRecording = False

    # Define a method onRecording, which sets the value of the __isRecording attribute to True
    def onRecording(self):
        self.__isRecording = True

    # Define a method onPlaying, which sets the value of the __isPlaying attribute to True
    def onPlaying(self):
        self.__isPlaying = True

# Define a global variable
