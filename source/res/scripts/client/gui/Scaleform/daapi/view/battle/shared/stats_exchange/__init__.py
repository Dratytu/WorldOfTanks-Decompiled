# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/stats_exchange/__init__.py

# Import necessary modules
import weakref

# Import custom modules from the same package
from gui.Scaleform.daapi.view.battle.shared.stats_exchange import broker, player
from gui.Scaleform.daapi.view.battle.shared.stats_exchange.stats_ctrl import BattleStatisticsDataController

# Define the list of all exported symbols from this module
__all__ = ('BattleStatisticsDataController', 'createExchangeBroker')

def createExchangeBroker(exchangeCtx):
    # Create a weak reference proxy for the exchange context
    proxy = weakref.proxy(exchangeCtx)
    
    # Create an ExchangeBroker instance and associate it with the exchange context
    exchangeBroker = broker.ExchangeBroker(exchangeCtx)
    
    # Set up the PlayerStatusExchange component for the broker
    exchangeBroker.setPlayerStatusExchange(player.PlayerStatusComponent())
    
    # Set up the UsersTagsExchangeData component for the broker, using the proxy for the exchange context
    exchangeBroker.setUsersTagsExchange(player.UsersTagsListExchangeData(proxy))
    
    # Set up the InvitationsExchangeBlock component for the broker
    exchangeBroker.setInvitationsExchange(player.InvitationsExchangeBlock())
    
    # Return the configured ExchangeBroker instance
    return exchangeBroker

