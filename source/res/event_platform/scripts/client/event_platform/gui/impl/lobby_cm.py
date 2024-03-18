# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: event_platform/scripts/client/event_platform/gui/impl/lobby_cm.py

import logging

from debug_utils import LOG_ERROR  # Importing LOG_ERROR for logging error messages
from gui.Scaleform.daapi.view.lobby.hangar.hangar_cm_handlers import VehicleContextMenuHandler  # Importing VehicleContextMenuHandler as a base class

# Defining a custom handler class for the vehicle context menu in the event platform lobby
class EPVehicleContextMenuHandler(VehicleContextMenuHandler):

    # Initializing the custom handler class
    def __init__(self, cmProxy, ctx=None):
        # Logging an error message with the name of the function being initialized
        LOG_ERROR('INIT -- EPVehicleContextMenuHandler')
        
        # Calling the constructor of the base class with the provided cmProxy and ctx
        super(EPVehicleContextMenuHandler, self).__init__(cmProxy, ctx)
