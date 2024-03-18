# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic_random/stats_exchange.py

# Import the base classes for vehicle information component and statistics data controller
from gui.Scaleform.daapi.view.battle.classic.stats_exchange import ClassicStatisticsDataController, DynamicVehicleStatsComponent
# Import utility functions for creating exchange brokers and components
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import createExchangeBroker, broker, vehicle

# Define a new class for the epic random vehicle information component
class EpicRandomVehicleInfoComponent(vehicle.VehicleInfoComponent):
    """
    A custom vehicle information component for epic random battles.
    """

    # Override the 'addVehicleInfo' method to add a new 'playerGroup' field
    def addVehicleInfo(self, vInfoVO, overrides):
        """
        Adds the vehicle information to the component and updates the 'playerGroup' field.

        :param vInfoVO: The vehicle information view object
        :param overrides: Additional data to override existing fields
        """
        # Call the superclass method to add the basic vehicle information
        super(EpicRandomVehicleInfoComponent, self).addVehicleInfo(vInfoVO, overrides)
        # Update the 'playerGroup' field with the value from the game mode specific data
        return self._data.update({'playerGroup': vInfoVO.gameModeSpecific.getValue(EPIC_RANDOM_KEYS.PLAYER_GROUP)})


# Define a new class for the epic random statistics data controller
class EpicRandomStatisticsDataController(ClassicStatisticsDataController):
    """
    A custom statistics data controller for epic random battles.
    """

    # Override the '_createExchangeBroker' method to set up custom exchange blocks
    def _createExchangeBroker(self, exchangeCtx):
        """
        Creates and configures a new exchange broker for the epic random battle.

        :param exchangeCtx: The exchange context
        :return: The configured exchange broker
        """
        # Create a new exchange broker using the provided context
        exchangeBroker = createExchangeBroker(exchangeCtx)
        # Configure the vehicles information exchange block
        exchangeBroker.setVehiclesInfoExchange(vehicle.VehiclesExchangeBlock(EpicRandomVehicleInfoComponent(), 
                                                                            positionComposer=broker.BiDirectionComposer(), 
                                                                            idsComposers=(vehicle.TeamsSortedIDsComposer(), 
                                                                                         vehicle.TeamsCorrelationIDsComposer()), 
                                                                            statsComposers=None))
        # Configure the vehicles stats exchange block
        exchangeBroker.setVehiclesStatsExchange(vehicle.VehiclesExchangeBlock(DynamicVehicleStatsComponent(), 
                                                                              positionComposer=broker.BiDirectionComposer(),
