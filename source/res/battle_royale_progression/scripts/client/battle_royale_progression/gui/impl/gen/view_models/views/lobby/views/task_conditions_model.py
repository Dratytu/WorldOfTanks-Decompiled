# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale_progression/scripts/client/battle_royale_progression/gui/impl/gen/view_models/views/lobby/views/task_conditions_model.py

from frameworks.wulf import ViewModel  # Import ViewModel from the frameworks.wulf library

class TaskConditionsModel(ViewModel):
    """
    The TaskConditionsModel class represents a view model for task conditions in the Battle Royale Progression lobby.
    """
    __slots__ = ()  # Declare empty __slots__ to save memory by preventing Python from creating __dict__ for the class

    def __init__(self, properties=4, commands=0):
        """
        Initialize the TaskConditionsModel with the given properties and commands.

        :param properties: The number of properties in the view model (default: 4)
        :param commands: The number of commands in the view model (default: 0)
        """
        super(TaskConditionsModel, self).__init__(properties=properties, commands=commands)

    def getCondition(self):
        """
        Get the condition string.

        :return: The condition string
        """
        return self._getString(0)

    def setCondition(self, value):
        """
        Set the condition string.

        :param value: The new condition string
        """
        self._setString(0, value)

    def getLastValue(self):
        """
        Get the last value.

        :return: The last value
        """
        return self._getNumber(1)

    def setLastValue(
