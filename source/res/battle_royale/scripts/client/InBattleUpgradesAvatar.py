# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/in_battle_upgrades_avatar.py

import BigWorld  # Imported for creating a DynamicScriptComponent
from debug_utils import LOG_DEBUG, LOG_WARNING  # Imported for logging debug and warning messages
import BattleReplay  # Imported for replay control
from items import vehicles, ITEM_TYPES  # Imported for vehicle-related functionalities

class InBattleUpgradesAvatar(BigWorld.DynamicScriptComponent):
    """
    A class representing the in-battle upgrades for an avatar.
    """

    def onEnterWorld(self, *args):
        """
        Called when the avatar enters the world.
        """
        pass

    def onLeaveWorld(self, *args):
        """
        Called when the avatar leaves the world.
        """
        pass

    def vehicleUpgradeResponse(self, intCDs, reasons):
        """
        Handles the response for vehicle upgrades.

        :param intCDs: A list of integer compact descriptor codes for the upgrades.
        :param reasons: A list of boolean values indicating success or failure for each upgrade.
        """
        player = self.entity  # The player entity

        def __vehicleUpgradeLogger(is_success, int_cd, reason, module_txt):
            """
            A helper function for logging upgrade successes and failures.

            :param is_success: A boolean value indicating success or failure.
            :param int_cd: The integer compact descriptor code for the upgrade.
           
