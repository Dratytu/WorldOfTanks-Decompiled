# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/Sector.py

from functools import partial
import BigWorld
import MapActivities
from constants import SECTOR_STATE
from debug_utils import LOG_DEBUG
import Math
import items
from ReplayEvents import g_replayEvents

# Mapping of sector location tuples to map activity names
SECTOR_LOCATION_TO_MAP_ACTIVITY = {
    (1, 1): 'zone_destr_WZ1_planes',
    (1, 2): 'zone_destr_WZ2_planes',
    (1, 3): 'zone_destr_WZ3_planes',
    (2, 1): 'zone_destr_CZ1_planes',
    (2, 2): 'zone_destr_CZ2_planes',
    (2, 3): 'zone_destr_CZ3_planes',
    (3, 1): 'zone_destr_EZ1_planes',
    (3, 2): 'zone_destr_EZ2_planes',
    (3, 3): 'zone_destr_EZ3_planes'
}

# Mapping of IDs in player group to map activity lead times
ID_IN_PLAYER_GROUP_TO_MAP_ACTIVITY_LEAD_TIME = {
    1: 2.0,
    2: 2.0,
    3: 23.0
}

# Border visualization dash dimensions
BORDER_VISUALISATION_DASH_DIMENSIONS = (10, 1, 1)

# Border visualization gap length
BORDER_VISUALISATION_GAP_LENGTH = 5

class Sector(BigWorld.Entity):
    """
    A class representing a sector in the game world.
    """

    def __init__(self):
        """
        Initializes a new Sector instance.
        """
        self.__start_destruction_callback = None

    def onEnterWorld(self, prereqs):
        """
        Called when the sector enters the game world.
        """
        g_replay_events.on_time_warp_start += self.__cancel_callback
        sector_component = BigWorld.player().arena.component_system.sector_component
        if sector_component is not None:
            sector_component.add_sector(self)
        self.model = model = BigWorld.Model('')
        model.add_motor(BigWorld.Servo(self.matrix))
        model.visible = True

    def onLeaveWorld(self):
        """
        Called when the sector leaves the game world.
        """
        g_replay_events.on_time_warp_start -= self.__cancel_callback
        self.__cancel_callback()
        sector_component = BigWorld.player().arena.component_system.sector_component
        if sector_component is not None:
            sector_component.remove_sector(self)

    def set_length_x(self, old_value):
        """
        Called when the length of the sector in the X direction is set.
        """
        sector_component = BigWorld.player().arena.component_system.sector_component
        if sector_component is not None:
            sector_component.update_sector(self)

    def set_length_z(self, old_value):
        """
        Called when the length of the sector in the Z direction is set.
        """
        sector_component = BigWorld.player().arena.component_system.sector_component
        if sector_component is not None:
            sector_component.update_sector(self)

    def set_state(self, old_value):
        """
        Called when the state of the sector is set.
        """
        sector_component = BigWorld.player().arena.component_system.sector_component
        if sector_component is not None:
            sector_component.update_sector(self, old_value)
        if self.state is SECTOR_STATE.TRANSITION:
            lead_time = ID_IN_PLAYER_GROUP_TO_MAP_ACTIVITY_LEAD_TIME[self.IDInPlayerGroup]
            delay = max(0, self.transition_time - lead_time)
            self.__start_destruction_callback = BigWorld.callback(delay, partial(self.start_sector_bombing_map_activities, MapActivities.Timer.get_time() + delay))

    def start_sector_bombing_map_activities(self, actual_target_time):
        """
        Called to start the sector bombing map activities.
        """
        self.__cancel_callback()
        actual_time = MapActivities.Timer.get_time()
        time_offset = actual_target_time - actual_time
        if actual_time < actual_target_time:
            self.__start_destruction_callback = BigWorld.callback(time_offset, partial(self.start_sector_bombing_map_activities, actual_target_time))
            return
        map_activity_name = SECTOR_LOCATION_TO_MAP_ACTIVITY[self.player_group, self.IDInPlayerGroup]
        LOG_DEBUG('mapActivityName ', map_activity_name)
        MapActivities.start_activity(map_activity_name, time_offset)

    def show_bomb(self, position):
        """
        Called to show a bomb at the specified position.
        """
        large_effects_index = items.vehicles.g_cache.shot_effects_indexes.get('largeHighExplosive')
        dir_ = Math.Vector3(0.5, 1.0, -0.5)
        self.set_sector_bombing(position, dir_, large_effects_index)

    def set_sector_bombing(self, position, dir_, effects_index):
        """
        Called to set the sector bombing.

