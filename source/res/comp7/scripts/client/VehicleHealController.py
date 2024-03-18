# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: comp7/scripts/client/VehicleHealController.py

import typing
from helpers import fixed_dict
from script_component.DynamicScriptComponent import DynamicScriptComponent
from view_state_component import ViewStateComponentAdaptor

# A class representing a vehicle heal controller
class VehicleHealController(DynamicScriptComponent):

    def __init__(self):
        # Initialize the superclass
        super(VehicleHealController, self).__init__()
        
        # Initialize an empty dictionary to store adaptors
        self.__adaptors = {}

