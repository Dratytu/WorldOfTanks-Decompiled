# Python bytecode 2.7 (decompiled from Python 2.7)

# Embedded file name: scripts/client/AvatarInputHandler/DynamicCameras/camera_switcher.py

import time
import typing
from enum import Enum
import BigWorld
import math_utils

# Enum for different switch types
class SwitchTypes(Enum):
    """
    Enum for different switch types.
    """
    FROM_MAX_DIST = 0
    FROM_MIN_DIST = 1
    FROM_TRANSITION_DIST_AS_MAX = 2
    FROM_TRANSITION_DIST_AS_MIN = 3

# Enum for switch to places
class SwitchToPlaces(Enum):
    """
    Enum for switch to places.
    """
    TO_RELATIVE_POS = 0
    TO_TRANSITION_DIST = 1
    TO_NEAR_POS = 2

# Transition distance hysteresis value
TRANSITION_DIST_HYSTERESIS = 0.01

# Camera switcher class
class CameraSwitcher(object):
    """
    Camera switcher class.
    """
    __slots__ = ('__switchType', '__switchToName', '__switchToPos', '__lastDist', '__intervalToSwitch', '__lastScrollTime', '__hasTimeout', '__timeoutCallback', '__timeoutTime', '__transitionValue', '__switchToPlaceType')

    def __init__(self, switchType, switchToName, switchToPos, intervalToSwitch=_INTERVAL_TO_SWITCH, timeoutTime=_TIMEOUT_TIME):
        """
        Initialize the camera switcher object with switch type, switch to name, switch to position, interval to switch, and timeout time.

        :param switchType: Switch type.
        :type switchType: SwitchTypes
        :param switchToName: Switch to name.
        :type switchToName: str
        :param switchToPos: Switch to position.
        :type switchToPos: typing.Tuple[float, float, float]
        :param intervalToSwitch: Interval to switch (optional).
        :type intervalToSwitch: float
        :param timeoutTime: Timeout time (optional).
        :type timeoutTime: float
        """
        self.__switchType = switchType
        self.__switchToName = switchToName
        self.__switchToPos = switchToPos
        self.__lastDist = None
        self.__hasTimeout = None
        self.__timeoutCallback = None
        self.__timeoutTime = timeoutTime
        self.__intervalToSwitch = intervalToSwitch
        self.__lastScrollTime = 0
        if self.__switchType in (SwitchTypes.FROM_TRANSITION_DIST_AS_MAX, SwitchTypes.FROM_TRANSITION_DIST_AS_MIN):
            self.__switchToPlaceType = SwitchToPlaces.TO_TRANSITION_DIST
        else:
            self.__switchToPlaceType = SwitchToPlaces.TO_RELATIVE_POS

    def clear(self):
        """
        Clear the switcher's state.
        """
        self.__lastDist = None
        self.__clearTimeout()

    def getSwitchParams(self):
        """
        Get the switch parameters.

        :return: Switch parameters.
        :rtype: typing.Tuple[str, typing.Tuple[float, float, float], SwitchToPlaces]
        """
        return (self.__switchToName, self.__switchToPos, self.__switchToPlaceType)

    def needToSwitch(self, zValue, dist, minValue, maxValue, transitionValue=None):
        """
        Check if the switcher needs to switch.

        :param zValue: Z value.
        :type zValue: float
        :param dist: Distance.
        :type dist: float
        :param minValue: Minimum value.
        :type minValue: float
        :param maxValue: Maximum value.
        :type maxValue: float
        :param transitionValue: Transition value (optional).
        :type transitionValue: float
        :return: Switch result.
        :rtype: bool
        """
        if transitionValue is not None:
            transMin, transMax = self.getDistLimitationForSwitch(minValue, maxValue, transitionValue)
        else:
            transMin = minValue
            transMax = maxValue
        if self.__switchType == SwitchTypes.FROM_MAX_DIST:
            result = self.__switchFromDist(zValue, dist, maxValue)
        elif self.__switchType == SwitchTypes.FROM_TRANSITION_DIST_AS_MAX:
            result = self.__switchFromDist(zValue, dist, transMax)
        elif self.__switchType == SwitchTypes.FROM_TRANSITION_DIST_AS_MIN:
            result = self.__switchFromDist(zValue, dist, transMin)
        else:
            result = self.__switchFromDist(zValue, dist, minValue)
        self.__lastDist = dist
        return result

    def getDistLimitationForSwitch(self, minValue, maxValue, transitionValue):
        """
        Get the distance limitation for switch.

        :param minValue: Minimum value.
        :type minValue: float
        :param maxValue: Maximum value.
        :type maxValue: float
        :param transitionValue: Transition value.
        :type transitionValue: float
        :return: Tuple of minimum and maximum distance limitations.
        :rtype: typing.Tuple[float, float]
        """
        resultMin = minValue
        resultMax = maxValue
        if self.__switchType == SwitchTypes.FROM_TRANSITION_DIST_AS_MIN:
            resultMin = max(transitionValue, minValue)
        elif self.__switchType == SwitchTypes.FROM_TRANSITION_DIST_AS_MAX:
            resultMax = min(maxValue, transitionValue)
        return (resultMin, resultMax)

    def __clearTimeout(self):
        """
        Clear the timeout.
        """
        if self.__timeoutCallback is not None:
            BigWorld.cancelCallback(self.__timeoutCallback)
            self.__timeoutCallback = None
        self.__hasTimeout = None

    def __setTimeout(self):
        """
       
