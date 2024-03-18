# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutTankCarouselMeta.py

# Import the TankCarousel class from the gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.tank_carousel module
from gui.Scaleform.daapi.view.lobby.hangar.carousels.basic.tank_carousel import TankCarousel

# Define the FalloutTankCarouselMeta class, which inherits from the TankCarousel class
class FalloutTankCarouselMeta(TankCarousel):

    # Define the changeVehicle method, which takes an id parameter
    def changeVehicle(self, id):
        # Print an override error message for the changeVehicle method
        self._printOverrideError('changeVehicle')

    # Define the clearSlot method, which takes a vehicleId parameter
    def clearSlot(self, vehicleId):
        # Print an override error message for the clearSlot method
        self._printOverrideError('clearSlot')

    # Define the shiftSlot method, which takes a vehicleId parameter
    def shiftSlot(self, vehicleId):
        # Print an override error message for the shiftSlot method
        self._printOverrideError('shiftSlot')

    # Define the as_setMultiselectionInfoS method, which takes a data parameter
    def as_setMultiselectionInfoS(self, data):
        # If the DAAPI is initialized, return the result of calling the as_setMultiselectionInfo method on the flashObject with the data parameter
        return self.flashObject.as_setMultiselectionInfo(data) if self._isDAAPIInited() else None

    # Define the as_getMultiselectionDPS method
    def as_getMultiselectionDPS(self):
        # If the DAAPI is initialized, return the result of calling the as_getMultiselectionDP method on the flashObject
        return self.flashObject.as_getMultiselectionDP() if
