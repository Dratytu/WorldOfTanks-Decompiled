# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/frontline_lvl_range_rewards.py

# This script defines a ViewModel for the FrontlineLvlRangeRewards view.
# ViewModels are used in the MVVM architectural pattern to separate the UI and business logic.
# They serve as containers for data and commands that are bound to UI elements.

from frameworks.wulf import Array  # Importing Array from the wulf framework, used for handling arrays in ViewModels
from frameworks.wulf import ViewModel  # Importing ViewModel from the wulf framework, used as a base class for custom ViewModels
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_reward_model import FrontlineRewardModel  # Importing FrontlineRewardModel, used as a type for the 'rewards' array

class FrontlineLvlRangeRewards(ViewModel):
    # The FrontlineLvlRangeRewards class inherits from the ViewModel class and overrides its constructor

    __slots__ = ()  # Declaring an empty __slots__ tuple to save memory by preventing the creation of a dictionary for storing instance variables

    def __init__(self, properties=3, commands=0):
        # The ViewModel constructor is called with two optional arguments: properties and commands
        # properties: The number of properties (instance variables) in the ViewModel
        # commands: The number of commands (functions that can be called from the UI) in the ViewModel
        super(FrontlineLvlRangeRewards, self).__init__(properties=properties, commands=commands)

    def getLvlStart(self):
        # A read-only property that returns the value of the 'lvlStart' instance variable
        return self._getNumber(0)

    def setLvlStart(self, value):
        # A write-only property that sets the value of the 'lvlStart' instance variable

