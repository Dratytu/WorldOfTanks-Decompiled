# Python bytecode 3.x (to be compatible with modern Python versions)

# Importing the Enum class from the built-in enum module
from enum import Enum

# Importing the ViewModel class from the frameworks.wulf module
try:
    from frameworks.wulf import ViewModel
except ImportError:
    # In case the frameworks.wulf module is not found, a simple ViewModel implementation is provided
    class ViewModel:
        def __init__(self, *args, **kwargs):
            pass

        def __call__(self, *args, **kwargs):
            return self


# Defining an enumeration for possible states of the armory yard entry point
class ArmoryYardState(Enum):
    LOCKED = 1
    UNLOCKED = 2
    UPGRADED = 3


# Implementing the ArmoryYardEntryPointViewModel class
class ArmoryYardEntryPointViewModel(ViewModel):

    def __init__(self, state=ArmoryYardState.LOCKED, level=1, is_available_for_purchase=False):
        super(ArmoryYardEntryPointViewModel, self).__init__()
        self._state = state
        self._level = level
        self._is_available_for_purchase = is_available_for_purchase

    # Properties to access the private variables
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def is_available_for_purchase(self):
        return self._is_available_for_purchase

    @is_available_for_purchase.setter
    def is_available_for_purchase(self, value):
        self._is_available_for_purchase = value

