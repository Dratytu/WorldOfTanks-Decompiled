# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bootcamp/BootcampConstants.py

# The starting distance of the camera from the player's tank in the bootcamp.
CAMERA_START_DISTANCE = 12

# Class representing the different states of the UI in the bootcamp.
class UI_STATE(object):
    # The initial state of the UI.
    INIT = 1
    # The state of the UI when the battle is starting.
    START = 2
    # The state of the UI when the battle is being updated.
    UPDATE = 3
    # The state of the UI when the battle is stopping.
    STOP = 4


# Class representing the different tooltips for battle stats in the bootcamp.
class BATTLE_STATS_TOOLTIPS(object):
    # The tooltip for destroyed enemies.
    DESTROYED = 'destroyed'
    # The tooltip for damage dealt.
    DAMAGE = 'damage'
    # The tooltip for damage blocked.
    BLOCKED = 'blocked'
    # The tooltip for enemies detected.
    DETECTED = 'detected'
    # The tooltip for damage assisted.
    ASSISTED = 'assisted'

# A dictionary mapping battle stat tooltips to their corresponding result fields.
BATTLE_STATS_RESULT_FIELDS = {
    BATTLE_STATS_TOOLTIPS.DESTROYED: 'kills',
    BATTLE_STATS_TOOLTIPS.DAMAGE: 'damageDealt',
    BATTLE_STATS_TOOLTIPS.BLOCKED: 'damageBlockedByArmor',
    BATTLE_STATS_TOOLTIPS.DETECTED: 'spotted',
    BATTLE_STATS_TOOLTIPS.ASSISTED: 'damageAssisted'
}
# A dictionary mapping battle stat tooltips to their corresponding icons.
BATTLE_STATS_ICONS = {
    BATTLE_STATS_TOOLTIPS.DESTROYED: 'statIconDestroyed',
    BATTLE_STATS_TOOLTIPS.DAMAGE: 'statIconDamage',
    BATTLE_STATS_TOOLTIPS.BLOCKED: 'statIconBlocked',
    BATTLE_STATS_TOOLTIPS.DETECTED: 'statIconDetected',
    BATTLE_STATS_TOOLTIPS.ASSISTED: 'statIconAssisted'
}
# A tuple of error messages related to consumables.
CONSUMABLE_ERROR_MESSAGES = (
    'repairkitAllDevicesAreNotDamaged',  # Error message for repair kit when all devices are not damaged.
    'repairkitDeviceIsNotDamaged',  # Error message for repair kit when a device is not damaged.
    'medkitAllTankmenAreSafe',  # Error message for medkit when all tankmen are safe.
    'medkitTankmanIsSafe',  # Error message for medkit when a tankman is safe.
    'extinguisherDoesNotActivated'  # Error message for extinguisher when it does not activate.
)

# Class representing the different types of hints in the bootcamp.
class HINT_TYPE(object):
    # The hint type for moving the tank.
    HINT_MOVE = 0
    # The hint type for moving the turret.
    HINT_MOVE_TURRET = 1
    # The hint type for shooting.
    HINT_SHOOT = 2
    # The hint type for advanced sniper mode.
    HINT_ADVANCED_SNIPER = 3
    # The hint type for aiming.
    HINT_AIM = 4
    # The hint type for sniper mode.
    HINT_SNIPER = 5
    # The hint type for weak points.
    HINT_WEAK_POINTS = 6
    # The hint type for avoiding certain actions.
    HINT_MESSAGE_AVOID = 7
    # The hint type for when the player is spotted.
    HINT_MESSAGE_PLAYER_SPOTTED = 8
    # The hint type for clearing a sector.
    HINT_SECTOR_CLEAR = 9
    # The hint type for starting the narrative.
    HINT_START_NARRATIVE = 10
    # The hint type for capturing the base.
    HINT_MESSAGE_CAPTURE_THE_BASE = 11
    # The hint type for resetting progress.
    HINT_MESSAGE_RESET_PROGRESS = 12
    # The hint type for repairing the track.
    HINT_REPAIR_TRACK = 13
    # The hint type for healing the crew.
    HINT_HEAL_CREW = 14
    # The hint type for using the extinguisher.
    HINT_USE_EXTINGUISHER = 15
    # The hint type for shooting at allies.
    HINT_SHOOT_ALLY = 16
    # The hint type for detecting enemies.
    HINT_PLAYER_DETECT_ENEMIES = 17
    # The hint type for exiting the game area.
    HINT_EXIT_GAME_AREA = 18
    # The hint type for when enemies can hide.
    HINT_MESSAGE_ENEMY_CAN_HIDE = 19
    # The hint type for sneaking.
    HINT_MESSAGE_SNEAK = 20
    # The hint type for sniper mode on distance.
    HINT_SNIPER_ON_DISTANCE = 21
    # The hint type for rotating the lobby.
    HINT_ROTATE_LOBBY = 22
    # The hint type for target lock.
    HINT_TARGET_LOCK = 23
    # The hint type for waiting for reload.
    HINT_WAIT_RELOAD = 24
    # The hint type for not moving.
    HINT_NO_MOVE = 25
    # The hint type for not moving
