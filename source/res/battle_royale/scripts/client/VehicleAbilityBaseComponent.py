# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/VehicleAbilityBaseComponent.py

import BigWorld
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID
from Event import EventsSubscriber

class VehicleAbilityBaseComponent(BigWorld.DynamicScriptComponent):

    def __init__(self, timerViewID=None, markerID=None):
        # Initialize the component with optional timerViewID and markerID
        super(VehicleAbilityBaseComponent, self).__init__()
        self._guiSessionProvider = self.entity.guiSessionProvider
        self._guiFeedback = self.entity.guiSessionProvider.shared.feedback
        self._finishTime = self.finishTime  # Finish time for the ability
        self._timerViewID = timerViewID  # ID for the timer visual component
        self._markerID = markerID  # ID for the marker visual component
        self._es = EventsSubscriber()  # Event subscriber for handling events
        self.__postponedCalls = []  # List for storing postponed function calls
        self.__isSwitching = False  # Flag for checking if the view is switching
        self._avatar = BigWorld.player()  # The local player avatar
        self._subscribeOnEvents()  # Subscribe to relevant events
        self._updateVisuals()  # Update visual components initially

    def set_finishTime(self, _=None):
        # Setter for finishTime, updates visual components
        self._finishTime = self.finishTime
        self._updateVisuals()

    def onDestroy(self):
        # Called when the component is destroyed, cleans up resources
        self._destroy()

    def onLeaveWorld(self, *args):
        # Called when the entity leaves the game world, cleans up resources
        self._destroy()

    def getInfo(self):
        # Returns an empty dictionary, not used in this script
        return {}

    def _onAvatarReady(self):
        # Called when the avatar is ready, not used in this script
        pass

    def _subscribeOnEvents(self):
        # Subscribes to relevant events for the component
        self._es.subscribeToEvent(self._guiSessionProvider.onUpdateObservedVehicleData, self._onUpdateObservedVehicleData)
        self._es.subscribeToEvent(self.entity.onAppearanceReady, self._onAppearanceReady)
        if self._avatar is not None and self._avatar.inputHandler is not None:
            self._es.subscribeToEvent(self._avatar.inputHandler.onCameraChanged, self.__onCameraChanged)
            self._es.subscribeToEvent(self._avatar.onSwitchingViewPoint, self.__onSwitchingViewPoint)
        return

    def _unSubscribeFromAllEvents(self):
        # Unsubscribes from all subscribed events
        self._es.unsubscribeFromAllEvents()

    def _destroy(self):
        # Clean up resources when the component is destroyed
        self._unSubscribeFromAllEvents()
        self.__isSwitching = False
        self._updateVisuals(isShow=False)
        self.__postponedCalls = []
        self._avatar = None
        return

    def _updateVisuals(self, isShow=True):
        # Update visual components like the timer and marker
        self._updateTimer(self._getTimerData(isShow))
        self._updateMarker(self._getMarkerData(isShow))

    def _updateTimer(self, data):
        # Update the timer visual component
        if self._timerViewID is None:
            return
        else:
            if self.__isSwitching:
              `enter code here`                self.__pushToPostponeCall(self._updateTimer, (data,))
            elif self._canUpdateTimer():
                self._guiSessionProvider.invalidateVehicleState(self._timerViewID, data)
                self._updateMarker(self._getMarkerData(isShow=False), isHide=True)
            return

    def _canUpdateTimer(self):
        # Check if the timer can be updated based on the current camera mode and vehicle
        modeName = self._avatar.inputHandler.ctrlModeName
        return True if self.entity.id == self._avatar.inputHandler.ctrl.curVehicleID and modeName != 'video' else False

    def _updateMarker(self, data, isHide=False):
        # Update the marker visual component
        if self._markerID is None:
            return
        else:
            if self.__isSwitching:
                self.__pushToPostponeCall(self._updateMarker, (data, isHide))
            else:
                modeName = self._avatar.inputHandler.ctrlModeName
                if self.entity.id != self._avatar.inputHandler.ctrl.curVehicleID or isHide or modeName == 'video':
                    self._guiFeedback.onVehicleFeedbackReceived(FEEDBACK_EVENT_ID.VEHICLE_CUSTOM_MARKER, self.entity.id, data)
            return

    def _getTimerData(self, isShow=True):
        # Prepare data for updating the timer visual component
        data = {'duration': self._getDuration() if isShow else 0.0,
         'endTime': self._finishTime}
        return data

    def _getMarkerData(self, isShow=True):
        # Prepare data for updating the marker visual component
        data = {'isShown': isShow,
         'isSourceVehicle': True,
         'duration': self._getDuration() if isShow else 0.0,
         'animated': True,
         'markerID': self._markerID}
        return data

    def _getDuration(self):
        # Calculate the remaining duration for the ability
        return self._finishTime - BigWorld.serverTime
