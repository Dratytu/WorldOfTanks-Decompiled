# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/frontline_reward_model.py

# Importing Enum class from the built-in enum module for defining claim states
from enum import Enum

# Importing IconBonusModel from a separate file, which is a ViewModel for icon bonuses
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

# Defining an Enum class named ClaimState with two states: STATIC and CLAIMABLE
class ClaimState(Enum):
    STATIC = 'static'
    CLAIMABLE = 'claimable'


# Defining FrontlineRewardModel, a subclass of IconBonusModel, with no additional instance variables
class FrontlineRewardModel(IconBonusModel):
    # Defining a slot to prevent the creation of __dict__ and __weakref__ for each instance
    __slots__ = ()

    # Initializing the FrontlineRewardModel class with default properties and commands
    def __init__(self, properties=11, commands=0):
        # Calling the constructor of the superclass with the given properties and commands
        super(FrontlineRewardModel, self).__init__(properties=properties, commands=commands)

    # A property method to get the reward's unique identifier
    def getId(self):
        return self._getString(8)

    # A property method to set the reward's unique identifier
    def setId(self, value):
        self._setString(8, value)

    # A property method to get the claim state of the reward
    def getClaimState(self):
        return ClaimState(self._getString(9))

    # A property method to set the claim state of the reward
    def setClaimState(self, value):
        self._setString(9, value.value)

    # A property method to get the
