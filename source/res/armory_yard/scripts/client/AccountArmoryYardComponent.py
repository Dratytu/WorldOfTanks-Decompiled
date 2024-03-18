# Python 2.7
import BigWorld
import armory_yard_constants

class AccountArmoryYardComponent(BigWorld.StaticScriptComponent):
    """
    A component for handling Account Armory Yard related functionality.
    """

    def collect_all_rewards(self, callback=None):
        """
        Collect all rewards available in the Armory Yard.

        :param callback: A function to be called when the command is processed.
        """
        self.entity._do_cmd_int(armory_yard_constants.CMD_COLLECT_REWARDS, 0, callback)

    def buy_step_tokens(self, currency, count, callback=None):

