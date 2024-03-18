# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/common/fun_random_progression_state.py

import enum
from frameworks.wulf import ViewModel

# Define an enumeration for FunRandomProgressionStatus
class FunRandomProgressionStatus(enum.Enum):
    DISABLED = 'disabled'
    ACTIVE_FINAL = 'activeFinal'
    ACTIVE_RESETTABLE = 'activeResettable'
    COMPLETED_FINAL = 'completedFinal'
    COMPLETED_RESETTABLE = 'completedResettable'

# Define the FunRandomProgressionState view model
class FunRandomProgressionState(ViewModel):
    # Define the slots for the view model
    __slots__ = ()

    # Initialize the view model with the given properties and commands
    def __init__(self, properties=4, commands=0):
        super(FunRandomProgressionState, self).__init__(properties=properties, commands=commands)

        # Initialize the properties of the view model
        self._status = None  # FunRandomProgressionStatus
        self._currentStage = -1  # int
        self._maximumStage = -1  # int
        self._resetTimer = -1  # int

    # Get the current status of the fun random progression
    def getStatus(self):
        return FunRandomProgressionStatus(self._getString(0))

    # Set the status of the fun random progression
    def setStatus(self, value):
        self._setString(0, value.value)

    # Get the current stage of the fun random progression
    def getCurrentStage(self):
        return self._getNumber(1)

    # Set the current stage of the fun random progression
    def setCurrentStage(self, value):
        self._setNumber(1, value)

    # Get the maximum stage of the fun random progression
    def getMaximumStage(self):
        return self._getNumber(2)

    # Set the maximum stage of the fun random progression
    def setMaximumStage(self, value):
        self._setNumber(2, value)

    # Get the reset timer for the fun random progression
    def getResetTimer(self):
        return self._getNumber(3)

    # Set the reset timer for the fun random progression
    def setResetTimer(self, value):
        self._setNumber(3, value
