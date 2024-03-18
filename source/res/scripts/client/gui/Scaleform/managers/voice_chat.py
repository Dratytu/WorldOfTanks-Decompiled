# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/managers/voice_chat.py

from frameworks.wulf import WindowLayer  # Importing WindowLayer from wulf framework
from VOIP import getVOIPManager  # Importing getVOIPManager from VOIP module
from messenger.proto.events import g_messengerEvents  # Importing g_messengerEvents from messenger.proto.events
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS  # Importing VIEW_ALIAS from daapi.settings.views
from gui.shared.utils import getPlayerDatabaseID  # Importing getPlayerDatabaseID from shared.utils
from gui import DialogsInterface  # Importing DialogsInterface from gui
from messenger.m_constants import PROTO_TYPE  # Importing PROTO_TYPE from m_constants
from messenger.proto import proto_getter  # Importing proto_getter from proto
from gui.Scaleform.framework.entities.abstract.VoiceChatManagerMeta import VoiceChatManagerMeta  # Importing VoiceChatManagerMeta from framework.entities.abstract

_MESSAGE_INIT_SUCCESS = 'voiceChatInitSucceded'
_MESSAGE_INIT_FAILED = 'voiceChatInitFailed'

class BaseVoiceChatManager(VoiceChatManagerMeta):
    """
    Base class for voice chat managers.
    """

    def __init__(self, app):
        """
        Initialize the base voice chat manager.

        :param app: The application instance.
        """
        super(BaseVoiceChatManager, self).__init__()
        self.setEnvironment(app)

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def bwProto(self):
        """
        Get the BW_CHAT2 protocol object.

        :return: The BW_CHAT2 protocol object.
        """
        return None

    def isPlayerSpeaking(self, accountDBID):
        """
        Check if the player with the given accountDBID is speaking.

        :param accountDBID: The account database ID of the player.
        :return: True if the player is speaking, False otherwise.
        """
        return self.bwProto.voipController.isPlayerSpeaking(accountDBID)

    def isVivox(self):
        """
        Check if the voice chat is Vivox.

        :return: True if the voice chat is Vivox, False otherwise.
        """
        return self.bwProto.voipController.isVivox()

    def isYY(self):
        """
        Check if the voice chat is YY.

        :return: True if the voice chat is YY, False otherwise.
        """
        return self.bwProto.voipController.isYY()

    def isVOIPEnabled(self):
        """
        Check if the voice chat is enabled.

        :return: True if the voice chat is enabled, False otherwise.
        """
        return self.bwProto.voipController.isVOIPEnabled()

    def isVOIPAvailable(self):
        """
        Check if the voice chat is available.

        :return: True if the voice chat is available, False otherwise.
        """
        return getVOIPManager().isChannelAvailable()

    def _populate(self):
        """
        Populate the voice chat manager with event listeners.
        """
        super(BaseVoiceChatManager, self)._populate()
        voipEvents = g_messengerEvents.voip
        voipEvents.onVoiceChatInitSucceeded += self._showChatInitSuccessMessage
        voipEvents.onVoiceChatInitFailed += self._showChatInitErrorMessage
        voipEvents.onPlayerSpeaking += self.__onPlayerSpeaking
        self.app.containerManager.onViewAddedToContainer += self.__onViewAddedToContainer

    def _dispose(self):
        """
        Dispose the voice chat manager and remove event listeners.
        """
        voipEvents = g_messengerEvents.voip
        voipEvents.onVoiceChatInitSucceeded -= self._showChatInitSuccessMessage
        voipEvents.onVoiceChatInitFailed -= self._showChatInitErrorMessage
        voipEvents.onPlayerSpeaking -= self.__onPlayerSpeaking
        containerMgr = self.app.containerManager
        if containerMgr:
            containerMgr.onViewAddedToContainer -= self.__onViewAddedToContainer
        super(BaseVoiceChatManager, self)._dispose()

    def _onViewAdded(self, viewAlias):
        """
        Handle the event when a view is added to the container.

        :param viewAlias: The alias of the added view.
        """
        raise NotImplementedError

    def _showChatInitSuccessMessage(self):
        """
        Show the chat initialization success message.
        """
        raise NotImplementedError

    def _showChatInitErrorMessage(self):
        """
        Show the chat initialization error message.
        """
        raise NotImplementedError

    def _showDialog(self, key):
        """
        Show an info dialog with the given key.

        :param key: The key of the dialog.
        """
        DialogsInterface.showI18nInfoDialog(key, lambda result: None)

    def __onPlayerSpeaking(self, accountDBID, isSpeak):
        """
        Handle the event when a player starts or stops speaking.

        :param accountDBID: The account database ID of the player.
        :param isSpeak: True if the player started speaking, False otherwise.
        """
        self.as_onPlayerSpeakS(accountDBID, isSpeak, accountDBID == getPlayerDatabaseID())

    def __onViewAddedToContainer(self, _, pyView):
        """
        Handle the event when a view is added to the container.

        :param _: The event data (not used).
        :param pyView: The added view.
        """
        if pyView.layer == WindowLayer.VIEW:
            self._onViewAdded(pyView.alias)


