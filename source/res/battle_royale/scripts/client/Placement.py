# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/Placement.py

import BigWorld  # Import BigWorld module for creating custom entities
from constants import AirdropType  # Import AirdropType constants
from debug_utils import LOG_DEBUG_DEV, LOG_ERROR  # Import logging functions
from gui.shared import g_eventBus, EVENT_BUS_SCOPE  # Import event bus for handling events
from gui.shared.events import AirDropEvent  # Import AirDropEvent for placement events
from helpers import dependency  # Import dependency for dependency injection
from skeletons.gui.battle_session import IBattleSessionProvider  # Import IBattleSessionProvider interface


