# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/ClientSelectableRankedObject.py

# Import necessary modules
from ClientSelectableObject import ClientSelectableObject
from helpers import dependency
from skeletons.gui.game_control import IRankedBattlesController

# Define the ClientSelectableRankedObject class, which inherits from ClientSelectableObject
class ClientSelectableRankedObject(ClientSelectableObject):
    
    # Use dependency injection to get an instance of IRankedBattlesController
    __rankedController = dependency.descriptor(IRankedBattlesController)

    # onEnterWorld method is called when the object enters the world
    def onEnterWorld(self, prereqs):
        # Call the superclass's onEnterWorld method
        super(ClientSelectableRankedObject, self).onEnterWorld(prereqs)
        
        # Register the __onGameModeStatusUpdate method as a callback for onGameModeStatusUpdated event
        self.__rankedController.onGameModeStatusUpdated += self.__onGameModeStatusUpdate
        
        # Call the __onGameModeStatusUpdate method to update the object's state
        self.__onGameModeStatusUpdate()

    # onLeaveWorld method is called when the object leaves the world
    def onLeaveWorld(self):
        # Unregister the __onGameModeStatusUpdate method as a callback for onGameModeStatusUpdated event
        self.__rankedController.onGameModeStatusUpdated -= self.__onGameModeStatusUpdate
        
        # Call the superclass's onLeaveWorld method
        super(ClientSelectableRankedObject, self).onLeaveWorld()

    # onMouseClick method is called when the object is clicked
    def onMouseClick(self):
        # Call the superclass's onMouseClick method
        super(ClientSelectableRankedObject, self).onMouseClick()
        
        # Call the doActionOnEntryPointClick method of IRankedBattlesController
        self.__rankedController.doActionOnEntryPointClick()

    # __onGameModeStatusUpdate method is called when the game mode status is updated
    def __onGameModeStatusUpdate(self, *_):
        # Get the current status of the ranked battles controller
        isEnabled = self.__rankedController.isEnabled()
        hasCur
