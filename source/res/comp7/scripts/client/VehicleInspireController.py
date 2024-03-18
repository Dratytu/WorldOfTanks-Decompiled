# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: comp7/scripts/client/VehicleInspireController.py

import typing
from helpers import fixed_dict
from script_component.DynamicScriptComponent import DynamicScriptComponent
from view_state_component import ViewStateComponentAdaptor

# A class that controls the state of a vehicle's inspiration
class VehicleInspireController(DynamicScriptComponent):

    def __init__(self):
        # Initialize the superclass
        super(VehicleInspireController, self).__init__()
        # Initialize the adaptor attribute as None
        self.__adaptor = None
        # Return after initialization
        return

    def onDestroy(self):
        # If the adaptor is not None
        if self.__adaptor is not None:
            # Destroy the adaptor
            self.__adaptor.destroy()
            # Set the adaptor to None
            self.__adaptor = None
        # Call the superclass's onDestroy method
        super(VehicleInspireController, self).onDestroy()
        # Return after destroying the adaptor
        return

    def set_isActive(self, prev):
        # If the avatar is ready
        if self._isAvatarReady:
            # Invalidate the displayed state
            self.__invalidateDisplayedState()

    def set_displayedState(self, prev):
        # If the avatar is ready
        if self._isAvatarReady:
            # Invalidate the displayed state
            self.__invalidateDisplayedState()

    def _onAvatarReady(self):
        # If the avatar is ready
        if self._isAvatarReady:
            # Invalidate the displayed state
            self.__invalidateDisplayedState()

    def __invalidateDisplayedState(self):
        # If the controller is active
        if self.isActive:
            # Get the state with time interval using the displayed state
            state = fixed_dict.getStateWithTimeInterval(self.displayedState)
            # If the adaptor is not None
            if self.__adaptor is not None:
                # Update the state of the adaptor
                self.__adaptor.updateState(state)
            # Otherwise, create a new adaptor
            else:
                self.__adaptor = ViewStateComponentAdaptor(entity=self.entity, state=state
