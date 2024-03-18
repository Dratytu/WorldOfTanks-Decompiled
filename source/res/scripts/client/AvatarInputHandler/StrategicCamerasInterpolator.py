# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/AvatarInputHandler/StrategicCamerasInterpolator.py

import BigWorld  # Import BigWorld library for managing game cameras
import Math  # Import Math library for matrix operations
import math_utils  # Import math_utils library for mathematical functions
from Event import EventManager, Event  # Import EventManager and Event classes for event handling
from helpers.CallbackDelayer import CallbackDelayer  # Import CallbackDelayer helper class

_EASING_METHOD = math_utils.easeInOutQuad  # Define easing method for interpolation
_INTERPOLATION_TIME = 0.2  # Define the total time for interpolation

class StrategicCamerasInterpolator(CallbackDelayer):
    """
    A class for interpolating between two camera states with optional FOV change.
    """

    def __init__(self):
        """
        Initialize the StrategicCamerasInterpolator with default parameters.
        """
        CallbackDelayer.__init__(self)
        self.__totalInterpolationTime = max(0.01, _INTERPOLATION_TIME)  # Set the total interpolation time
        self.__elapsedTime = 0.0  # Initialize elapsed time
        self.__easingMethod = _EASING_METHOD  # Set the easing method
        self.__prevTime = 0.0  # Initialize previous time
        self.__initialState = None  # Initialize initial state
        self.__finalState = None  # Initialize final state
        self.__initialFov = 0.0  # Initialize initial field of view
        self.__finalFov = 0.0  # Initialize final field of view
        self.__cam = None  # Initialize camera
        self._eventManager = EventManager()  # Initialize event manager
        self.onInterpolationStart = Event(self._eventManager)  # Create an event for interpolation start
        self.onInterpolationStop = Event(self._eventManager)  # Create an event for interpolation stop

    def destroy(self):
        """
        Clean up resources when the object is destroyed.
        """
        self._eventManager.clear()  # Clear all events
        super(StrategicCamerasInterpolator, self).destroy()  # Call the parent class's destroy method

    def enable(self, initialState, finalState, initialFov, finalFov):
        """
        Enable interpolation between two camera states with optional FOV change.
        :param initialState: The initial camera state
        :param finalState: The final camera state
        :param initialFov: The initial field of view
        :param finalFov: The final field of view
        """
        self.__prevTime = BigWorld.timeExact()  # Set the previous time
        if self.__elapsedTime > 0.0:
            self.__elapsedTime = self.__totalInterpolationTime - self.__elapsedTime  # Calculate remaining time
        self.__initialState = initialState  # Set the initial state
        self.__finalState = finalState  # Set the final state
        self.__initialFov = initialFov  # Set the initial field of view
        self.__finalFov = finalFov  # Set the final field of view
        self.__setupCamera()  # Set up the camera
        self.__cameraUpdate()  # Update the camera
        self.onInterpolationStart()  # Trigger the interpolation start event
        self.delayCallback(0.0, self.__cameraUpdate)  # Schedule the next camera update

    def __setupCamera(self):
        """
        Set up the camera with the given parameters.
        """
        if self.__cam is None:
            self.__cam = BigWorld.CursorCamera()  # Create a new camera
        self.__cam.target = math_utils.MatrixProviders.product(self.__finalState.target.a, Math.Matrix())  # Set the target
        self.__cam.source = Math.Matrix()  # Set the source
        self.__cam.pivotMaxDist = 0.0  # Set the pivot maximum distance
        self.__cam.maxDistHalfLife = 0.01  # Set the maximum distance half-life
        self.__cam.movementHalfLife = 0.0  # Set the movement half-life
        self.__cam.turningHalfLife = -1  # Set the turning half-life
        self.__cam.pivotPosition = self.__initialState.pivotPosition  # Set the pivot position
        self.__cam.forceUpdate()  # Force the camera to update
        BigWorld.camera(self.__cam)  # Set the camera
        BigWorld.projection().fov = self.__initialFov  # Set the initial field of view
        return

    def disable(self):
        """
        Disable interpolation and reset camera parameters.
        """
        self.__elapsedTime = 0.0  # Reset elapsed time
        self.stopCallback(self.__cameraUpdate)  # Stop the camera update callback
        self.stopCallback(self.disable)  # Stop the disable callback
        BigWorld.camera(self.__finalState)  # Set the final state as the camera
        self.__initialState = None  # Reset the initial state
        self.__finalState = None  # Reset the final state
        self.__cam = None  # Reset the camera
        self.onInterpolationStop()  # Trigger the interpolation stop event
        return

    def __cameraUpdate(self):
        """
        Update the camera with interpolated parameters.
        """
        currentTime = BigWorld.timeExact()  # Get the current time
        self.__elapsedTime += currentTime - self.__prevTime  # Calculate elapsed time
        self.__prevTime = currentTime  # Set the previous time
        interpolationCoefficient = self.__easingMethod(self.__elapsedTime, 1.0, self.__totalInterpolationTime)  # Calculate interpolation coefficient
        interpolationCoefficient = math_utils.clamp(0.0, 1.0, interpolationCoefficient)  # Clamp the interpolation coefficient

        # Interpolate camera parameters
        iSource = self.__initialState.source
        iTarget = self.__initialState.target.b.translation
       
