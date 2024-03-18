# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/AvatarInputHandler/PostmortemDelay.py

import math
import BigWorld
import Math
import math_utils
from AvatarInputHandler.DynamicCameras.ArcadeCamera import ArcadeCamera
from PlayerEvents import g_playerEvents
from constants import ARENA_PERIOD
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_DEBUG

# Class representing the postmortem delay functionality
class PostmortemDelay(object):
    # Class variables
    FADE_DELAY_TIME = 2.0  # Time for which the screen will fade after death
    KILLER_VISION_TIME = 5.0  # Time for which the killer's vision will be shown
    KILLER_VEHICLE_CAMERA_DISTANCE = 15.0  # Distance of the camera from the killer's vehicle
    KILLER_VEHICLE_CAMERA_PIVOT_SETTINGS = (1.5, 3.0)  # Pivot settings for the camera when viewing the killer's vehicle
    KILLER_VEHICLE_PITCH_OFFSET = -0.3  # Pitch offset for the camera when viewing the killer's vehicle

    def __init__(self, arcadeCamera, onKillerVisionStart, onStop, initialDelay=0, enableKillerVision=True):
        # Initialize the PostmortemDelay class
        # arcadeCamera: ArcadeCamera instance for controlling the camera
        # onKillerVisionStart: Callback function to be called when killer vision starts
        # onStop: Callback function to be called when postmortem delay is stopped
        # initialDelay: Initial delay before the postmortem delay starts
        # enableKillerVision: Flag to enable/disable killer vision

        # Variables
        self.__killerVehicleID = None  # ID of the killer's vehicle
        self.__bActive = False  # Flag to check if the postmortem delay is active
        self.__mouseInputEnabled = False  # Flag to enable/disable mouse input
        self.__bChoiceWindowActive = False  # Flag to check if the choice window is active
        self.__bFadeScreenActive = False  # Flag to check if the screen fade is active
        self.__bKillerVisionActive = False  # Flag to check if killer vision is active
        self.__savedPivotSettings = None  # Saved pivot settings for the camera
        self.__savedCameraDistance = None  # Saved camera distance for the camera
        self.__savedYawPitch = None  # Saved yaw and pitch for the camera
        self.__arcadeCamera = arcadeCamera  # ArcadeCamera instance
        self.__onKillerVisionStart = onKillerVisionStart  # Callback function to be called when killer vision starts
        self.__onStop = onStop  # Callback function to be called when postmortem delay is stopped
        self.__cbIDWait = None  # Callback ID for the wait callback
        self.__initialDelay = initialDelay  # Initial delay before the postmortem delay starts
        self.__enableKillerVision = enableKillerVision  # Flag to enable/disable killer vision

        # Event handlers
        BigWorld.player().onVehicleLeaveWorld += self.__onVehicleLeaveWorld  # Event handler for when the player's vehicle leaves the world
        g_playerEvents.onArenaPeriodChange += self.__onRoundFinished  # Event handler for when the arena period changes

    def destroy(self):
        # Destroy the PostmortemDelay class
        self.stop()
        self.__arcadeCamera = None  # Reset the ArcadeCamera instance
        self.__onKillerVisionStart = None  # Reset the callback function to be called when killer vision starts
        self.__onStop = None  # Reset the callback function to be called when postmortem delay is stopped
        BigWorld.player().onVehicleLeaveWorld -= self.__onVehicleLeaveWorld  # Remove the event handler for when the player's vehicle leaves the world
        g_playerEvents.onArenaPeriodChange -= self.__onRoundFinished  # Remove the event handler for when the arena period changes

    def start(self):
        # Start the postmortem delay
        if self.__bActive:
            return
        self.__bActive = True
        self.__fadeScreen()  # Fade the screen
        self.__moveCameraTo(BigWorld.player().playerVehicleID)  # Move the camera to the player's vehicle
        fadeDelay = self.FADE_DELAY_TIME + self.__initialDelay  # Calculate the delay before the postmortem delay starts
        self.__cbIDWait = BigWorld.callback(fadeDelay, self.__onFadeDelay)  # Wait for the calculated delay

    def stop(self):
        # Stop the postmortem delay
        if not self.__bActive:
            return
        else:
            self.__cancelWait()  # Cancel the wait callback
            self.__showChoiceWindow(False)  # Hide the choice window
            self.__fadeScreen(bFade=False)  # Stop fading the screen
            self.__bKillerVisionActive = False  # Reset the killer vision flag
            self.__mouseInputEnabled = False  # Reset the mouse input flag

            # Reset the camera settings
            try:
                self.__moveCameraTo(BigWorld.player().playerVehicleID)
            except Exception:
                pass

            self.__killerVehicleID = None  # Reset the killer's vehicle ID
            self.__savedPivotSettings = None  # Reset the saved pivot settings
            self.__savedCameraDistance = None  # Reset the saved camera distance
            self.__savedYawPitch = None  # Reset the saved yaw and pitch
            self.__bActive = False  # Reset the active flag
            try:
                self.__onStop()  # Call the callback function to be called when postmortem delay is stopped
            except Exception:
                LOG_CURRENT_EXCEPTION()

            return

    def handleMouseEvent(self, dx, dy, dz):
        # Handle mouse events during the postmortem delay
        if self.__bActive
