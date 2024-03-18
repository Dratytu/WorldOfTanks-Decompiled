import logging
import BigWorld
import BattleRoyaleConstants as brc

class AccountBattleRoyaleComponent(BigWorld.StaticScriptComponent):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

