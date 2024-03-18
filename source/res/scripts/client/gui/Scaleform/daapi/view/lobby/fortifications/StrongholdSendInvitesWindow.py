# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/StrongholdSendInvitesWindow.py

# Import necessary modules
from functools import partial
from gui.prb_control.entities.base.external_battle_unit.base_external_battle_ctx import SendInvitesExternalBattleUnitCtx
from gui.Scaleform.daapi.view.lobby.SendInvitesWindow import SendInvitesWindow
from gui.shared.utils.requesters.abstract import Response
from gui.shared.view_helpers.UsersInfoHelper import UsersInfoHelper
from client_request_lib.exceptions import ResponseCodes
from gui import SystemMessages
from gui.Scaleform.locale.INVITES import INVITES

# Define the StrongholdSendInvitesWindow class, which inherits from SendInvitesWindow and UsersInfoHelper
class StrongholdSendInvitesWindow(SendInvitesWindow, UsersInfoHelper):

    # Implement the sendInvites method, which takes accountsToInvite and comment as arguments
    def sendInvites(self, accountsToInvite, comment):
        # Check if accountsToInvite is not empty
        if accountsToInvite:
            # Request the send invites action using the prbEntity
            self.prbEntity.request(SendInvitesExternalBattleUnitCtx(accountsToInvite, comment), partial(self.__sendInvitesCallback, accountsToInvite))

    # Implement the __sendInvitesCallback method, which takes accountsToInvite and response as arguments
    def __sendInvitesCallback(self, accountsToInvite, response):
        # Check if response is an instance of Response and its code is NO_ERRORS
        if isinstance(response, Response) and response.getCode() == ResponseCodes.NO_ERRORS:
            # Iterate through the accountsToInvite list
            for userId in accountsToInvite:
                # Push a system message indicating the invite has been sent to the user
                SystemMessages.pushI18nMessage(INVITES.STRONGHOLD_INVITE_SENDINVITETOUSERNAME, type
