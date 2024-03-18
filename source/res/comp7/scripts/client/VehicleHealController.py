# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: comp7/scripts/client/VehicleHealController.py

import typing
from helpers import fixed_dict
from script_component.DynamicScriptComponent import DynamicScriptComponent
from view_state_component import ViewStateComponentAdaptor

# A class representing a vehicle heal controller
class VehicleHealController(DynamicScriptComponent):

    def __init__(self):
        # Initialize the superclass
        super(VehicleHealController, self).__init__()
        # Initialize an empty dictionary to store adaptors
        self.__adaptors = {}

    # Called when the object is about to be destroyed
    def onDestroy(self):
        # Iterate over all adaptors and destroy them
        for adaptor in self.__adaptors.itervalues():
            adaptor.destroy()

        # Clear the dictionary of adaptors
        self.__adaptors.clear()
        # Call the onDestroy method of the superclass
        super(VehicleHealController, self).onDestroy()

    # Called when the displayed states are set
    def set_displayedStates(self, prev):
        # If the avatar is ready
        if self._isAvatarReady:
            # Invalidate the displayed states
            self.__invalidateDisplayedStates()

    # Called when the avatar is ready
    def _onAvatarReady(self):
        # Invalidate the displayed states
        self.__invalidateDisplayedStates()

    # Invalidate the displayed states
    def __invalidateDisplayedStates(self):
        # Initialize a set to store the removed states
        removedStates = set(self.__adaptors)
        # Iterate over all displayed states
        for stateDict in self.displayedStates:
            # Get the state with time interval from the state dictionary
            state = fixed_dict.getStateWithTimeInterval(stateDict)
            # Get the state ID from the state
            stateID = state.stateID
            # If the state ID is in the adaptors
            if stateID in self.__adaptors:
                # Update the state of the adaptor
                self.__adaptors[stateID].updateState(state)
                # Remove the state ID from the removed states
                removedStates.remove(stateID)
            # Create a new adaptor for the state
            self.__ad
