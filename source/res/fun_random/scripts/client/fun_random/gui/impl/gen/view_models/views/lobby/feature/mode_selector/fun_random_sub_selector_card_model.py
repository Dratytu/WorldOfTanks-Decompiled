# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/feature/mode_selector/fun_random_sub_selector_card_model.py

import enum  # For creating custom enumeration classes
from frameworks.wulf import Array  # For handling arrays in the view model
from frameworks.wulf import ViewModel  # Base class for view models

# Define a custom enumeration for CardState
class CardState(enum.IntEnum):
    NOT_STARTED = 0  # The card state is not started
    ACTIVE = 1  # The card state is active
    DISABLED = 2  # The card state is disabled
    FINISHED = 3  # The card state is finished

# Subclass ViewModel to create the FunRandomSubSelectorCardModel
class FunRandomSubSelectorCardModel(ViewModel):
    # Define the private slots for the model
    __slots__ = ()

    # Initialize the FunRandomSubSelectorCardModel
    def __init__(self, properties=8, commands=0):
        super(FunRandomSubSelectorCardModel, self).__init__(properties=properties, commands=commands)

    # Getter for the assetsPointer property
    def getAssetsPointer(self):
        return self._getString(0)

    # Setter for the assetsPointer property
    def setAssetsPointer(self, value):
        self._setString(0, value)

    # Getter for the subModeId property
    def getSubModeId(self):
        return self._getNumber(1)

    # Setter for the subModeId property
    def setSubModeId(self, value):
        self._setNumber(1, value)

    # Getter for the conditions property
    def getConditions(self):
        return self._getString(2)

    # Setter for the conditions property
    def setConditions(self, value):
        self._setString(2, value)

    # Getter for the state property
    def getState(self):
        return CardState(self._getNumber(3))

    # Setter for the state property
    def setState(self, value):
        self._setNumber(3, value.value)

    # Getter for the isSelected property
    def getIsSelected(self):
        return self._getBool(4)

    # Setter for the isSelected property
    def setIsSelected(self, value):
        self._setBool(4, value)

    # Getter for the timeLeft property
    def getTimeLeft(self):
        return self._getString(5)

    # Setter for the timeLeft property
    def setTimeLeft(self, value):
        self._setString(5, value)

    # Getter for the timeToStart property
    def getTimeToStart(self):
        return self._getNumber(6)

    # Setter for the timeToStart property
    def setTimeToStart(self, value):
        self._setNumber(6, value)

    # Getter for the modifiersDomains property
    def getModifiersDomains(self):
        return self._getArray(7)

    # Setter for the modifiersDomains property
    def setModifiersDomains(self, value):
        self._setArray(7, value)

    # Static method to define the type of modifiersDomains
    @staticmethod
    def getModifiersDomainsType():
        return unicode

    # Initialize the properties of the model
    def _initialize(self):
        super(FunRandomSubSelectorCardModel, self)._initialize()
        self._addStringProperty('assetsPointer', '')
