# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/PoiCaptureBlockerComponent.py

import logging
import typing

# Importing PoiBaseComponent from PoiBaseComponent.py file
from PoiBaseComponent import PoiBaseComponent

# Importing PoiCaptureBlockerStateComponent from points_of_interest_components.py file
from points_of_interest.components import PoiCaptureBlockerStateComponent

# Importing PoiBlockReasons from points_of_interest_shared.py file
from points_of_interest_shared import PoiBlockReasons

# Creating a logger with the name of the current module
_logger = logging.getLogger(__name__)

# Defining the PoiCaptureBlockerComponent class that inherits from PoiBaseComponent
class PoiCaptureBlockerComponent(PoiBaseComponent):

    # Initializing the class with no arguments
    def __init__(self):
        # Calling the constructor of the parent class
        super(PoiCaptureBlockerComponent, self).__init__()

        # Initializing the stateComponent attribute to None
        self.__stateComponent = None

    # onDestroy method is called when the object is about to be destroyed
    def onDestroy(self):
        # Checking if the poiGameObject attribute is not None and is valid
        if self._poiGameObject is not None and self._poiGameObject.isValid():
            # Removing the stateComponent from the poiGameObject
            self._poiGameObject.removeComponent(self.__stateComponent)

        # Setting the stateComponent attribute to None
        self.__stateComponent = None

        # Calling the onDestroy method of the parent class
        super(PoiCaptureBlockerComponent, self).onDestroy()

        return

    # The set_blockReasons method sets the blockReasons attribute
    def set_blockReasons(self, prev):
        # Checking if the stateComponent attribute is not None
        if self.__stateComponent is not None:
            # Setting the blockReasons attribute of the stateComponent to the value returned by the __getBlockReasons method
            self.__stateComponent.blockReasons = self.__getBlockReasons()

        return

    # The _onAvatarReady method is called when the avatar is ready
    def _onAvatarReady(self):
        # Checking if the poiGameObject attribute is not None and is valid
        if self._poiGameObject is not None and self._
