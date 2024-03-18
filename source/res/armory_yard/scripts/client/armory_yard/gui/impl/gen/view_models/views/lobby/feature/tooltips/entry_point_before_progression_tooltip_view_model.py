# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/gen/view_models/views/lobby/feature/tooltips/entry_point_before_progression_tooltip_view_model.py

import frameworks.wulf as wulf # Importing the wulf framework, which is used for creating view models.

# Define a new class 'EntryPointBeforeProgressionTooltipViewModel' that inherits from 'ViewModel' class.
class EntryPointBeforeProgressionTooltipViewModel(wulf.ViewModel):
    # Declare an empty list of slots. This is used to store any additional data that the class needs to store.
    __slots__ = ()

    # Initialize the class with default properties and commands.
    def __init__(self, properties=1, commands=0):
        # Call the constructor of the parent class with the given properties and commands.
        super(EntryPointBeforeProgressionTooltipViewModel, self).__init__(properties=properties, commands=commands)

    # Define a property to get the 'startTimestamp' value.
    def getStartTimestamp(self):
        # Return the value of 'startTimestamp' property.
        return self._getNumber(0)

    # Define a property to set the 'startTimestamp' value.
    def setStartTimestamp(self, value):
        # Set the value of 'startTimestamp' property.
        self._setNumber(0, value)

    # Initialize the properties of the class.
    def _initialize(self):
        # Call the '_initialize' method of the parent class.
        super(EntryPointBeforeProgressionTooltipViewModel, self)._initialize()

        # Add a new number property 'startTimestamp' with a default value of 0.
        self._addNumberProperty('startTimestamp', 0)
