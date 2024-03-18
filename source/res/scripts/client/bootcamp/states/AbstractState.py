# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bootcamp/states/AbstractState.py

import BigWorld
from debug_utils_bootcamp import LOG_DEBUG_DEV_BOOTCAMP

class AbstractState(object):
    """
    Abstract base class for all bootcamp states.
    Provides basic functionality for state management.
    """

    def __init__(self, stateId):
        """
        Initialize the state object with a unique state identifier.
        :param stateId: A unique identifier for the state.
        """
        super(AbstractState, self).__init__()
        self.__id = stateId  # The unique identifier for the state.
        self.__isActive = False  # Flag to track if the state is currently active.

    def id(self):
        """
        Return the unique identifier for the state.
        :return: The unique identifier for the state.
        """
        return self.__id

    def handleKeyEvent(self, event):
        """
        Override this method in subclasses to handle key events.
        :param event: The key event to handle.
        """
        pass

    def activate(self):
        """
        Activate the state.
        This method should only be called when the state is not already active.
        """
        if self.__isActive:
            LOG_DEBUG_DEV_BOOTCAMP('State.activate: state is already active')
            return
        self.__isActive = True
        self._doActivate()  # Activate the state by calling the protected method.

    def deactivate(self):
        """
        Deactivate the state.
        This method should only be called when the state is currently active.
        """
        if not self.__isActive:
            LOG_DEBUG_DEV_BOOTCAMP('State.deactivate: state is already not active')
            return
        self._doDeactivate()  # Deactivate the state by calling the protected method.
        self.__isActive = False

    def onSpaceLoadCompleted(self):
        """
        Callback method called when the space has finished loading.
        """
        BigWorld
