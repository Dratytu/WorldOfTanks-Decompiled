# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/aih_constants.py

# The CTRL_TYPE class defines different types of control modes for the game.
# It includes three types: USUAL, OPTIONAL, and DEVELOPMENT.
class CTRL_TYPE(object):
    USUAL = 0  # Usual control mode.
    OPTIONAL = 1  # Optional control mode.
    DEVELOPMENT = 2  # Development control mode.

# The ShakeReason enumeration defines various reasons for camera shake in the game.
# It includes five reasons: OWN_SHOT, OWN_SHOT_DELAYED, HIT, HIT_NO_DAMAGE, and SPLASH.
class ShakeReason(object):
    OWN_SHOT = 0
    OWN_SHOT_DELAYED = 1
    HIT = 2
    HIT_NO_DAMAGE = 3
    SPLASH = 4

# The CTRL_MODE_NAME class defines various control mode names for the game.
# It includes 17 modes: ARCADE, STRATEGIC, ARTY, SNIPER, POSTMORTEM, DEBUG, CAT, VIDEO,
# MAP_CASE, MAP_CASE_ARCADE, MAP_CASE_EPIC, RESPAWN_DEATH, DEATH_FREE_CAM, DUAL_GUN,
# MAP_CASE_ARCADE_EPIC_MINEFIELD, VEHICLES_SELECTION, and SPG_ONLY_ARTY_MODE.
class CTRL_MODE_NAME(object):
    ARCADE = 'arcade'  # Arcade control mode.
    STRATEGIC = 'strategic'  # Strategic control mode.
    ARTY = 'arty'  # Artillery control mode.
    SNIPER = 'sniper'  # Sniper control mode.
    POSTMORTEM = 'postmortem'  # Postmortem control mode.
    DEBUG = 'debug'  # Debug control mode.
    CAT = 'cat'  # Cat control mode.
    VIDEO = 'video'  # Video control mode.
    MAP_CASE = 'mapcase'  # Map case control mode.
    MAP_CASE_ARCADE = 'arcadeMapcase'  # Arcade map case control mode.
    MAP_CASE_EPIC = 'epicMapcase'  # Epic map case control mode.
    RESPAWN_DEATH = 'respawn'  # Respawn death control mode.
    DEATH_FREE_CAM = 'deathfreecam'  # Death free cam control mode.
    DUAL_GUN = 'dualgun'  # Dual gun control mode.
    MAP_CASE_ARCADE_EPIC_MINEFIELD = 'arcadeEpicMinefieldMapcase'  # Arcade epic minefield map case control mode.
    VEHICLES_SELECTION = 'vehiclesSelection'  # Vehicles selection control mode.
    SPG_ONLY_ARTY_MODE = 'spgOnlyArtyMode'  # SPG only arty mode control mode.
    DEFAULT = ARCADE  # Default control mode (arcade).

# The CTRL_MODES tuple contains all possible control mode names.
CTRL_MODES = (CTRL_MODE_NAME.ARCADE,
              CTRL_MODE_NAME.STRATEGIC,
              CTRL_MODE_NAME.ARTY,
              CTRL_MODE_NAME.SNIPER,
              CTRL_MODE_NAME.POSTMORTEM,
              CTRL_MODE_NAME.DEBUG,
              CTRL_MODE_NAME.CAT,
              CTRL_MODE_NAME.VIDEO,
              CTRL_MODE_NAME.MAP_CASE,
              CTRL_MODE_NAME.MAP_CASE_ARCADE,
              CTRL_MODE_NAME.MAP_
