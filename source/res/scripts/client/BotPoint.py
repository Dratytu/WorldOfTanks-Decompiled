# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/BotPoint.py

import BigWorld # Importing BigWorld for creating a UserDataObject
from debug_utils import LOG_DEBUG # Importing LOG_DEBUG for logging debug information

# Defining the BotPoint class that inherits from BigWorld.UserDataObject
class BotPoint(BigWorld.UserDataObject):

    def __init__(self):
        # Calling the constructor of the parent class
        BigWorld.UserDataObject.__init__(self)
        
        # Logging the debug information with the position of the BotPoint
        LOG_DEBUG('BotPoint ', self.position)
