# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/common/fun_random_progression_stage.py

# This file defines the `FunRandomProgressionStage` class, which is a ViewModel for the fun random progression stage.
# ViewModels are used in the MVVM architectural pattern to separate the graphical user interface from the business logic.
# A ViewModel acts as an intermediary between the View (graphical interface) and the Model (business logic).

from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel  # Importing the ItemBonusModel class for the rewards property.

class FunRandomProgressionStage(ViewModel):
    # The FunRandomProgressionStage class inherits from the ViewModel class, which provides basic functionality for ViewModels.

    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        # Initialize the FunRandomProgressionStage class with the given properties and commands.
        # The properties are the attributes of the class, and the commands are the methods that can be called from the View.

        super(FunRandomProgressionStage, self).__init__(properties=properties, commands=commands)

    def getCurrentPoints(self):
        # A method to get the current points of the progression stage.
        return self._getNumber(0)

    def setCurrentPoints(self, value):
        # A method to set the current points of the progression stage.
        self._setNumber(0, value)

    def getMaximumPoints(self):
        # A method to get the maximum points of the progression stage.
        return self._getNumber(1)

    def setMaximumPoints(self, value):
        # A method to set the maximum points of the progression stage.
        self._setNumber(1, value
