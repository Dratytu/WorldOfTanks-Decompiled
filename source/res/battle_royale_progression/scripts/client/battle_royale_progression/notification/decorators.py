# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale_progression/scripts/client/battle_royale_progression/notification/decorators.py

# Import necessary modules and classes
from helpers import dependency
from notification.decorators import MessageDecorator
from notification.settings import NOTIFICATION_BUTTON_STATE
from battle_royale_progression.skeletons.game_controller import IBRProgressionOnTokensController

# Define a new class BRProgressionLockButtonDecorator that inherits from MessageDecorator
class BRProgressionLockButtonDecorator(MessageDecorator):
    
    # Declare a dependency for IBRProgressionOnTokensController
    _brProgressionController = dependency.descriptor(IBRProgressionOnTokensController)

    # Initialize the class with entityID, entity, settings, and model
    def __init__(self, entityID, entity=None, settings=None, model=None):
        # Call the constructor of the parent class
        super(BRProgressionLockButtonDecorator, self).__init__(entityID, entity, settings, model)
        
        # Register a callback function to be called when the settings change
        self._brProgressionController.onSettingsChanged += self.__update

    # Define a method to clear the resources used by the class
    def clear(self):
        # Remove the callback function when the settings change
        self._brProgressionController.onSettingsChanged -= self.__update
        # Call the clear method of the parent class
        super(BRProgressionLockButtonDecorator, self).clear()

    # Define a method to create the notification entity
    def _make(self, formatted=None, settings=None):
        # Call the method to update the entity buttons
        self.__updateEntityButtons()
        # Call the _make method of the parent class
        super(BRProgressionLockButtonDecorator, self)._make(formatted, settings)

    # Define a method to update the buttons of the entity
    def __updateEntityButtons(self):
        # Check if the entity and buttonsLayout exist
        if self._entity is None or not self._entity.get('buttonsLayout'):
            return
        
        # Get the buttonsStates from the entity
        buttonsStates = self._entity.get('buttonsStates')
        
        # If the buttonsStates exist, update the 'submit' button state based on the isEnabled property of _brProgressionController
        if buttonsStates is not None:
            if self._brProgressionController.isEnabled:
                state = NOTIFICATION_BUTTON_STATE.DEFAULT
            else:
                state = NOTIFICATION_BUTTON_STATE.VISIBLE
            buttonsStates['submit'] = state

    # Define a method to be called when the settings change
    def __update(self, *_):
        # Call the method to update the entity buttons
        self.__updateEntityButtons()
        # If the model exists, update the notification
        if self._model is not None:
            self._model.updateNotification(self.getType(), self._entityID, self._entity, False)
        return

