# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/abilities.py

import AccountCommands
from items.abilities_manager import AbilitiesManager  # Importing AbilitiesManager to manage abilities

class AbilitiesHelper(object):
    def __init__(self):
        """
        Initialize the AbilitiesHelper class with default values.
        :param self: The object itself
        """
        self.__account = None  # Holder for the account object
        self.__ignore = True  # Flag to ignore certain actions if not a player
        self.__abilities = AbilitiesManager()  # Manager to handle abilities
        return

    def onAccountBecomePlayer(self):
        """
        Set the ignore flag to False when the account becomes a player.
        :param self: The object itself
        """
        self.__ignore = False

    def onAccountBecomeNonPlayer(self):
        """
        Set the ignore flag to True when the account is no longer a player.
        :param self: The object itself
        """
        self.__ignore = True

    def setAccount(self, account):
        """
        Set the account object.
        :param self: The object itself
        :param account: The account object
        """
        self.__account = account

    @property
    def abilitiesManager(self):
        """
        Getter for the abilities manager.
        :param self: The object itself
        :return: The abilities manager
        """
        return self.__abilities

    def addPerks(self, battle, vehicleID, scopeIndex, perksList, callback=None):
        """
        Add perks to a vehicle in battle or in debug mode.
        :param self: The object itself
        :param battle: Boolean indicating if the game is in battle
        :param vehicleID: ID of the vehicle
        :param scopeIndex: Index of the scope
        :param perksList: List of perks to be added
        :param callback: Callback function for the result
        """
        if battle:
            if self.__ignore:
                if callback is not None:
                    callback(AccountCommands.RES_NON_PLAYER)
                return
            if callback is not None:
                proxy = lambda requestID, resultID, errorStr, ext={}: callback(resultID)
            else:
                proxy = None
            perksListRes = [vehicleID, scopeIndex]
            perksListRes.extend(perksList)
            self.__account._doCmdIntArr(AccountCommands.CMD_ADD_PERK_TO_BATTLE, perksListRes, proxy)
        else:
            perks = {perksList[i]: perksList[i + 1] for i in xrange(0, len(perksList), 2)}
            self.abilitiesManager.addBuild(vehicleID, 'debug' + str(scopeIndex), perks)
        return

    def resetPerks(self, battle, vehicleID, callback=None):
        """
        Reset perks for a vehicle in battle or in debug mode.
        :param self: The object itself
        :param battle: Boolean indicating if the game is in battle
        :param vehicleID: ID of the vehicle
        :param callback: Callback function for the result
        """
        if battle:
            if self.__ignore:
                if callback is not None:
                    callback(AccountCommands.RES_NON_PLAYER)
                return
           
