# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/AvatarInputHandler/commands/prebattle_setups_control.py

# Importing CommandMapping for command mapping functionality
import CommandMapping

# Importing InputHandlerCommand as the base command class for PrebattleSetupsControl
from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand

# Importing event_dispatcher from gui.battle_control to handle prebattle setup events
from gui.battle_control import event_dispatcher

# Predefined command list for prebattle setup shortcuts
_SETUP_CMDS = (CommandMapping.CMD_AMMUNITION_SHORTCUT_SWITCH_SETUP_1, CommandMapping.CMD_AMMUNITION_SHORTCUT_SWITCH_SETUP_2)

class PrebattleSetupsControl(InputHandlerCommand):
    """
    PrebattleSetupsControl class that inherits from InputHandlerCommand to handle prebattle setup key events.
    """

    def handleKeyEvent(self, isDown, key, mods, event=None):
        """
        handleKeyEvent method to process key events and change ammunition setups if necessary.

        :param isDown: Boolean value indicating whether the key is pressed down or released
        :param key: The key being processed
        :param mods: Modifier keys (e.g., shift, control, etc.)
        :param event: The event object (optional)
        :return: True if the key event is handled, False otherwise
        """

        # Check if the fired command list contains the current key and if the key is pressed down
        if CommandMapping.g_instance.isFiredList(_SETUP_CMDS, key) and isDown:
            # Change the ammunition setup based on the key
            event_dispatcher.changeAmmunitionSetup(key)
            # Return True to indicate the key event is handled
            return True

        # If the key event is not handled, return False
        return False
``
