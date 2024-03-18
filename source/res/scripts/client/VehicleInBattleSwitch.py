# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/VehicleInBattleSwitch.py

# Importing the 'ARENA_BONUS_TYPE_CAPS' constant from 'arena_bonus_type_caps' module
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS

# Importing the 'ScriptComponent' class from 'script_component.ScriptComponent' module
from script_component.ScriptComponent import ScriptComponent

# Defining the 'VehicleInBattleSwitch' class that inherits from 'ScriptComponent' class
class VehicleInBattleSwitch(ScriptComponent):
    # Class level constant 'REQUIRED_BONUS_CAP' set to 'ARENA_BONUS_TYPE_CAPS.VEHICLE_IN_BATTLE_SELECTION'
    REQUIRED_BONUS_CAP = ARENA_BONUS_TYPE_CAPS.VEHICLE_IN_BATTLE_SELECTION

