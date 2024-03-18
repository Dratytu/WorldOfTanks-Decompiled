# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale_progression/scripts/client/battle_royale_progression/gui/game_control/awards_controller.py

# Import necessary modules and classes
from battle_royale_progression.gui.gui_constants import SM_TYPE_BR_PROGRESSION, SCH_CLIENT_MSG_TYPE
from battle_royale_progression.gui.shared.event_dispatcher import showAwardsView
from chat_shared import SYS_MESSAGE_TYPE
from gui.game_control.AwardController import ServiceChannelHandler
from helpers import dependency
from skeletons.gui.system_messages import ISystemMessages

# Define a helper function to extract the message from the context
def _getMessage(ctx):
    _, message = ctx
    return message

# Subclass ServiceChannelHandler to handle BR progression notifications
class BRProgressionStageHandler(ServiceChannelHandler):
    # Define a class variable for the system messages dependency
    __systemMessages = dependency.descriptor(ISystemMessages)
    # Define a class variable for the client message type
    _CLIENT_MSG_TYPE = SCH_CLIENT_MSG_TYPE.BR_PROGRESSION_NOTIFICATIONS

    # Initialize the handler with the award controller
    def __init__(self, awardCtrl):
        super(BRProgressionStageHandler, self).__init__(SYS_MESSAGE_TYPE.__getattr__(SM_TYPE_BR_PROGRESSION).index(), awardCtrl)

    # Override the _showAward method to show awards for completed stages
    def _showAward(self, ctx):
        _, message = ctx
        stages = message.data.get('stages', set())
        for stage in stages:
            if stage.get('showAwardWindow', False):
                showAwardsView(stage)

        # Show any system messages after displaying awards
        self._showMessages(ctx)

    # Override the _showMessages method to send client messages
    def _showMessages(self, ctx):
        self.__systemMessages.proto.serviceChannel.pushClientMessage(_getMessage(ctx), self._CLIENT_MSG_TYPE)
