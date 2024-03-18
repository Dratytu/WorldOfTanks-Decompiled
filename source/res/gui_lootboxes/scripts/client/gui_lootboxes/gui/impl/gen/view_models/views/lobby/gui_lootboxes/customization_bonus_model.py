# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: gui_lootboxes/scripts/client/gui_lootboxes/gui/impl/gen/view_models/views/lobby/gui_lootboxes/customization_bonus_model.py

# Importing the base ItemBonusModel class from a common gen folder
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

# Defining the CustomizationBonusModel class that inherits from ItemBonusModel
class CustomizationBonusModel(ItemBonusModel):
    # Defining a slot wrapper to avoid creating new objects in the __init__ method
    __slots__ = ()

    # Initializing the class with default properties and commands
    def __init__(self, properties=12, commands=0):
        # Calling the parent class constructor
        super(CustomizationBonusModel, self).__init__(properties=properties, commands=commands)

    # A getter method for the customizationID property
    def getCustomizationID(self):
        return self._getNumber(9)

    # A setter method for the customizationID property
    def setCustomizationID(self, value):
        self._setNumber(9, value)

    # A getter method for the item property
    def getItem(self):
        return self._getString(10)

    # A setter method for the item property
    def setItem(self, value):
        self._setString(10, value)

    # A getter method for the icon property
    def getIcon(self):
        return self._getString(11)

    # A setter method for the icon property
    def setIcon(self, value):
        self._setString(11, value)

    # Initialization method called by the parent class constructor
    def _initialize(self):
        # Calling the parent class initialization method
        super(CustomizationBonusModel, self)._initialize()
        # Adding
