# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/minimap/settings.py

# Define a class for Battle Royale specific entries in the minimap
class BattleRoyaleEntries(object):
    # Constant for Death Zone entry
    BATTLE_ROYALE_DEATH_ZONE = 'DeathZoneEntry'

    # Constant for View Range Sector entry
    VIEW_RANGE_SECTOR = 'ViewRangeSectorEntry'

    # Constant for Battle Royale Marker
    BATTLE_ROYALE_MARKER = 'BRMarkerUI'


# Define a class for View Range Sector related AS3 descriptions
class ViewRangeSectorAs3Descr(object):
    # Constant for adding a sector
    AS_ADD_SECTOR = 'as_addSector'

    # Constant for updating sector radius
    AS_UPDATE_SECTOR_RADIUS = 'as_updateSectorRadius'

    # Constant for initializing arena size
    AS_INIT_ARENA_SIZE = 'as_initArenaSize'


# Define a class for Death Zones related AS3 descriptions
class DeathZonesAs3Descr(object):
    # Constant for updating death zones
    AS_UPDATE_DEATH_ZONES = 'as_updateDeathZones'

    # Constant for initializing death zone size
    AS_INIT_DEATH_ZONE_SIZE = 'as_initDeathZoneSize'


# Define a class for Markers related AS3 descriptions
class MarkersAs3Descr(object):
    # Constant for updating radar radius
    AS_UPDATE_RADAR_RADIUS = 'updateRadarRadius'

    # Constant for playing radar animation
    AS_PLAY_RADAR_ANIMATION = 'play'

    # Constant for updating marker
    AS_UPDATE_MARKER = 'updateIcon'

    # Constant for adding marker
    AS_ADD_MARKER = 'show'

    # Constant for removing marker
    AS_REMOVE_MARKER = 'hide'

    # Dictionary for adding loot marker by type ID
    AS_ADD_MARKER_LOOT_BY_TYPE_ID = {
        LOOT_TYPE.BASIC: 'loot',          # Basic loot
        LO
