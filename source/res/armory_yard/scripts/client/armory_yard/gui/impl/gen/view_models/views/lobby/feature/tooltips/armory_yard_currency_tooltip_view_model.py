# Python bytecode 3.8 (decompiled from Python 3.8)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/gen/view_models/views/lobby/feature/tooltips/armory_yard_currency_tooltip_view_model.py
from frameworks.wulf import ViewModel

class ArmoryYardCurrencyTooltipViewModel(ViewModel):
    """View model for the Armory Yard currency tooltip."""

    __slots__ = ()

    def __init__(self, properties: int = 5, commands: int = 0):
        """
        Initialize the view model.

        :param properties: The number of properties in the view model.
        :param commands: The number of commands in the view model.
        """
        super().__init__(properties=properties, commands=commands)

    def get_received_tokens(self) -> int:
        """
        Get the number of received tokens.

        :return: The number of received tokens.
        """
        return self._get_number(0)

    def set_received_tokens(self, value: int) -> None:
        """
        Set the number of received tokens.

        :param value: The number of received tokens.
        """
        self._set_number(0, value)

    def get_total_tokens(self) -> int:
        """
        Get the total number of tokens.

        :return: The total number of tokens.
        """
        return self._get_number(1)

    def set_total_tokens(self, value: int) -> None:
        """
        Set the total number of tokens.

        :param value: The total number of tokens.
        """
        self._set_number(1, value)

    def get_quests_for_token(self) -> int:
        """
        Get the number of quests for a token.

        :return: The number of quests for a token.
        """
        return self._get_number(2)

    def set_quests_for_token(self, value: int) -> None:
        """
        Set the number of quests for a token.

        :param value: The number of quests for a token.
        """
        self._set_number(2, value)

    def get_start_
