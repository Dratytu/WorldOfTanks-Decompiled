# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/AccountArmoryYardComponent.py

import BigWorld
import armory_yard_constants

class AccountArmoryYardComponent(BigWorld.StaticScriptComponent):
    """
    A component for handling Account Armory Yard related functionality.
    """

    def collectAllRewards(self, callback=None):
        """
        Collect all rewards available in the Armory Yard.

        :param callback: A function to be called when the command is processed.
        """
        self.entity._doCmdInt(armory_yard_constants.CMD_COLLECT_REWARDS, 0, callback)

    def buyStepTokens(self, currency, count, callback=None):
        """
        Buy step tokens using the specified currency.

        :param currency: The currency to be used for buying step tokens.
        :param count: The number of step tokens to be bought.
        :param callback: A function to be called when the command is processed.
        """
        self.entity._doCmdIntStr(armory_yard_constants.CMD_BUY_STEP_TOKENS, count, currency, callback)

    def devAddToken(self, count, callback=None):
        """
        Add a specified number of tokens for development purposes.

        :param count: The number of tokens to be added.
        :param callback: A function to be called when the command is processed.
        """
        self.entity._doCmdInt(armory_yard_constants.DEV_CMD_ADD_TOKEN_S, count, callback)

    def devCompleteQuest(self, cycle, number, callback=None):
        """
        Complete a specific quest for development purposes.

        :param cycle: The cycle of the quest to be completed.
        :param number: The number of the quest to be completed.
        :param callback: A function to be called when the command is processed.
        """
        self.entity._doCmdInt2(armory_yard_constants.DEV
