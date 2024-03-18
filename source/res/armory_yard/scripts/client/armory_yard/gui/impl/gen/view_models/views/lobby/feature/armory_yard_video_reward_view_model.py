# Python bytecode 3.x (to be compiled in Python 3.x)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/gen/view_models/views/lobby/feature/armory_yard_video_reward_view_model.py

class ArmoryYardVideoRewardViewModel(VehicleInfoModel):
    """View model for the armory yard video reward window."""
    __slots__ = (
        'on_close',  # Command called when the window is closed.
        'on_error',  # Command called when an error occurs during video playback.
        'on_show_vehicle',  # Command called when the vehicle is displayed after the video finishes playing.
        'on_video_started',  # Command called when the video starts playing.
        'is_window_accessible',  # Boolean property that determines whether the window is accessible or not.
        'video_name'  # String property that stores the name of the video to be played.
    )
