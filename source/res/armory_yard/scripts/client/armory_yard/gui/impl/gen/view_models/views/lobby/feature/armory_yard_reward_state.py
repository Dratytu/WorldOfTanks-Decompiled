# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/gen/view_models/views/lobby/feature/armory_yard_reward_state.py

# This script defines a ViewModel class named ArmoryYardRewardState, which is used for state management in the Armory Yard feature.
# ViewModels are part of the Wulf framework and are used to manage the state of a view.

from frameworks.wulf import ViewModel  # Importing ViewModel from the Wulf framework

class ArmoryYardRewardState(ViewModel):
    # ArmoryYardRewardState class inherits from ViewModel

    # Define class level constants for the state properties
    STAGE = 'stage'
    STYLE = 'style'

    def __init__(self, properties=0, commands=0):
        # Initialize the ViewModel with the given properties and commands
        super(ArmoryYardRewardState, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        # Called after the ViewModel is initialized.
        # This is where you would initialize any state properties or event handlers.

        super(ArmoryYardRewardState, self)._initialize()
        # Call the parent class's _initialize method to ensure proper initialization.
