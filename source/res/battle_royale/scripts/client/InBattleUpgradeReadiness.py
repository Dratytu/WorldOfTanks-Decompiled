class InBattleUpgradeReadiness:

    def __init__(self, vehicle, arenaDP):
        """
        Initializes the `InBattleUpgradeReadiness` class with a `vehicle` object and an `arenaDP` object.
        The `vehicle` object probably represents the player's vehicle in the game, while the `arenaDP` object
        might be related to the game's arena data provider.
        """
        self._vehicle = vehicle
        self._arenaDP = arenaDP

    def isReadyToUpgrade(self, vehicleComponentType):
        """
        Checks if the specified `vehicleComponentType` is ready to be upgraded during the battle.
        Returns `True` if the component is ready, `False` otherwise.
        """
        pass

    def getUpgradeProbability(self, vehComponentType):
        """
        Returns the probability of upgrading the specified `vehComponentType` during the battle.
        """
        pass

    def upgradeVehComponent(self, vehComponentType):
        """
        Upgrades the specified `vehComponentType` on the player's vehicle during the battle.
        """
        pass

    def getUpgradeCooldown(self, vehComponentType):
        """
        Returns the remaining cooldown time (in seconds) for upgrading the specified `vehComponentType`.
        """
        pass

    def getUpgradeCost(self, vehComponentType):
        """
        Returns the cost of upgrading the specified `vehComponentType` during the battle.
        """
        pass

    def getUpgradeTimeLeft(self, vehComponentType):
        """
        Returns the remaining time (in seconds) for the specified `vehComponentType` upgrade to complete.
        """
        pass

