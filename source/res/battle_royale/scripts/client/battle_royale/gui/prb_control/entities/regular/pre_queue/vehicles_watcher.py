# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/pre_queue/vehicles_watcher.py

# Import necessary modules and classes
from gui.prb_control.entities.base.pre_queue.vehicles_watcher import BaseVehiclesWatcher
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache

# Define the BattleRoyaleVehiclesWatcher class, which inherits from BaseVehiclesWatcher
class BattleRoyaleVehiclesWatcher(BaseVehiclesWatcher):
    # Inject dependencies using dependency.descriptor
    itemsCache = dependency.descriptor(IItemsCache)
    lobbyContext = dependency.descriptor(ILobbyContext)

    # Implement the _getUnsuitableVehicles method
    def _getUnsuitableVehicles(self, onClear=False):
        # Get all vehicles from the itemsCache that match the REQ_CRITERIA.INVENTORY criteria
        # and do not have REQ_CRITERIA.VEHICLE.BATTLE_ROYALE set
        vehs = self.itemsCache.items.getVehicles(REQ_CRITERIA.INVENTORY | ~REQ_CRITERIA.VEHICLE.BATTLE_ROYALE).itervalues()
        # Return the list of unsuitable vehicles
        return vehs
