# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/battleground/components.py

import BigWorld  # Import the BigWorld module for accessing player and models
import Math  # Import the Math module for vector and matrix operations
import AnimationSequence  # Import the AnimationSequence module for animation handling
import CGF  # Import the CGF module for game objects and components
import math_utils  # Import the math_utils module for creating matrices
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent  # Import utilities for creating components
from cgf_obsolete_script.py_component import Component  # Import the base Component class
from battleground.iself_assembler import ISelfAssembler  # Import the ISelfAssembler interface for self-assembling game objects
from cgf_obsolete_script.script_game_object import ScriptGameObject, ComponentDescriptorTyped  # Import the ScriptGameObject and related utilities
from arena_component_system.client_arena_component_system import ClientArenaComponent  # Import the ClientArenaComponent base class
from helpers import EffectsList, isPlayerAvatar  # Import helper functions for working with effects and checking if the local player is an avatar
from PlayerEvents import g_playerEvents  # Import the g_playerEvents object for listening to player-related events

class ModelComponent(Component):
    """
    A component representing a 3D model in the game world.
    """

    def __init__(self, compoundModel, **kwargs):
        """
        Initialize the ModelComponent with a compound model and optional offset.

        :param compoundModel: The CompoundModel to be managed by this component.
        :param offset: An optional offset to apply to the model's position (default: (0, 0, 0)).
        """
        offset = kwargs.get('offset', 0.0)
        self.__offset = (0.0, offset, 0.0)
        self.__baseModel = compoundModel
        self.__isInWorld = False

    def activate(self):
        """
        Add the model to the player's list of models, making it visible in the game world.
        """
        player = BigWorld.player()
        if self.compoundModel is not None and not self.__isInWorld and player is not None:
            player.addModel(self.compoundModel)
            self.__isInWorld = True

    def deactivate(self):
        """
        Remove the model from the player's list of models, making it invisible in the game world.
        """
        player = BigWorld.player()
        if self.__isInWorld and self.compoundModel is not None and player is not None and self.compoundModel in player.models:
            player.delModel(self.compoundModel)

class SequenceComponent(Component):
    """
    A component responsible for managing animation sequences.
    """

    def __init__(self, sequenceAnimator):
        """
        Initialize the SequenceComponent with a SequenceAnimator.

        :param sequenceAnimator: The SequenceAnimator to be managed by this component.
        """
        self.__sequenceAnimator = sequenceAnimator

    def bindToCompound(self, compound):
        """
        Bind the SequenceAnimator to a CompoundModel.

        :param compound: The CompoundModel to bind the SequenceAnimator to.
        """
        if compound is None:
            return
        else:
            if self.__sequenceAnimator is not None and not self.__sequenceAnimator.isBound():
                self.__sequenceAnimator.bindTo(AnimationSequence.CompoundWrapperContainer(compound))
                self.__startUnchecked()
            return

    def unbind(self):
        """
        Unbind the SequenceAnimator from its current target.
        """
        if self.__sequenceAnimator is not None and self.__sequenceAnimator.isBound():
            self.__sequenceAnimator.unbind()

    @property
    def sequenceAnimator(self):
        """
        Get the SequenceAnimator managed by this component.

        :return: The SequenceAnimator.
        """
        return self.__sequenceAnimator

    # (Other methods omitted for brevity)

# (Other classes omitted for brevity)

