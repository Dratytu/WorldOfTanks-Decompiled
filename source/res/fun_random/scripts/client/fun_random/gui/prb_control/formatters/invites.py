# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/prb_control/formatters/invites.py

# Import necessary modules and classes
from fun_random_common.fun_constants import UNKNOWN_EVENT_ID
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasSpecifiedSubMode
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.formatters.invites import PrbInviteHtmlTextFormatter
from gui.shared.utils.functions import makeTooltip
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import dependency
from shared_utils import first
from skeletons.gui.shared import IItemsCache

# Define the FunPrbInviteHtmlTextFormatter class, which inherits from PrbInviteHtmlTextFormatter,
# FunAssetPacksMixin, and FunSubModesWatcher.
class FunPrbInviteHtmlTextFormatter(PrbInviteHtmlTextFormatter, FunAssetPacksMixin, FunSubModesWatcher):
    
    # Declare dependency on IItemsCache
    __itemsCache = dependency.descriptor(IItemsCache)

    # Define the canAcceptInvite method, which checks if the user can accept the invite
    def canAcceptInvite(self, invite):
        canAccept = super(FunPrbInviteHtmlTextFormatter, self).canAcceptInvite(invite)
        return canAccept and self.__hasAnyVehicle()

    # Define the getIconPath method, which returns the path to the invite notification icon
    def getIconPath(self, invite, pathMaker=None):
        return backport.image(self.getModeIconsResRoot().library.invite_notification())

    # Define the updateTooltips method, which updates the tooltips in the invite message
    def updateTooltips(self, invite, canAccept, message):
        if not canAccept and 'buttonsLayout' in message and not self.__hasAnyVehicle():
            tooltip = makeTooltip(body=backport.text(R.strings.fun_random.invite.tooltip.noVehicles()))
            message['buttonsLayout'][0]['tooltip'] = tooltip
        return message

    # Define the _getTitle method, which returns the title of the invite
    def _getTitle(self, invite, kwargs=None):
        subModeID = first(invite.getExtraData('unitInviteExtras', []), UNKNOWN_EVENT_ID)
        detailedModeName = self.__getDetailedModeName(subModeID) or self.getModeUserName()
        return backport.text(R.strings.fun_random.invite.text.detailedTitle(), detailedModeName=detailedModeName)

    # Define the __hasAnyVehicle method, which checks if the user has any vehicles
    def __hasAnyVehicle(self):
        return bool(self.__itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY))

    # Define the __getDetailedModeName method, which returns the detailed name of the submode
    @hasSpecifiedSubMode(defReturn='')
    def __getDetailedModeName(self, subModeID):
        subModeName = backport.text(self.getSubMode(subModeID).getLocalsResRoot().userName())
        return self.getModeDetailedUserName(subModeName=subModeName)

