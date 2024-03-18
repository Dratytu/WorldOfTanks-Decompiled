# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/prb_control/entities/tournament/pre_queue/action_validator.py

from gui.prb_control.entities.base.actions_validator import ActionsValidatorComposite
from gui.prb_control.entities.base.pre_queue.actions_validator import PreQueueActionsValidator, InQueueValidator
from gui.prb_control.items import ValidationResult

# A custom InQueueValidator for Battle Royale tournament pre-queue entities
class _BattleRoyaleTournamentInQueueValidator(InQueueValidator):

    def _validate(self):
        # Override the default validation behavior to allow queueing if the entity is already in the queue
        return ValidationResult(True) if self._entity.isInQueue() else super(_BattleRoyaleTournamentInQueueValidator, self)._validate()


# A custom PreQueueActionsValidator for Battle Royale tournament entities
class BattleRoyaleTournamentActionsValidator(PreQueueActionsValidator):

    def _createStateValidator(self, entity):
        # Create a composite validator that includes the custom InQueueValidator
        return ActionsValidatorComposite(entity, [_BattleRoyaleTournamentInQueueValidator(entity)])
