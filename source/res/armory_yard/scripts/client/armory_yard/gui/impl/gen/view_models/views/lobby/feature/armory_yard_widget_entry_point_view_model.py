# Python bytecode 3.7 (decompiled from Python 3.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/gen/view_models/views/lobby/feature/armory_yard_widget_entry_point_view_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class State(Enum):
    BEFORE_PROGRESSION = 'beforeProgression'
    ACTIVE = 'active'
    POST_PROGRESSION = 'postProgression'
    COMPLETED = 'completed'
    DISABLED = 'disabled'


class ArmoryYardWidgetEntryPointViewModel(ViewModel):
    """
    View model for Armory Yard widget entry point.
    """
    __slots__ = ('on_action',)

    def __init__(self, properties=5, commands=1):
        super().__init__(properties=properties, commands=commands)

    @property
    def state(self):
        """
        Current state of the entry point.
        :return: State
        """
        return State(self._getString(0))

    @state.setter
    def state(self, value: State):
        self._setString(0, value.value)

    @property
    def start_time(self):
        """
        Start time of the entry point.
        :return: float
        """
        return self._getNumber(1)

    @start_time.setter
    def start_time(self, value: float):
        self._setNumber(1, value)

    @property
    def end_time(self):
        """
        End time of the entry point.
        :return: float
        """
        return self._getNumber(2)

    @end_time.setter
    def end_time(self, value: float):
        self._setNumber(2, value)

    @property
    def current_time(self):
        """
        Current time.
        :return: float
        """
        return self._getNumber(3)

    @current_time.setter
    def current_time(self, value: float):
        self._setNumber(3, value)

    @property
    def is_reward_available(self):
        """
        Indicates if the reward is available.
        :return: bool
        """
        return self._getBool(4)

    @is_reward_available.setter
    def is_reward_available(self, value: bool):
        self._setBool(4, value)

    def _initialize(self):
        super()._initialize()
        self._addStringProperty('state')
        self._addNumberProperty('start
