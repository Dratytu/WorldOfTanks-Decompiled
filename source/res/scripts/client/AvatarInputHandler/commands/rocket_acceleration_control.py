# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/AvatarInputHandler/commands/rocket_acceleration_control.py

import BigWorld  # Import the BigWorld module for accessing player's vehicle
import CommandMapping  # Import CommandMapping for handling input commands

from AvatarInputHandler.commands.input_handler_command import InputHandlerCommand  # Import InputHandlerCommand for inheritance

class RocketAccelerationControl(InputHandlerCommand):  # Define a class for handling rocket acceleration control

    def handleKeyEvent(self, isDown, key, mods, event=None):
        """
        Handle key events for rocket acceleration control.

        :param isDown: A boolean indicating whether the key is pressed down or released.
        :param key: The key being pressed or released.
        :param mods: Modifier keys (e.g., shift, control, etc.) being pressed.
        :param event: The key event object.
        :return: False if the key event is not captured, True otherwise.
        """
        cmdMap = CommandMapping.g_instance  # Get the CommandMapping instance
        keyCaptured = cmdMap.isFired(CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION, key) and isDown
        # Check if the key event is for the autorotation command and the key is pressed down

        if not keyCaptured:
            return False  # Return False if the key event is not captured
        else:
            vehicle = BigWorld.player().getVehicleAttached()
            # Get the player's attached vehicle

            if vehicle is not None and vehicle.isPlayerVehicle and vehicle.isAlive():
                self.__activateRocketAcceleration(vehicle)
                # If the vehicle exists, is a player's vehicle, and is alive, activate rocket acceleration

            return True  # Return True to indicate the key event is captured

    def __activateRocketAcceleration(self, vehicle):
        """
        Activate the rocket
