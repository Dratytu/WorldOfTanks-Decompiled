# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: gui_lootboxes/scripts/client/gui_lootboxes/gui/impl/gen/view_models/views/lobby/gui_lootboxes/vehicle_bonus_model.py

# Importing Enum class from Python's built-in enum module
from enum import Enum

# Importing ItemBonusModel from a different generated file
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel

# Defining an Enum class named VehicleType with five different vehicle types
class VehicleType(Enum):
    HEAVY = 'heavyTank'
    MEDIUM = 'mediumTank'
    LIGHT = 'lightTank'
    SPG = 'SPG'
    ATSPG = 'AT-SPG'

# Defining a class named VehicleBonusModel, inheriting from ItemBonusModel
class VehicleBonusModel(ItemBonusModel):
    # Defining a list of slot names for the class
    __slots__ = ()

    # Initializing the class with default properties and commands
    def __init__(self, properties=20, commands=0):
        # Calling the constructor of the parent class
        super(VehicleBonusModel, self).__init__(properties=properties, commands=commands)

    # A getter method for the vehicleName attribute
    def getVehicleName(self):
        return self._getString(9)

    # A setter method for the vehicleName attribute
    def setVehicleName(self, value):
        self._setString(9, value)

    # A getter method for the type attribute
    def getType(self):
        return VehicleType(self._getString(10))

    # A setter method for the type attribute
    def setType(self, value):
        self._setString(10, value.value)

    # A getter method for the level attribute
    def getLevel(self):
        return self._getNumber(11)

    # A setter method for the level attribute
    def setLevel(self, value):
        self._setNumber(11, value)

    # A getter method for the shortVehicleLabel attribute
    def getShortVehicleLabel(self):
        return self._getString(12)

    # A setter method for the shortVehicleLabel attribute
    def setShortVehicleLabel(self, value):
        self._setString(12, value)

    # A getter method for the nationTag attribute
    def getNationTag(self):
        return self._getString(13)

    # A setter method for the nationTag attribute
    def setNationTag(self, value):
        self._setString(13, value)

    # A getter method for the isElite attribute
    def getIsElite(self):
        return self._getBool(14)

    # A setter method for the isElite attribute
    def setIsElite(self, value):
        self._setBool(14, value)

    # A getter method for the isRent attribute
    def getIsRent(self):
        return self._getBool(15)

    # A setter method for the isRent attribute
    def setIsRent(self, value):
        self._setBool(15, value)

    # A getter method for the rentDays attribute
    def getRentDays(self):
        return self._getNumber(16)

    # A setter method for the rentDays attribute
    def setRentDays(self, value):
        self._setNumber(16, value)

    # A getter method for the rentBattles attribute
    def getRentBattles(self):
        return self._getNumber(17)

    # A setter method for the rentBattles attribute
    def setRentBattles(self, value):
        self._setNumber(17, value)

    # A getter method for the inInventory attribute
    def getInInventory(self):
        return self._getBool(18)

    # A setter method for the inInventory attribute
    def setInInventory(self, value):
        self._setBool(18, value)

    # A getter method for the wasSold attribute
    def getWasSold
