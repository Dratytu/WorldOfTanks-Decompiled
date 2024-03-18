# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/Comp7BattleStatisticDataControllerMeta.py

# Import the ClassicStatisticsDataController class from the gui.Scaleform.daapi.view.battle.classic.stats_exchange module
from gui.Scaleform.daapi.view.battle.classic.stats_exchange import ClassicStatisticsDataController

# Define the Comp7BattleStatisticDataControllerMeta class, which inherits from the ClassicStatisticsDataController class
class Comp7BattleStatisticDataControllerMeta(ClassicStatisticsDataController):

    # Define the as_removePointOfInterestS method, which takes two arguments: vehicleID (an integer) and type (a string)
    def as_removePointOfInterestS(self, vehicleID, type):
        # If the DAAPI is initialized, call the as_removePointOfInterest method on the flashObject with the provided arguments
        return self.flashObject.as_removePointOfInterest(vehicleID, type) if self._isDAAPIInited() else None

    # Define the as_updatePointOfInterestS method, which takes one argument: data (a dictionary)
    def as_updatePointOfInterestS(self, data):
        # If the DAAPI is initialized, call the as_updatePointOfInterest method on the flashObject with the provided arguments
        return self.flashObject.as_updatePointOfInterest(data) if self._isDAAPIInited() else None

