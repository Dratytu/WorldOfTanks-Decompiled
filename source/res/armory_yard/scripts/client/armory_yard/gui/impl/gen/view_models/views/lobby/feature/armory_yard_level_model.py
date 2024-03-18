# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/gen/view_models/views/lobby/feature/armory_yard_level_model.py

import frameworks.wulf as wulf # Importing the wulf framework, which is used for creating view models.
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel # Importing the ItemBonusModel, which is used as a type for rewards.

# Defining the ArmoryYardLevelModel class, which inherits from ViewModel.
class ArmoryYardLevelModel(wulf.ViewModel):
    # Defining class-level attributes for properties and commands.
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        # Calling the ViewModel constructor with the given properties and commands.
        super(ArmoryYardLevelModel, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        # A getter method for the level property.
        return self._getNumber(0)

    def setLevel(self, value):
        # A setter method for the level property.
        self._setNumber(0, value)

    def getRewards(self):
        # A getter method for the rewards property.
        return self._getArray(1)

    def setRewards(self, value):
        # A setter method for the rewards property.
        self._setArray(1, value)

    # A class method for getting the type of elements in the rewards array.
    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def _initialize(self):
        # Initializing the view model by calling the ViewModel's _initialize method
        # and setting up properties.
        super(ArmoryYardLevelModel, self)._initialize()
        self._addNumberProperty('level', 
