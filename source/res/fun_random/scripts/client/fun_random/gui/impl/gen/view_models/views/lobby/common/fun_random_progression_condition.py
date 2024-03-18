# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/common/fun_random_progression_condition.py

# Import necessary classes and functions from the wulf framework
from frameworks.wulf import Array  # Importing Array class from wulf framework for handling array data structures
from frameworks.wulf import ViewModel  # Importing ViewModel class from wulf framework for creating view models


class FunRandomProgressionCondition(ViewModel):
    """
    A class representing the FunRandomProgressionCondition view model in the lobby.
    Inherits from the ViewModel class provided by the wulf framework.
    """

    def __init__(self, properties=None, **kwargs):
        """
        Initialize the FunRandomProgressionCondition view model.

        :param properties: A dictionary of property values to initialize the view model with
        :param kwargs: Additional keyword arguments to pass to the ViewModel constructor
        """
        super(FunRandomProgressionCondition, self).__init__(properties=properties, **kwargs)

        # Initialize an empty array for storing condition data
        self._conditions = Array()

    @property
    def conditions(self):
        """
        A read-only property that returns the array of condition data.

        :return: The array of condition data
        """
        return self._conditions

    @conditions.setter
    def conditions(self, value):
        """
        A property setter for the conditions array.

        :param value: The new value for the conditions array
        """
        self._conditions.clear()
        self._conditions.extend(value)

    def getConditionType(self, index):
        """
        A method for retrieving the type of a condition at a given index.

        :param index: The index of the condition in the conditions array
        :return: The type of the condition
        """
        return self._conditions.get(index).getType()

    def getConditionValue(self, index):

