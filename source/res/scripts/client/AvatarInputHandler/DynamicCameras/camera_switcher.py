# Python bytecode 2.7 (decompiled from Python 2.7)

# Embedded file name: scripts/client/AvatarInputHandler/DynamicCameras/camera_switcher.py

import time
import typing
from enum import Enum
import BigWorld
import math_utils

# Enum for different switch types
class SwitchTypes(Enum):
    FROM_MAX_DIST = 0
    FROM_MIN_DIST = 1
    FROM_TRANSITION_DIST_AS_MAX = 2
    FROM_TRANSITION_DIST_AS_MIN = 3

# Enum for switch to places
class SwitchToPlaces(Enum):
    TO_RELATIVE_POS = 0
    TO_TRANSITION_DIST = 1
    TO_NEAR_POS = 2

# Transition distance hysteresis value
TRANSITION_DIST_HYSTERESIS = 0.01

# Camera switcher class
class CameraSwitcher(object):
    __slots__ = ('__switchType', '__switchToName', '__switchToPos', '__lastDist', '__intervalToSwitch', '__lastScrollTime', '__hasTimeout', '__timeoutCallback', '__timeoutTime', '__transitionValue', '__switchToPlaceType')

    def __init__(self, switchType, switchToName, switchToPos, intervalToSwitch=_INTERVAL_TO_SWITCH, timeoutTime=_TIMEOUT_TIME):
        """
        Initialize the camera switcher object with switch type, switch to name, switch to position, interval to switch, and timeout time.
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
        """
        return (self.__switchToName, self.__switchToPos, self.__switchToPlaceType)

    def needToSwitch(self, zValue, dist, minValue, maxValue, transitionValue=None):
        """
        Check if the switcher needs to switch.
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
        Set the timeout.
        """
        self.__hasTimeout = False
        self.__timeoutCallback = None

    def __switchFromDist(self, zValue, dist, value):
        """
        Switch from distance.
        """
        currentScrollInterval = None
        if zValue != 0:
            currentTime = time.time()
            currentScrollInterval = currentTime - self.__lastScrollTime
            self.__lastScrollTime = currentTime
        if self.__lastDist == dist:
            isEqual = math_utils.almostZero(value - dist)
            if isEqual and self.__hasTimeout is None and self.__timeoutTime:
                self.__hasTimeout = True
              ````
