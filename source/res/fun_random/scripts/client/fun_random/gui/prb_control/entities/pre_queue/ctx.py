# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/ctx.py

# Import necessary constants and classes
from constants import QUEUE_TYPE
from gui.prb_control.entities.base.pre_queue.ctx import QueueCtx, JoinPreQueueModeCtx
from gui.prb_control.settings import FUNCTIONAL_FLAG
from gui.shared.utils.decorators import ReprInjector

# Define a new class FunRandomQueueCtx that inherits from QueueCtx
@ReprInjector.withParent(('getVehicleInventoryID', 'vInvID'), ('getDesiredSubModeID', 'subModeID'))
class FunRandomQueueCtx(QueueCtx):
    __slots__ = ('__desiredSubModeID', '__vInventoryID')

    # Initialize the class with vehicle inventory ID, desired sub-mode ID, and waiting ID
    def __init__(self, vInventoryID, desiredSubModeID, waitingID=''):
        super(FunRandomQueueCtx, self).__init__(entityType=QUEUE_TYPE.FUN_RANDOM, waitingID=waitingID)
        self.__desiredSubModeID = desiredSubModeID  # Set the desired sub-mode ID
        self.__vInventoryID = vInventoryID  # Set the vehicle inventory ID

    # Get the desired sub-mode ID
    def getDesiredSubModeID(self):
        return self.__desiredSubModeID

    # Get the vehicle inventory ID
    def getVehicleInventoryID(self):
        return self.__vInventoryID


# Define a new class JoinFunPreQueueModeCtx that inherits from JoinPreQueueModeCtx
@ReprInjector.withParent(('getDesiredSubModeID', 'desiredSubModeID'))
class JoinFunPreQueueModeCtx(JoinPreQueueModeCtx):
    __slots__ = ('__desiredSubModeID',)

    # Initialize the class with queue type, desired sub-mode ID, flags, and waiting ID
    def __init__(self, queueType, desiredSubModeID, flags=FUNCTIONAL_FLAG.UNDEFINED, waitingID=''):
        super(JoinFunPreQueueModeCtx, self).__init__(queueType=queueType, flags=flags, waitingID=waitingID)
        self.__desiredSubModeID = desiredSub
