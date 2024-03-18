# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/skill_category_base_model.py

# This script defines a ViewModel for a Skill Category in the Frontline game mode.
# ViewModels are used in the MVVM architectural pattern to separate the UI and business logic.

from enum import Enum  # Importing Enum class for defining skill category types
from frameworks.wulf import Array  # Importing Array class for handling arrays of models
from frameworks.wulf import ViewModel  # Base class for all view models

# Define an Enum for SkillCategoryType, which includes three possible categories:
#   - FIRESUPPORT
#   - RECONNAISSANCE
#   - TACTICS
class SkillCategoryType(Enum):
    FIRESUPPORT = 'firesupport'
    RECONNAISSANCE = 'reconnaissance'
    TACTICS = 'tactics'


class SkillCategoryBaseModel(ViewModel):
    # Initialize the class with default properties and commands
    def __init__(self, properties=2, commands=0):
        super(SkillCategoryBaseModel, self).__init__(properties=properties, commands=commands)

    # Getter for the SkillCategoryType
    def getType(self):
        # Return the SkillCategoryType using the ViewModel's _getString method
        return SkillCategoryType(self._getString(0))

    # Setter for the SkillCategoryType
    def setType(self, value):
        # Set the SkillCategoryType using the ViewModel's _setString method
        self._setString(0, value.value)

    # Getter for the skills array
    def getSkills(self):
        # Return the skills array using the ViewModel's _getArray method
        return self._getArray(1)

    # Setter for the skills array
    def setSkills(self, value):
        # Set the skills array
