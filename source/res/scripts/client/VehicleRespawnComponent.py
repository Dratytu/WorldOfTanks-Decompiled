# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/VehicleRespawnComponent.py

import Event # Importing Event module for creating and handling events
from script_component.DynamicScriptComponent import DynamicScriptComponent # Importing DynamicScriptComponent for inheritance

class VehicleRespawnComponent(DynamicScriptComponent): # Defining a class named VehicleRespawnComponent that inherits from DynamicScriptComponent
    onSetSpawnTime = Event.Event() # Creating an event named onSetSpawnTime

    def chooseSpawnGroup(self, groupName):
        """
        A method to choose a spawn group by specifying its name.
        :param groupName: The name of the spawn group
        """
        self.cell.chooseSpawnGroup(groupName) # Calling the chooseSpawnGroup method of the cell object

    def set_spawnTime(self, prev):
        """
        A method to set the spawn time for the entity.
        :param prev: Previous spawn time
        """
        self.onSetSpawnTime(self.entity.id, self.spawnTime) # Triggering the onSetSpawnTime event with the entity id and spawn time
