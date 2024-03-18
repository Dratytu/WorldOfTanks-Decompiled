# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/vehicles_slide_model.py

# This script defines a ViewModel class named 'VehiclesSlideModel' using the 'ViewModel' class from the 'frameworks.wulf' package.
# ViewModel is a base class for view models, which are used to store and manage data in the MVP (Model-View-Presenter) pattern.

from frameworks.wulf import ViewModel

class VehiclesSlideModel(ViewModel):
    # The 'VehiclesSlideModel' class inherits from 'ViewModel' and has no additional member variables ('__slots__ = ()').

    def __init__(self, properties=2, commands=0):
        # The constructor takes two optional arguments: 'properties' and 'commands'.
        # 'properties' is the number of properties the view model will have (default is 2).
        # 'commands' is the number of commands the view model will have (default is 0).

        super(VehiclesSlideModel, self).__init__(properties=properties, commands=commands)
        # Calls the constructor of the parent class 'ViewModel' with the given 'properties' and 'commands'.

    def getFromLevel(self):
        # A method to retrieve the value of the 'fromLevel' property.
        return self._getNumber(0)
        # Returns the value of the 'fromLevel' property, which is a number property with index 0.

    def setFromLevel(self, value):
        # A method to set the value of the 'fromLevel' property.
        self._setNumber(0, value)
        # Sets the value of the 'fromLevel' property to the given 'value', which is a number property with index 0.

    def getToLevel(self):
        # A method to retrieve the value of the 'toLevel' property.
        return self._getNumber(1)
        # Returns the value of the
