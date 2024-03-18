# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/avatar_components/visual_script_controller.py

import cPickle
import VSE

class VisualScriptController(object):
    """
    A class that handles visual script events for an avatar.
    """

    def __init__(self):
        """
        Initializes the VisualScriptController instance.
        """
        self.__enabled = False

    def onBecomePlayer(self):
        """
        Enables visual script handling when the avatar becomes a player.
        """
        self.__enabled = True

    def onBecomeNonPlayer(self):
        """
        Disables visual script handling when the avatar becomes a non-player.
        """
        self.__enabled = False

    def handleKey(self, isDown, key, mods):
        """
        Handles key events, but does not process them in this example.

        :param isDown: A boolean indicating whether the key is pressed down.
        :param key: The key being pressed.
        :param mods: Any modifier keys being pressed.
        """
        pass

    def handleScriptEventFromServer(self, eventName, planName, params, targetAspects, eventScope):
        """
        Handles visual script events received from the server.

        :param eventName: The name of the event.
        :param planName: The name of the plan associated with the event.
        :param params: The serialized parameters of the event.
        :param targetAspects: The aspects of the target affected by the event.
        :param eventScope: The scope of the event.
        """
        if self.__enabled:
            # If the controller is enabled, process the event.
            if eventScope.startswith('ArenaT:') and self.arena is not None:
                # If the event scope is related to an arena, update the scope
                # with the unique arena ID if the arena is available.
                eventScope = 'ArenaT:' +
