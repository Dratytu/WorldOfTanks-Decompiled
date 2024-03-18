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
    FADE_DELAY_TIME = 2.0  # Time for which the screen should fade after death
    KILLER_VISION_TIME = 5.0  # Time for which the killer's vision should be shown
    KILLER_VEHICLE_CAMERA_DISTANCE = 15.0  # Distance of the camera from the killer's vehicle
    KILLER_VEHICLE_CAMERA_PIVOT_SETTINGS = (1.5, 3.0)  # Pivot settings for the camera when viewing the killer's vehicle
    KILLER_VEHICLE_PITCH_OFFSET = -0.3  # Pitch offset for the camera when viewing the killer's vehicle

    def __init__(self, arcadeCamera, onKillerVisionStart, onStop, initialDelay=0, enableKillerVision=True):
        # Initialize the PostmortemDelay class
        # arcadeCamera: The ArcadeCamera instance for controlling the camera
        # onKillerVisionStart: Callback function to be called when killer vision starts
        # onStop: Callback function to be called when the postmortem delay ends
        # initialDelay: Initial delay before the postmortem delay starts
        # enableKillerVision: Flag to enable/disable killer vision

        # Variables to store the state of the postmortem delay
        self.__killerVehicleID = None  # ID of the killer's vehicle
        self.__bActive = False  # Flag to check if the postmortem delay is active
        self.__mouseInputEnabled = False  # Flag to enable/disable mouse input
        self.__bChoiceWindowActive = False  # Flag to check if the choice window is active
        self.__bFadeScreenActive = False  # Flag to check if the screen is fading
        self.__bKillerVisionActive = False  # Flag to check if killer vision is active

        # Variables to store the saved camera settings
        self.__savedPivotSettings = None
        self.__savedCameraDistance = None
        self.__savedYawPitch = None

        # Assign the input parameters to class variables
        self.__arcadeCamera = arcadeCamera
        self.__onKillerVisionStart = onKillerVisionStart
        self.__onStop = onStop
        self.__cbIDWait = None
        self.__initialDelay = initialDelay
        self.__enableKillerVision = enableKillerVision

        # Register event handlers
        BigWorld.player().onVehicleLeaveWorld += self.__onVehicleLeaveWorld
        g_playerEvents.onArenaPeriodChange += self.__onRoundFinished

    def destroy(self):
        # Clean up the PostmortemDelay class
        self.stop()
        self.__arcadeCamera = None
        self.__onKillerVisionStart = None
        self.__onStop = None
        BigWorld.player().onVehicleLeaveWorld -= self.__onVehicleLeaveWorld
        g_playerEvents.onArenaPeriodChange -= self.__onRoundFinished

    def start(self):
        # Start the postmortem delay
        if self.__bActive:
            return
        self.__bActive = True
        self.__fadeScreen()
        self.__moveCameraTo(BigWorld.player().playerVehicleID)
        fadeDelay = self.FADE_DELAY_TIME + self.__initialDelay
        self.__cbIDWait = BigWorld.callback(fadeDelay, self.__onFadeDelay)

    def stop(self):
        # Stop the postmortem delay
        if not self.__bActive:
            return
        else:
            self.__cancelWait()
            self.__showChoiceWindow(False)
            self.__fadeScreen(bFade=False)
            self.__bKillerVisionActive = False
            self.__mouseInputEnabled = False
            try:
                self.__moveCameraTo(BigWorld.player().playerVehicleID)
            except Exception:
                pass

            self.__killerVehicleID = None
            self.__savedPivotSettings = None
            self.__savedCameraDistance = None
            self.__savedYawPitch = None
            self.__bActive = False
            try:
                self.__onStop()
            except Exception:
                LOG_CURRENT_EXCEPTION()

            return

    def handleMouseEvent(self, dx, dy, dz):
        # Handle mouse events during the postmortem delay
        if self.__bActive and self.__mouseInputEnabled:
            self.__arcadeCamera.update(dx, dy, math_utils.clamp(-1, 1, dz))

    def __fadeScreen(self, bFade=True):
        # Fade the screen in/out
        if self.__bFadeScreenActive == bFade:
            return
        self.__bFadeScreenActive = bFade
        if bFade:
            pass  # Implement screen fading
        else:
            pass  # Implement screen unfading

    def __showChoiceWindow(self, bShow=True):
        # Show/hide the choice window
        if self.__bChoiceWindowActive == bShow:
            return
        self.__bChoiceWindowActive = bShow
        if bShow:
            self.__onContinueBattle()
        else:
            self.__onCancelBattle()

    def __moveCameraTo(self, vehicleID, sourceVehicleID=None):
        # Move the camera to the specified vehicle
        vehicle = BigWorld.entity(vehicleID)
        if vehicle is None:
            if vehicleID == BigWorld.player().playerVehicleID:
                steadyMatrix = BigWorld.player().inputHandler.steady
