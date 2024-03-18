# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/tooltips/royale_battle_builders.py

# Import necessary modules and constants
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.app_loader import sf_battle
from gui.shared.gui_items import GUI_ITEM_TYPE
from battle_royale.gui.shared.tooltips.battle_royale_modules import BattleRoyaleModulesTooltip
from gui.shared.tooltips.builders import DataBuilder
from helpers import dependency
from items import parseIntCompactDescr
from skeletons.gui.battle_session import IBattleSessionProvider

# Define the function that returns the tooltip builders
def getTooltipBuilders():
    # Return a tuple of DataBuilder instances
    return (DataBuilder(TOOLTIPS_CONSTANTS.BATTLE_ROYALE_MODULES, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, BattleRoyaleModulesTooltip(_BattleRoyaleBattleVehInfoContext())),)

# Define the inner class _BattleRoyaleBattleVehInfoContext
class _BattleRoyaleBattleVehInfoContext(object):

    # Define the sf_battle decorated method to get the application instance
    @sf_battle
    def app(self):
        return None

    # Define the method to build the item tooltip
    def buildItem(self, *args, **kwargs):
        # Get the item compact descriptor from the arguments
        intCD = args[0]
        # Decode the compact descriptor to get the item type ID, and other parameters
        itemTypeID, _, _ = parseIntCompactDescr(intCD)
        # Check if the item type is a vehicle
        if itemTypeID == GUI_ITEM_TYPE.VEHICLE:
            # Get the initial vehicle from the progression controller
            vehicle = self.getVehicle()
            # Return a tuple of the vehicle and itself
            return (vehicle, vehicle)
        # If the item is not a vehicle, it should be a module
        module = self.__getProgressionCtrl().getModule(intCD)
        # Get the currently installed module on the vehicle
        currentModule = self.__getProgressionCtrl().getInstalledOnVehicleAnalogByIntCD(intCD)
        # Return a tuple of the module and the current module
        return (module, currentModule)

    # Define the method to get the initial vehicle from the progression controller
    def getVehicle(self):
        return self.__getProgressionCtrl().getInitialVehicle()

    # Define the method to get the progression controller instance
    @dependency.
