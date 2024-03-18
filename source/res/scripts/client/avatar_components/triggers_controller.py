# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/avatar_components/triggers_controller.py

import Event  # Importing the Event module to create and handle events

class TriggersController(object):
    """
    A class representing a Triggers Controller that manages trigger events.
    This class is responsible for enabling and disabling trigger events,
    as well as handling external triggers and key events.
    """

    def __init__(self):
        """
        Initialize the TriggersController instance.
        Set the enabled flag to False and create an Event object to handle trigger events.
        """
        self.__enabled = False  # A flag to track if the controller is enabled
        self.onTrigger = Event.Event()  # An Event object to handle trigger events

    def onBecomePlayer(self):
        """
        Enable the controller when the avatar becomes a player.
        Set the enabled flag to True to allow trigger events to be processed.
        """
        self.__enabled = True  # Enable the controller

    def onBecomeNonPlayer(self):
        """
        Disable the controller when the avatar becomes a non-player.
        Set the enabled flag to False to prevent trigger events from being processed.
        """
        self.__enabled = False  # Disable the controller

    def externalTrigger(self, eventId, extra):
        """
        Trigger an external event if the controller is enabled.

        :param eventId: The ID of the event to trigger
        :param extra: Additional data to pass to the event
        If the controller is enabled, trigger the onTrigger event with the given event ID and extra data.
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
        This function currently does not do anything. It can be overridden to handle key events.
        """
        pass
