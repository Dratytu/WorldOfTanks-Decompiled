# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/avatar_components/triggers_controller.py

import Event  # Importing the Event module to create and handle events

class TriggersController(object):
    """
    A class representing a Triggers Controller that manages trigger events.
    """

    def __init__(self):
        """
        Initialize the TriggersController instance.
        """
        self.__enabled = False  # A flag to track if the controller is enabled
        self.onTrigger = Event.Event()  # An Event object to handle trigger events

    def onBecomePlayer(self):
        """
        Enable the controller when the avatar becomes a player.
        """
        self.__enabled = True

    def onBecomeNonPlayer(self):
        """
        Disable the controller when the avatar becomes a non-player.
        """
        self.__enabled = False

    def externalTrigger(self, eventId, extra):
        """
        Trigger an external event if the controller is enabled.

        :param eventId: The ID of the event to trigger
        :param extra: Additional data to pass to the event
        """
        if not self.__enabled:
            return
        self.onTrigger(eventId, extra)

    def handleKey(self, isDown, key, mods):
        """
        A placeholder function to handle key events.

        :param isDown: A boolean indicating if the key is pressed or released
        :param key: The key that was pressed or released
        :param mods: Any modifier keys (e.g., shift, control) that were also pressed
        """
        pass
