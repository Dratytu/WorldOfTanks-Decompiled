# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/frontline_const.py

import enum  # For defining custom enumeration classes
from frameworks.wulf import ViewModel  # Base class for all view models

# Define an enumeration class for FrontlineState with the following states:
# ANNOUNCE: The frontline event is being announced
# ACTIVE: The frontline event is currently active
# FINISHED: The frontline event has finished
# FROZEN: The frontline event is in a paused or frozen state
class FrontlineState(enum.Enum):
    ANNOUNCE = 'announce'  # The frontline event is being announced
    ACTIVE = 'active'  # The frontline event is currently active
    FINISHED = 'finished'  # The frontline event has finished
    FROZEN = 'frozen'  # The frontline event is in a paused or frozen state

# Define the FrontlineConst view model class
class FrontlineConst(ViewModel):
    # Define a blank list of slots (class attributes)
    __slots__ = ()

    # Initialize the class with the default properties and commands
    def __init__(self, properties=0, commands=0):
        # Call the ViewModel constructor with the given properties and commands
        super(FrontlineConst, self).__init__(properties=properties, commands=commands)

    # Initialize the view model after the constructor call
    def _initialize(self):
        # Call the ViewModel's _initialize method
        super(FrontlineConst, self)._initialize()

