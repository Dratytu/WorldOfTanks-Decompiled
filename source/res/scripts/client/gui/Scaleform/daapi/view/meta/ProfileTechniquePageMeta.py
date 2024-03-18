# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileTechniquePageMeta.py

# Import the base ProfileTechnique class from the gui.Scaleform.daapi.view.lobby.profile package
from gui.Scaleform.daapi.view.lobby.profile import ProfileTechnique

# Define the ProfileTechniquePageMeta class, which inherits from the ProfileTechnique class
class ProfileTechniquePageMeta(ProfileTechnique):

    # Define the setIsInHangarSelected method, which overrides the parent class's method
    def setIsInHangarSelected(self, value):
        # Print an error message indicating that this method is overridden and should not be called
        self._printOverrideError('setIsInHangarSelected')

    # Define the as_setSelectedVehicleIntCDS method, which returns an action script command
    def as_setSelectedVehicleIntCDS(self, index):
        # If the DAAPI is initialized, return the as_setSelectedVehicleIntCD action script command with the index parameter
        return self.flashObject.as_setSelectedVehicleIntCD(index) if self._isDAAPIInited() else None

