# frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/tooltips/not_enough_points_tooltip_model.py

import frameworks.wulf as wulf

class NotEnoughPointsTooltipModel(wulf.ViewModel):
    """
    A view model for the 'Not Enough Points' tooltip in the Frontline lobby.
    This view model handles the display of points that the player needs to progress.
    """
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        """
        Initialize the NotEnoughPointsTooltipModel with the given properties and commands.

        :param properties: The number of properties for this view model.
        :param commands: The number of commands for this view model.
        """
        super(NotEnoughPointsTooltipModel, self).__init__(properties=properties, commands=commands)

    def getPoints(self):
        """
        Get the number of points required for the player to progress.

        :return: The points required.
        """
        return self._getNumber(0)

    def setPoints(self, value):
        """
        Set the number of points required for the player to progress.

        :param value: The points required.
        """
        self._setNumber(0, value)

    def _initialize(self):
        """
        Initialize the properties of the NotEnoughPointsTooltipModel.
        """
        super(NotEnoughPointsTooltipModel, self)._initialize()
        self._addNumberProperty('points', 0)  # The points required for the player to progress.
