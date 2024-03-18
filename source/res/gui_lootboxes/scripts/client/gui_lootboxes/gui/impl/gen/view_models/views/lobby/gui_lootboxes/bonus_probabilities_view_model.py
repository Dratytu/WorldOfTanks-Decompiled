# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: gui_lootboxes/scripts/client/gui_lootboxes/gui/impl/gen/view_models/views/lobby/gui_lootboxes/bonus_probabilities_view_model.py

# Import necessary modules
from frameworks.wulf import Array
from frameworks.wulf import ViewModel

# Define the SlotViewModel type for future use
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.slot_view_model import SlotViewModel

# BonusProbabilitiesViewModel class inherits from ViewModel class
class BonusProbabilitiesViewModel(ViewModel):
    # Declare an empty __slots__ attribute to prevent creating unnecessary dictionary for CPython optimizations
    __slots__ = ()

    # Initialize the class with default properties and commands
    def __init__(self, properties=6, commands=0):
        super(BonusProbabilitiesViewModel, self).__init__(properties=properties, commands=commands)

    # Getter for the lootboxName property
    def getLootboxName(self):
        return self._getString(0)

    # Setter for the lootboxName property
    def setLootboxName(self, value):
        self._setString(0, value)

    # Getter for the lootboxTier property
    def getLootboxTier(self):
        return self._getNumber(1)

    # Setter for the lootboxTier property
    def setLootboxTier(self, value):
        self._setNumber(1, value)

    # Getter for the slots property
    def getSlots(self):
        return self._getArray(2)

    # Setter for the slots property
    def setSlots(self, value):
        self._setArray(2, value)

    # Static method to get the SlotViewModel type
    @staticmethod
    def getSlotsType():
        return SlotViewModel

    # Getter for the hasLootLists property
    def getHasLootLists(self):
        return self._getBool(3)

    # Setter for the hasLootLists property
    def setHasLootLists(self, value):
        self._setBool(3, value)

    # Getter for the rotationStage property
    def getRotationStage(self):
        return self._getNumber(4)

    # Setter for the rotationStage property
    def setRotationStage(self, value):
        self._setNumber(4, value)

    # Getter for the lootLists property
    def getLootLists(self):
        return self._getArray(5)

    # Setter for the lootLists property
    def setLootLists(self, value):
        self._setArray(5, value)

    # Static method to get the SlotViewModel type for lootLists
    @staticmethod
    def getLootListsType():
        return SlotViewModel

    #
