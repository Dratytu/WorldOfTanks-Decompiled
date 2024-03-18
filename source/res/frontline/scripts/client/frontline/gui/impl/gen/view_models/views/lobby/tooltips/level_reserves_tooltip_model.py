# frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/tooltips/level_reserves_tooltip_model.py

import frameworks.wulf as wulf

class LevelReservesTooltipModel(wulf.ViewModel):
    """
    A view model for the level reserves tooltip in the Frontline lobby.

    This view model is responsible for storing and managing data related to the level reserves,
    such as the list of levels and their corresponding reserves.

    Attributes:
        levels (Array[unicode]): An array of strings representing the levels and their corresponding reserves.
    """
    def __init__(self, properties=1, commands=0):
        """
        Initialize the LevelReservesTooltipModel with the given properties and commands.

        Args:
            properties (int): The number of properties for this view model.
            commands (int): The number of commands for this view model.
        """
        super(LevelReservesTooltipModel, self).__init__(properties=properties, commands=commands)

    def getLevels(self):
        """
        Get the list of levels and their corresponding reserves.

        Returns:
            Array[unicode]: An array of strings representing the levels and their corresponding reserves.
        """
        return self._getArray(0)

    def setLevels(self, value):
        """
        Set the list of levels and their corresponding reserves.

        Args:
            value (Array[unicode]): An array of strings representing the levels and their corresponding reserves.
        """
        self._setArray(0, value)

    @staticmethod
    def getLevelsType():
        """
        Get the type of the levels array.

        Returns:
            type: The type of the levels array, which is unicode.
        """
        return unicode

    def _initialize(self):
        """
        Initialize the view model by setting up its properties.
        """
        super(LevelReservesTooltipModel, self)._initialize()
        self._addArrayProperty('level
