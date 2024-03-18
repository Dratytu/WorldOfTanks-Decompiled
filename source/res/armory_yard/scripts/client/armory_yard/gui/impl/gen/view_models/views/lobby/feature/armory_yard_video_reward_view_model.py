# Python bytecode 3.x (to be compiled in Python 3.x)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/gen/view_models/views/lobby/feature/armory_yard_video_reward_view_model.py
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class ArmoryYardVideoRewardViewModel(VehicleInfoModel):
    __slots__ = ('on_close', 'on_error', 'on_show_vehicle', 'on_video_started', 'is_window_accessible', 'video_name')

    def __init__(self, properties=10, commands=4):
        super().__init__(properties=properties, commands=commands)

    def get_is_window_accessible(self):
        return self._get_bool(self.is_window_accessible.get())

    def set_is_window_accessible(self, value):
        self.is_window_accessible.set(value)

    def get_video_name(self):
        return self._get_string(self.video_name.get())

    def set_video_name(self, value):
        self.video_name.set(value)

    def _initialize(self):
        super()._initialize()
        self.is_window_accessible = self._add_bool_property('isWindowAccessible', True)
        self.video_name = self._add_string_property('videoName', '')
        self.on_close = self._add_command('onClose')
        self.on_error = self._add_command('onError')
        self.on_show_vehicle = self._add_command('onShowVehicle')
        self.on_video_started = self._add_command('onVideoStarted')
