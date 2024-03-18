# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/markers2d/markers.py

# Import necessary modules
from enum import Enum
import Event
import GUI
import Math
from gun_rotation_shared import getLocalAimPoint
from vehicle_systems.tankStructure import TankNodeNames

# Define a constant vector for hidden vehicle offset
HIDDEN_VEHICLE_OFFSET = Math.Vector3(0, 5, 0)

# Define an Enum for ReplyStateForMarker
class ReplyStateForMarker(Enum):
    CREATE_STATE = 0
    REPLIED_ME_STATE = 1
    REPLIED_ALLY_STATE = 2
    NO_ACTION = 3

# Base Marker class
class Marker(object):

    def __init__(self, markerID, active=True):
        super(Marker, self).__init__()
        # Initialize markerID, active, replyCount, isSticky, isRepliedByPlayer, isReplied, and state
        self._markerID = markerID
        self._active = active
        self._replyCount = 0
        self._isSticky = False
        self._isRepliedByPlayer = False
        self._isReplied = False
        self._state = ReplyStateForMarker.CREATE_STATE

    # Methods to get and set properties
    def getMarkerID(self):
        return self._markerID

    def isActive(self):
        return self._active

    def setActive(self, active):
        if self._active != active:
            self._active = active
            return True
        return False

    def getIsReplied(self):
        return self._isReplied

    def setIsReplied(self, value):
        self._isReplied = value

    def getIsRepliedByPlayer(self):
        return self._isRepliedByPlayer

    def setIsRepliedByPlayer(self, value):
        self._isRepliedByPlayer = value

    def setReplyCount(self, replyCount):
        self._replyCount = replyCount

    def setIsSticky(self, isSticky):
        self._isSticky = isSticky

    def setState(self, state):
        self._state = state

    def getReplyCount(self):
        return self._replyCount

    def getIsSticky(self):
        return self._isSticky

    def getState(self):
        return self._state

    def getActiveCommandID(self):
        return None

    def destroy(self):
        pass


# LocationMarker class inherits from Marker
class LocationMarker(Marker):

    def __init__(self, markerID, position, active=True, markerSymbolName=None):
        super(LocationMarker, self).__init__(markerID, active)
        # Initialize position and markerSymbolName
        self._position = position
        self._markerSymbolName = markerSymbolName

    def getPosition(self):
        return self._position

    def getMarkerSubtype(self):
        return self._markerSymbolName


# BaseMarker class inherits from Marker
class BaseMarker(Marker):

    def __init__(self, markerID, active=True, owner=''):
        super(BaseMarker, self).__init__(markerID, active)
        # Initialize activeCommandID, owningTeam, boundCheckEnabled, and isHighlighted
        self._activeCommandID = -1
        self._owningTeam = owner
        self._boundCheckEnabled = True
        self._isHighlighted = False

    def getActiveCommandID(self):
        return self._activeCommandID

    def setActiveCommandID(self, commandID):
        self._activeCommandID = commandID

    def setOwningTeam(self, owningTeam):
        self._owningTeam = owningTeam

    def getOwningTeam(self):
        return self._owningTeam

    def setBoundCheckEnabled(self, enabled):
        self._boundCheckEnabled = enabled

    def getBoundCheckEnabled(self):
        return self._boundCheckEnabled


# VehicleMarker class inherits from Marker
class VehicleMarker(Marker):

    def __init__(self, markerID, vehicleID, vProxy=None, active=True, isPlayerTeam=False):
        super(VehicleMarker, self).__init__(markerID, active)
        # Initialize vehicleID, vProxy, speaking, isActionMarkerActive, isPlayerTeam, and actionState
        self._vehicleID = vehicleID
        self._vProxy = vProxy
        self._speaking = False
        self._isActionMarkerActive = False
        self._isPlayerTeam = isPlayerTeam
        self._actionState = ''
        if self._vProxy is not None:
            self.attach(vProxy)
        self.onVehicleModelChanged = Event.Event()

    # Methods to attach, detach, and destroy the vehicle marker
    def attach(self, vProxy):
        self.detach()
        self._vProxy = vProxy
        if self._vProxy.appearance is not None:
            self._vProxy.appearance.onModelChanged += self.__onModelChanged

    def detach(self):
        if self._vProxy is not None and hasattr(self._vProxy, 'appearance'):
            if self._vProxy.appearance is not None:
                self._vProxy.appearance.onModelChanged -= self.__onModelChanged
                self._vProxy = None

    def destroy(self):
        self.detach()
        self.onVehicleModelChanged.clear()

    # Methods to get properties
    def getVehicleID(self):
        return self._vehicleID

    def getVehicleEntity(self):
        return self._vProxy

    def isAlive(self):
        return self._vProxy.isAlive() if self._vProxy is not None else 0

    def getHealth(self):
        return self._vProxy.health if self._vProxy is
