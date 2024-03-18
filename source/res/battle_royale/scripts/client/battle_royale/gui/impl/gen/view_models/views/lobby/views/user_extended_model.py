# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/user_extended_model.py

# This script defines a UserExtendedModel class that inherits from UserModel class.
# The UserExtendedModel class extends the UserModel class by adding two new properties:
# 'vehicleType' and 'vehicleName'.

from battle_royale.gui.impl.gen.view_models.views.lobby.views.user_model import UserModel

class UserExtendedModel(UserModel):
    # Declare empty slots to improve memory usage and performance.
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        # Call the constructor of the superclass with the given properties and commands.
        super(UserExtendedModel, self).__init__(properties=properties, commands=commands)

    def getVehicleType(self):
        # Return the value of the 'vehicleType' string property.
        return self._getString(3)

    def setVehicleType(self, value):
        # Set the value of the 'vehicleType' string property.
        self._setString(3, value)

    def getVehicleName(self):
        # Return the value of the 'vehicleName' string property.
        return self._getString(4)

    def setVehicleName(self, value):
        # Set the value of the 'vehicleName' string property.
        self._setString(4, value)

    def _initialize(self):
        # Initialize the UserExtendedModel instance by calling the _initialize() method
        # of the superclass and adding two new string properties: 'vehicleType' and 'vehicleName'.
        super(UserExtendedModel, self)._initialize()
        self._addStringProperty('vehicleType', '')
        self._addStringProperty('vehicleName', '')

