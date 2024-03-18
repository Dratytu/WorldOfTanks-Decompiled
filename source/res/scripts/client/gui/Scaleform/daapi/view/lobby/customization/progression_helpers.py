# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/customization/progression_helpers.py

import binascii
import logging
import struct
from collections import namedtuple

# Dependency injection for IItemsCache
from CurrentVehicle import g_currentVehicle
from constants import EVENT_TYPE
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.impl import backport
from gui.impl.gen import R
from gui.server_events import formatters
from gui.server_events.events_helpers import MISSIONS_STATES
from helpers import dependency
from helpers import int2roman
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache

# Logger setup for this module
_logger = logging.getLogger(__name__)

