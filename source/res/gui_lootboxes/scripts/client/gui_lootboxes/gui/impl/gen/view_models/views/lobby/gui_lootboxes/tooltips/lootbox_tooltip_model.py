# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: gui_lootboxes/scripts/client/gui_lootboxes/gui/impl/gen/view_models/views/lobby/gui_lootboxes/tooltips/lootbox_tooltip_model.py

import frameworks.wulf as wulf # Importing ViewModel from the wulf framework

# Define a new class LootboxTooltipModel that inherits from ViewModel
class LootboxTooltipModel(wulf.ViewModel):
    # Declare an empty list of slots
    __slots__ = ()

    # Initialize the class with default properties and commands
    def __init__(self, properties=4, commands=0):
        # Call the ViewModel constructor with the given properties and commands
        super(LootboxTooltipModel, self).__init__(properties=properties, commands=commands)

    # Getter for userNameKey property
    def getUserNameKey(self):
        return self._getString(0)

    # Setter for userNameKey property
    def setUserNameKey(self, value):
        self._setString(0, value)

    # Getter for descriptionKey property
    def getDescriptionKey(self):
        return self._getString(1)

    # Setter for descriptionKey property
    def setDescriptionKey(self, value):
        self._setString(1, value)

    # Getter for tier property
    def getTier(self):
        return self._getNumber(2)

    # Setter for tier property
    def setTier(self, value):
        self._setNumber(2, value)

    # Getter for count property
    def getCount(self):
        return self._getNumber(3)

    # Setter for count property
    def setCount(self, value):
        self._setNumber(3, value)

    # Initialize the object with default values
    def _initialize(self):
        # Call the ViewModel's initialization
        super(LootboxTooltipModel, self)._
