# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/game_control/awards_controller.py

import dependency
from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher
from gui.game_control.AwardController import ServiceChannelHandler
from helpers import dependency
from fun_random.gui.fun_gui_constants import SCH_CLIENT_MSG_TYPE
from skeletons.gui.system_messages import ISystemMessages

# A helper function to extract the message from the context
def _getMessage(ctx):
    _, message = ctx
    return message


class FunProgressionQuestsHandler(ServiceChannelHandler, FunProgressionWatcher):
    # Dependency injection for ISystemMessages
    __systemMessages = dependency.descriptor(ISystemMessages)
    # Constants for the client message type
    _CLIENT_MSG_TYPE = SCH_CLIENT_MSG_TYPE.FUN_RANDOM_PROGRESSION

    def __init__(self, awardCtrl):
        # Initialize the superclass with the battle results message type and the award controller
        super(FunProgressionQuestsHandler, self).__init__(SYS_MESSAGE_TYPE.battleResults.index(), awardCtrl)

    def _showAward(self, ctx):
        # Push the client message with the corresponding message and client message type
        self.__systemMessages.proto.serviceChannel.pushClientMessage(_getMessage(ctx), self._CLIENT_MSG_TYPE)

    def _needToShowAward(self, ctx):
        # Check if the superclass method returns True and if the completed quest IDs contain any progression quest IDs
        if super(FunProgressionQuestsHandler, self)._needToShowAward(ctx):
            return bool([qID for qID in _getMessage(ctx).data.get('completedQuestIDs', set()) if self._funRandomCtrl.progressions.isProgressionExecutor(qID)])
        # If not, return False
        return False
