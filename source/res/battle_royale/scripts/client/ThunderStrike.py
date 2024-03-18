# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/ThunderStrike.py

import BigWorld
from Event import Event  # Importing Event class from helpers.Event
from helpers.CallbackDelayer import CallbackDelayer  # Importing CallbackDelayer class from helpers.CallbackDelayer
from debug_utils import LOG_DEBUG_DEV  # Importing LOG_DEBUG_DEV for debug logging

class ThunderStrike(BigWorld.Entity, CallbackDelayer):
    
    def __init__(self):
        """
        Initialize the ThunderStrike class, which inherits from BigWorld.Entity and CallbackDelayer.
        """
        super(ThunderStrike, self).__init__()
        
        # Log a debug message with the position and equipmentID of the ThunderStrike
        LOG_DEBUG_DEV('ArenaInfoThunderStrikeLauncher launched', self.position, self.equipmentID)
        
        # Create an Event object called onHit
        self.onHit = Event()

    def hitThunderStrike(self):
        """
        A method to handle the hit event for the ThunderStrike.
        """
        LOG_DEBUG_DEV('hitThunderStrike')
        
        # Trigger the onHit event
        self.onHit()
