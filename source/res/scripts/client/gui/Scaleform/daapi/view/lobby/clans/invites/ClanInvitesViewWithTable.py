# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/clans/invites/ClanInvitesViewWithTable.py

import weakref
import math
from debug_utils import LOG_ERROR
from gui.Scaleform.daapi.settings import BUTTON_LINKAGES
from gui.clans import formatters as clans_fmts
from gui.clans.settings import CLAN_INVITE_STATES, ACTIVE_INVITE_LIFE_TIME
from gui.clans.items import isValueAvailable, formatField
from gui.Scaleform.daapi.view.meta.ClanInvitesViewWithTableMeta import ClanInvitesViewWithTableMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider
from gui.Scaleform.locale.CLANS import CLANS
from gui.shared.formatters import text_styles
from helpers import time_utils
from helpers.i18n import makeString as _ms
from gui.shared.utils.functions import makeTooltip


