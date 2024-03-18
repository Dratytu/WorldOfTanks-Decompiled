# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_modifiers/scripts/client/battle_modifiers/gui/impl/lobby/feature/helpers.py

from typing import TYPE_CHECKING, Union, Optional
# Importing type hints for variables and function return types

from battle_modifiers.gui.impl.lobby.feature.constants import MOD_TYPE_MAP, PHYS_TYPE_MAP, USE_TYPE_MAP, GAMEPLAY_IMPACT_MAP
# Importing constant dictionaries to map internal values to user-friendly strings

from battle_modifiers.gui.impl.gen.view_models.views.lobby.feature.modifier_model import ModifierModel
# Importing ModifierModel class to create a view model for a battle modifier

from battle_modifiers.gui.impl.gen.view_models.views.lobby.feature.limit_model import LimitModel, LimitType
# Importing LimitModel class to create a view model for a modifier limit

if TYPE_CHECKING:
    # Importing type hints for type checking purposes only
    from battle_modifiers_ext.battle_modifiers import BattleModifier, FakeBattleModifier
    from frameworks.wulf import Array

def packModifierModel(modifier):
    # Function to pack a BattleModifier object into a ModifierModel view model
    result = ModifierModel()
    # Creating a new ModifierModel instance

    result.setValue(modifier.value)
    # Setting the value of the modifier

    result.setUseType(USE_TYPE_MAP[modifier.useType])
    # Mapping the useType to a user-friendly string

    result.setModificationType(MOD_TYPE_MAP[modifier.param.id])
    # Mapping the modification type (id) to a user-friendly string

    result.setResName(modifier.param.clientData.resName)
    # Setting the resource name of the modifier

    result.setPhysicalType(PHYS_TYPE_MAP[modifier.param.clientData.physicalType])
    # Mapping the physical type to a user-friendly string

    result.setGameplayImpact(GAMEPLAY_IMPACT_MAP[modifier.gameplayImpact])
    # Mapping the gameplay impact to a user-friendly string

    _invalidateLimits(modifier, result.getLimits())
    # Invalidating and setting the limits for the modifier

    return result
    # Returning the populated ModifierModel


def _invalidateLimits(modifier, limitsModel):
    # Helper function to invalidate and set limits for a modifier
    limitsModel.clear()
    # Clearing any existing limits

    models = [_packLimitModel(modifier.minValue, LimitType.MIN), _packLimitModel(modifier.maxValue
