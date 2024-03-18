# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: gui_lootboxes/scripts/client/gui_lootboxes/gui/impl/gen/view_models/views/lobby/gui_lootboxes/guaranteed_reward_model.py

# This script defines a ViewModel named GuaranteedRewardModel, which is used in the GUI of the loot boxes feature.
# ViewModels are part of the MVVM (Model-View-ViewModel) architectural pattern, serving as an interface
# and data structure between the View (GUI) and Model (business logic).

from frameworks.wulf import Array  # Importing Array class from wulf framework, used for handling arrays in ViewModels
from frameworks.wulf import ViewModel  # Importing ViewModel class from wulf framework, base class for all ViewModels

class GuaranteedRewardModel(ViewModel):
    # GuaranteedRewardModel class inherits from ViewModel, with no additional instance variables.

    def __init__(self, properties=2, commands=0):
        # Initializing the ViewModel with 2 properties and 0 commands.
        super(GuaranteedRewardModel, self).__init__(properties=properties, commands=commands)

    def getLevelsRange(self):
        # A getter method for the 'levelsRange' property, which returns the array stored in the property.
        return self._getArray(0)

    def setLevelsRange(self, value):
        # A setter method for the 'levelsRange' property, which sets the array stored in the property.
        self._setArray(0, value)

    @staticmethod
    def getLevelsRangeType():
        # A static method that returns the type of elements in the 'levelsRange' array.
        return int

    def getBoxesUntilGuaranteedReward(self):
        # A getter method for the 'boxesUntilGuaranteedReward' property, which returns the number stored in the property.
        return self._getNumber(1)

   
