# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/test_drive_info_tooltip_view_model.py

# The 'TestDriveInfoTooltipViewModel' class is a ViewModel for the tooltip that displays information about the test drive feature in the lobby.
# It inherits from the 'ViewModel' class and takes two optional arguments: 'properties' and 'commands'.
# 'properties' is an integer that represents the number of properties the ViewModel has, and 'commands' is an integer that represents the number of commands the ViewModel has.
# The class initializes the ViewModel with 2 properties and 0 commands.
class TestDriveInfoTooltipViewModel(ViewModel):
    """View model for the tooltip that displays information about the test drive feature in the lobby."""
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        """
        Initializes the view model with 2 properties and 0 commands.

        :param properties: An integer representing the number of properties the ViewModel has. Defaults to 2.
        :param commands: An integer representing the number of commands the ViewModel has. Defaults to 0.
        """
        super(TestDriveInfoTooltipViewModel, self).__init__(properties=properties, commands=commands)

    # The 'price' property returns the view model for the price of the test drive.
    @property
    def price(self):
        """
        Returns the view model for the price of the test drive.

        :return: The view model for the price of the test drive.
        """
        return self._getViewModel(0)

    # The 'onSomeEvent' method is a placeholder for a command that can be bound to an event.
    # It takes no arguments and returns no value.
    @staticmethod
    @event_handler('some_event')
    def onSome
