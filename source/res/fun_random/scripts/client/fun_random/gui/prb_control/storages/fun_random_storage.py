# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/prb_control/storages/fun_random_storage.py

# Import necessary modules and dependencies
from fun_random_common.fun_constants import UNKNOWN_EVENT_ID
from gui.prb_control.storages.local_storage import SessionStorage
from helpers import dependency
from skeletons.gui.game_control import IFunRandomController

# Define the FunRandomStorage class, which inherits from SessionStorage
class FunRandomStorage(SessionStorage):
    # Use dependency injection to get an instance of IFunRandomController
    __funRandomController = dependency.descriptor(IFunRandomController)

    def isModeSelected(self):
        # Get the desired sub-mode from the controller
        desiredSubMode = self.__funRandomController.subModesHolder.getDesiredSubMode()
        
        # Check if the desired sub-mode is available
        isSelected = desiredSubMode is not None and desiredSubMode.isAvailable()
        
        # Get the sub-mode ID based on the selection
        desiredSubModeID = desiredSubMode.getSubModeID() if isSelected else UNKNOWN_EVENT_ID
        
        # Set the desired sub-mode ID in the controller
        self.__funRandomController.setDesiredSubModeID(desiredSubModeID)
        
        # Return the selection status
        return isSelected

