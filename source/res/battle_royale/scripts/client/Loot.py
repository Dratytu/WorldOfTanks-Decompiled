# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/Loot.py

# Import necessary modules
from battleground.loot_object import loadLootById, ILootObject
from constants import NULL_ENTITY_ID
from entity_game_object import EntityGameObject

# Define the Loot class, which inherits from EntityGameObject
class Loot(EntityGameObject):

    # onEnterWorld method is called when the Loot object enters the world
    def onEnterWorld(self, *args):
        # Call the superclass's onEnterWorld method
        super(Loot, self).onEnterWorld(*args)
        
        # Check if the Loot object has been picked up by an entity
        if self.pickedUpBy != NULL_ENTITY_ID:
            # If it has, call the __onPickup method
            self.__onPickup()

    # set_pickedUpBy method is called when the Loot object is picked up by an entity
    def set_pickedUpBy(self, prev=None):
        # Call the __onPickup method
        self.__onPickup()

    # _loadGameObject method loads the Loot object's data
    def _loadGameObject(self):
        # Load the Loot object's data using the loadLootById function
        lootObj = loadLootById(self.pickupRange, self._registerGameObject, self.typeID)
        # Return the loaded Loot object
        return lootObj

    # __onPickup method is called when the Loot object is picked up by an entity
    def __onPickup(self):
        # Get the ID of the entity that picked up the Loot object
        entityID = self.pickedUpBy
        
        # If the Loot object has a gameObject attribute
        if self.gameObject is not None:
            # Call the processPickup method of the gameObject
            self.gameObject.processPickup(entityID)
        #
