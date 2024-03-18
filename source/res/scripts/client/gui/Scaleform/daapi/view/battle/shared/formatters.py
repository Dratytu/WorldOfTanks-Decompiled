# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/formatters.py

import math
from debug_utils import LOG_ERROR, LOG_WARNING

# Normalizes health value to be non-negative
def normalizeHealth(health):
    return max(0.0, health)


# Calculates the health percentage of a unit with given health and maximum health
# Parameters:
#   health (float): The current health of the unit
#   max_health (float): The maximum health of the unit
# Returns:
#   float: The health percentage as a value between 0.0 and 1.0
def getHealthPercent(health, maxHealth):
    if not (maxHealth > 0 and maxHealth >= health):
        LOG_WARNING('Maximum health is not valid! health={}, maxHealth={}'.format(health, maxHealth))
        return 0.0
    return float(normalizeHealth(health)) / maxHealth


# Rounds the health percentage to the nearest integer and normalizes it
def normalizeHealthPercent(health, maxHealth):
    return int(math.ceil(getHealthPercent(health, maxHealth) * 100))


# Formats the health and maximum health of a unit as a string
# Parameters:
#   health (float): The current health of the unit
#   max_health (float): The maximum health of the unit
# Returns:
#   str: A string in the format of "<current_health>/<max_health>"
def formatHealthProgress(health, maxHealth):
    if not (maxHealth > 0 and maxHealth >= health):
        LOG_ERROR('Maximum health is not valid! health={}, maxHealth={}'.format(health, maxHealth))
    return '%d/%d' % (normalizeHealth(health), maxHealth)
