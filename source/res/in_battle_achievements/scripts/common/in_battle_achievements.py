# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: in_battle_achievements/scripts/common/in_battle_achievements.py

# Importing the 'RECORD_DB_IDS' from 'dossiers2.custom.records.records' module
from dossiers2.custom.records import RECORD_DB_IDS

# Defining a constant string for a vehicle tag that disables in-battle achievements
DISABLE_ACHIEVEMENTS_VEHICLE_TAG = 'disableIBA'

# A tuple containing vehicle tags that exclude achievements
EXCLUDED_VEHICLE_TAGS = ('observer', DISABLE_ACHIEVEMENTS_VEHICLE_TAG)

# A dictionary containing enabled achievements with their respective categories as keys
ENABLED_ACHIEVEMENTS = {
    ('achievements', 'kamikaze'): True,
    ('achievements', 'huntsman'): True,
    ('achievements', 'medalPascucci'): True,
    # ... more achievements ...
}

# A dictionary containing enabled achievements with their respective IDs as keys
ENABLED_ACHIEVEMENTS_BY_ID = {
    RECORD_DB_IDS[item]: isEnabled
    for item, isEnabled in ENABLED_ACHIEVEMENTS.iteritems()
}
