# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/InBattleUpgradesAvatar.py

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

        def __vehicleUpgradeLogger(isSuccess, intCD, reason, moduleTxt):
            """
            A helper function for logging upgrade successes and failures.

            :param isSuccess: A boolean value indicating success or failure.
            :param intCD: The integer compact descriptor code for the upgrade.
            :param reason: The reason for the upgrade failure.
            :param moduleTxt: The text for the module type.
            """
            if isSuccess:
                LOG_DEBUG('{} intCD = {} successfully installed'.format(moduleTxt, intCD))
            else:
                LOG_WARNING('Could not install {} intCD = {}. Reason - {}!'.format(moduleTxt, intCD, reason))

        for intCD, reason in zip(intCDs, reasons):
            __vehicleUpgradeLogger(reason == '', intCD, reason, 'Main' if intCD is intCDs[0] else 'Additional')

        mainIntCDs = intCDs[0]  # The main integer compact descriptor code
        mainSuccess = not reasons[0]  # The success or failure of the main upgrade

        if mainSuccess and ITEM_TYPES.vehicleGun in [vehicles.parseIntCompactDescr(intCD)[0] for intCD in intCDs]:
            """
            If the main upgrade was successful and it's a vehicle gun, upgrade the vehicle gun.
            """
            self.__upgradeVehicleGun()

        if player.guiSessionProvider.dynamic.progression:
            if BattleReplay.g_replayCtrl.isPlaying:
                player.guiSession
