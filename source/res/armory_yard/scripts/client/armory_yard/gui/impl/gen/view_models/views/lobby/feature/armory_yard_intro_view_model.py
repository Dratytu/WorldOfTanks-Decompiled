# Python bytecode 3.7 (decompiled from Python 3.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/gen/view_models/views/lobby/feature/armory_yard_intro_view_model.py
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class ArmoryYardIntroViewModel(VehicleInfoModel):
    __slots__ = ('on_close', 'on_continue', 'on_go_back')

    def __init__(self, properties=11, commands=3):
        super().__init__(properties=properties, commands=commands)

    @property
    def start_date(self):
        return self._get_number(8)

    @start_date.setter
    def start_date(self, value):
        self._set_number(8, value)

    @property
    def end_date(self):
        return self._get_number(9)

    @end_date.setter
    def end_date(self, value):
        self._set_number(9, value)

    @property
    def has_intro_video_link(self):
        return self._get_bool(10)

    @has_intro_video_link.setter
    def has_intro_video_link(self, value):
        self._set_bool(10, value)

    def _initialize(self):
        super()._initialize()
        self._add_number_property('start_date', 0)
        self._add_number_property('end_date', 0)
        self._add_bool_property('has_intro_video_link', False)
        self.on_close = self._add_command('on_close')
        self.on_continue = self._add_command('on_continue')
        self.on_go_back = self._add_command('on_go_back')
