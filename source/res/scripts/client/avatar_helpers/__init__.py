# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/avatar_helpers/__init__.py

import BigWorld  # Import the BigWorld module for accessing player and arena information
from shared_utils.avatar_helpers import VehicleTelemetry  # Import VehicleTelemetry class from shared_utils.avatar_helpers

# Function to get the avatar's database ID
def getAvatarDatabaseID():
    dbID = 0  # Initialize the database ID
    player = BigWorld.player()  # Get the player object
    arena = getattr(player, 'arena', None)  # Get the arena object from the player object
    if arena is not None:  # If the arena object exists
        vehID = getattr(player, 'playerVehicleID', None)  # Get the player's vehicle ID
        if vehID is not None and vehID in arena.vehicles:  # If the vehicle ID exists and is in the arena's vehicles
            dbID = arena.vehicles[vehID]['accountDBID']  # Get the database ID from the arena's vehicles
    return dbID  # Return the database ID


# Function to get the avatar's session ID
def getAvatarSessionID():
    player = BigWorld.player()  # Get the player object
    avatarSessionID = getattr(player, 'sessionID', '')  # Get the session ID from the player object
    return avatarSessionID  # Return the session ID


# Function to get the best shot result sound
def getBestShotResultSound(currBest, newSoundName, otherData):
    newSoundPriority = _shotResultSoundPriorities[newSoundName]  # Get the priority of the new sound
    if currBest is None:  # If there is no current best sound
        return (newSoundName, otherData, newSoundPriority)  # Return the new sound as the best
    else:
        return (newSoundName, otherData, newSoundPriority) if newSoundPriority > currBest[2] else currBest  # Otherwise, return the new sound if its priority is higher than the current best


# Dictionary of shot result sound priorities
_shotResultSoundPriorities = {'enemy_hp_damaged_by_projectile_and_gun_damaged_by_player': 12,
                              'enemy_hp_damaged_by_projectile_and_chassis_damaged_by_player': 11,
                              'enemy_hp_damaged_by_projectile_by_player': 10,
                              'enemy_hp_damaged_by_explosion_at_direct_hit_by_player': 9,
                              'enemy_hp_damaged_by_near_explosion_by_player': 8,
                              'enemy_no_hp_damage_at_attempt_and_gun_damaged_by_player': 7,
                             
