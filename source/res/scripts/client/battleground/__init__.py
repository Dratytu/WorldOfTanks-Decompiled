# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/battleground/__init__.py

# Import vehicles module which contains classes and functions related to vehicles
from items import vehicles

# Define the author of the code
__author__ = 'a_jorov'

# Define a function to get the Kamikaze equipment description
def getKamikazeEquipmentDescr():
    # Get the equipments dictionary from the vehicles module
    equipments_dict = vehicles.g_cache.equipments()
    
    # Get the equipment ID for Kamikaze from the vehicles module
    kamikaze_equipment_id = vehicles.g_cache.equipmentIDs()['spawn_kamikaze']
    
    # Return the Kamikaze equipment description from the equipments dictionary
    return equipments_dict[kamikaze_equipment_id]
