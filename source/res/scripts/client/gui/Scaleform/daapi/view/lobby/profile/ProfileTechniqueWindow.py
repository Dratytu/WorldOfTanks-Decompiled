# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileTechniqueWindow.py

# Import necessary classes and functions
from gui.Scaleform.daapi.view.lobby.profile.QueuedVehicleDossierReceiver import QueuedVehicleDossierReceiver
from gui.Scaleform.daapi.view.lobby.profile.ProfileTechnique import ProfileTechnique

class ProfileTechniqueWindow(ProfileTechnique):

    def __init__(self, *args):
        # Initialize the superclass
        super(ProfileTechniqueWindow, self).__init__(*args)

        # Initialize the data receiver and set the currently requesting vehicle ID
        self.__dataReceiver = QueuedVehicleDossierReceiver()
        self.__currentlyRequestingVehicleId = None

        # Register the data received callback
        self.__dataReceiver.onDataReceived += self.__requestedDataReceived

    def requestData(self, vehicleId):
        # Request data for the specified vehicle ID
        self.as_responseVehicleDossierS(None)
        self.__currentlyRequestingVehicleId = int(vehicleId)
        self.__dataReceiver.invoke(self._databaseID, self.__currentlyRequestingVehicleId)

    def invokeUpdate(self):
        # Invoke the update method of the superclass
        super(ProfileTechniqueWindow, self).invokeUpdate()

        # If a vehicle CD is selected, receive the vehicle dossier
        if self._selectedVehicleIntCD is not None:
            self._receiveVehicleDossier(self._selectedVehicleIntCD, self._databaseID)

    def _dispose(self):
        # Unregister the data received callback, dispose the data receiver, and reset the reference
        self.__dataReceiver.onDataReceived -= self.__requestedDataReceived
        self.__dataReceiver.dispose()
        self.__dataReceiver = None

        # Call the superclass's dispose method
        super(ProfileTechniqueWindow, self)._dispose()

    def _setRatingButton(self):
        # Set the rating button's state
        self.as_setRatingButtonS({'enabled': False,
         'visible': False})

    def __requestedDataReceived(self, databaseID, vehicleID):
        # If the received data matches the currently requesting vehicle ID, receive the vehicle dossier
        if self.__currentlyRequestingVehicleId == vehicleID:
            self._receiveVehicleDossier(vehicleID, databaseID)
