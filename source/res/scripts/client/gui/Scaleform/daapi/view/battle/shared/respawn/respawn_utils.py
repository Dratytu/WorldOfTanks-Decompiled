# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/respawn/respawn_utils.py

# Import necessary modules
import BigWorld
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS
from helpers import time_utils

# Define the template for flag icons
FLAG_ICON_TEMPLATE = '../maps/icons/battle/respawn/optimize_flags_160x100/%s.png'

# Define the template for vehicle type icons
VEHICLE_TYPE_TEMPLATE = '../maps/icons/vehicleTypes/%s.png'
VEHICLE_ELITE_TYPE_TEMPLATE = '../maps/icons/vehicleTypes/elite/%s.png'

# Define the format for displaying premium vehicle names
VEHICLE_FORMAT = makeHtmlString('html_templates:igr/premium-vehicle', 'name', {})

def getVehicleName(vehicle):
    """
    Return the name of the given vehicle.
    If the vehicle is a premium IGR vehicle, the name will be formatted
    as an IGR premium vehicle.
    """
    tags = vehicle.type.tags
    isIGR = bool(VEHICLE_TAGS.PREMIUM_IGR in tags)
    vehicleName = vehicle.type.shortUserString if isIGR else vehicle.type.userString
    if isIGR:
        vehicleName = VEHICLE_FORMAT % {'vehicle': vehicleName}
    return vehicleName


def getSlotsStatesData(vehs, cooldowns, disabled, limits={}):
    """
    Return a list of dictionaries containing information about the state of each vehicle slot.
    Each dictionary contains the following keys:
    - vehicleID: the compact description of the vehicle
    - enabled: whether the slot is enabled or not
    - cooldown: the cooldown time as a string
    - settings: the settings of the vehicle
    """
    result = []
    for v in vehs.itervalues():
        compactDescr = v.intCD
        cooldownTime = cooldowns.get(compactDescr, 0)
        cooldownStr = ''
        cooldown = cooldownTime - BigWorld.serverTime()
        enabled = cooldown <= 0 and not disabled and compactDescr not in limits
        if not enabled:
            if cooldown > 0:
                if disabled:
                    cooldownStr = backport.text(R.strings.ingame_gui.respawnView.disabledLbl())
                else:
                    cooldownStr = backport.text(R.strings.ingame_gui.respawnView.cooldownLbl(), time=time_utils.getTimeLeftFormat(cooldown))
            else:
                cooldownStr = backport.text(R.strings.ingame_gui.
