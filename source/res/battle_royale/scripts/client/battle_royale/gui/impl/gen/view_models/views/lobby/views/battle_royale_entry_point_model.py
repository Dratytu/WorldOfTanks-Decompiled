# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/battle_royale_entry_point_model.py

import enum
from frameworks.wulf import ViewModel

# Define an Enum class 'State' with three possible states
class State(enum.Enum):
    ACTIVE = 'active'
    DISABLED = 'disabled'
    ANNOUNCE = 'announce'


# Define the ViewModel class 'BattleRoyaleEntryPointModel' with properties and commands
class BattleRoyaleEntryPointModel(ViewModel):
    __slots__ = ('onClick',)

    # Initialize the class with properties and commands
    def __init__(self, properties=3, commands=1):
        super(BattleRoyaleEntryPointModel, self).__init__(properties=properties, commands=commands)

    # Getter method for the state property
    def getState(self):
        return State(self._getString(0))

    # Setter method for the state property
    def setState(self, value):
        self._setString(0, value.value)

    # Getter method for the timestamp property
    def getTimestamp(self):
        return self._getNumber(1)

    # Setter method for the timestamp property
    def setTimestamp(self, value):
        self._setNumber(1, value)

    # Getter method for the isSingle property
    def getIsSingle(self):
        return self._getBool(2)

    # Setter method for the isSingle property
    def setIsSingle(self, value):
        self._setBool(2, value)

    # Initialize the properties
    def _initialize(self):
        super(BattleRoyaleEntryPointModel, self)._initialize()
        self._addStringProperty('state')  # Add a string property 'state'
        self._addNumberProperty('timestamp', 0)  # Add a number
