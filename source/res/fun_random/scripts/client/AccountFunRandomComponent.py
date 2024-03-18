# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/AccountFunRandomComponent.py

import typing  # For type checking
import AccountCommands  # Account-related commands
from BaseAccountExtensionComponent import BaseAccountExtensionComponent  # Base class for account extension components
from constants import QUEUE_TYPE  # Different queue types
from PlayerEvents import g_playerEvents as events  # Player events

# Typing imports for type checking if enabled
if typing.TYPE_CHECKING:
    from fun_random.gui.prb_control.entities.pre_queue.ctx import FunRandomQueueCtx  # Context object for fun random queue


class AccountFunRandomComponent(BaseAccountExtensionComponent):

    def enqueueFunRandom(self, ctx):
        """
        Enqueue the player into the fun random queue with the given context.

        :param ctx: FunRandomQueueCtx - Context object containing queue parameters
        """
        self.base.doCmdIntArr(  # Call the base class method with integer array argument
            AccountCommands.REQUEST_ID_NO_RESPONSE,  # Request ID with no response
            AccountCommands.CMD_ENQUEUE_IN_BATTLE_QUEUE,  # Command to enqueue in battle queue
            [QUEUE_TYPE.FUN_RANDOM,  # Queue type: fun random
             ctx.getVehicleInventoryID(),  # Vehicle inventory ID
             ctx.getDesiredSubModeID()])  # Desired sub-mode ID

    def dequeueFunRandom(self):
        """
        Dequeue the player from the fun random queue if the player entity is not changing.
        """
        if not events.isPlayerEntityChanging:  # Check if the player entity is not changing
            self.base.doCmdInt(  # Call the base class method with integer argument
                AccountCommands.REQUEST_ID_NO_RESPONSE,  # Request ID with no response
                AccountCommands.CMD_DEQUEUE_FROM_BATTLE_QUEUE,  # Command to dequeue from battle queue
              
