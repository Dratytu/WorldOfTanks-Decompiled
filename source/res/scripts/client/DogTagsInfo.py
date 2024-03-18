# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/DogTagsInfo.py

import typing  # For type checking
import BigWorld  # A module for creating and managing game worlds
import Event  # A module for managing events

# If type checking is enabled, the following types are expected:
# List[Tuple[int, int]] for usedDogTagsComponents
if typing.TYPE_CHECKING:
    from typing import List, Tuple

class DogTagsInfo(BigWorld.DynamicScriptComponent):
    """
    A class representing DogTagsInfo, a dynamic script component.
    """

    def __init__(self):
        """
        Initialize the DogTagsInfo instance.
        """
        self.__eManager = Event.EventManager()  # Create an event manager for handling events
        self.onUsedComponentsUpdated = Event.Event(self.__eManager)  # Create an event for used dog tags components update

    def onLeaveWorld(self, *args):
        """
        Clear all event listeners when leaving the world.

        :param args: Variable length argument list
        """
        self.__eManager.clear()  # Clear all event listeners

    def setSlice_usedDogTagsComponents(self, changePath, oldValue):
        """
        Update the used dog tags components and trigger an event with new components.

        :param changePath: A tuple representing the change path
        :type changePath: List[Tuple[int, int]]
        :param oldValue: The old value of used dog tags components
        :type oldValue: List[Any]
        """
        begin, end = changePath[0]  # Unpack the first tuple from changePath
        newComponents = self.usedDogTagsComponents[begin:end]  # Get the new components from the updated range
        self.onUsedComponentsUpdated(newComponents)  # Trigger the event with new components
