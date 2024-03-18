# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/pre_queue/actions_validator.py

# Import necessary modules and classes
from CurrentVehicle import g_currentVehicle
from gui.prb_control.entities.base.actions_validator import BaseActionsValidator, ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator
from gui.prb_control.items import ValidationResult
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION
from gui.periodic_battles.models import PrimeTimeStatus
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleController

# Define the BattleRoyaleValidator class, which inherits from BaseActionsValidator
class BattleRoyaleValidator(BaseActionsValidator):

    # Implement the _validate method for BattleRoyaleValidator
    def _validate(self):
        # Get an instance of IBattleRoyaleController
        brController = dependency.instance(IBattleRoyaleController)
        # Get the prime time status, vehicle type, and vehicle ID
        status, _, _ = brController.getPrimeTimeStatus()
        # Check if the current vehicle is only for Battle Royale battles and the prime time status is not available
        if g_currentVehicle.isOnlyForBattleRoyaleBattles() and status != PrimeTimeStatus.AVAILABLE:
            # Return a ValidationResult indicating that the action is not valid
            return ValidationResult(False, PRE_QUEUE_RESTRICTION.MODE_NOT_AVAILABLE)
        # If the conditions are met, call the superclass's _validate method
        else:
            return super(BattleRoyaleValidator, self)._validate()

# Define the BattleRoyaleActionsValidator class, which inherits from PreQueueActionsValidator
class BattleRoyaleActionsValidator(PreQueueActionsValidator):

    # Implement the _createStateValidator method for BattleRoyaleActionsValidator
    def _createStateValidator(self, entity):
        # Create a base validator using the superclass's method
        baseValidator = super(BattleRoyaleActions
