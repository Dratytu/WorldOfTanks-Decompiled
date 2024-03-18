# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: gui_lootboxes/scripts/client/gui_lootboxes/gui/impl/gen/view_models/views/lobby/gui_lootboxes/dog_tag_bonus_model.py

# Importing the Enum class from Python's built-in enum module
from enum import IntEnum

# Importing IconBonusModel from a separate generated file
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

# Defining an Enum class named DogTagType with two constants: ENGRAVING and BACKGROUND
class DogTagType(IntEnum):
    ENGRAVING = 0
    BACKGROUND = 1

# Defining a class named DogTagBonusModel, inheriting from IconBonusModel
class DogTagBonusModel(IconBonusModel):
    # Defining a empty tuple for slots to prevent addition of new attributes
    __slots__ = ()

    # Initializing the class with default properties and commands
    def __init__(self, properties=9, commands=0):
        # Calling the constructor of the superclass with the given properties and commands
        super(DogTagBonusModel, self).__init__(properties=properties, commands=commands)

    # A property method to get the dogTagType attribute
    def getDogTagType(self):
        # Returning the dogTagType attribute as a DogTagType enum instance
        return DogTagType(self._getNumber(8))

    # A property method to set the dogTagType attribute
    def setDogTagType(self, value):
        # Validating the input value as a DogTagType enum instance and setting the attribute
        self._setNumber(8, value.value)

    # Initializing the view model by adding a number property named 'dogTagType'
    def _initialize(self):
        # Calling the initialization method of the superclass
        super(DogTagBonusModel, self)._
