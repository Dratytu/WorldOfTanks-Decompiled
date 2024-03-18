# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/QueuedVehicleDossierReceiver.py

import time
from Event import Event  # A class to create and handle custom events.
from adisp import adisp_process  # A decorator to process asynchronous tasks.
from debug_utils import LOG_ERROR  # A function to log errors.
from helpers import dependency  # A decorator to declare dependencies.
from skeletons.gui.shared import IItemsCache  # An interface for shared gui components.

# Constants
MIN_INTERVAL_BETWEEN_INVOKES = 300  # Minimum time interval between requests in milliseconds.

class QueuedVehicleDossierReceiver(object):
    itemsCache = dependency.descriptor(IItemsCache)  # Dependency injection for IItemsCache.

    def __init__(self):
        super(QueuedVehicleDossierReceiver, self).__init__()
        self.__isUnderRequesting = False  # A flag to check if a request is already in progress.
        self.__queuedVehicleData = None  # A container for queued vehicle data when a request is in progress.
        self.__lastInvokeTime = 0  # The timestamp of the last request.
        self.onDataReceived = Event()  # An event triggered when data is received.
        return

    def invoke(self, databaseID, vehicleID):
        """
        Initiates a request for vehicle dossier data.

        :param databaseID: The unique identifier of the user.
        :param vehicleID: The unique identifier of the vehicle.
        """
        if self.__isUnderRequesting:
            self.__queuedVehicleData = (databaseID, vehicleID)
        else:
            self.__requestData(databaseID, vehicleID)

    @adisp_process
    def __requestData(self, databaseID, vehicleID):
        """
        Asynchronously requests vehicle dossier data.

        :param databaseID: The unique identifier of the user.
        :param vehicleID: The unique identifier of the vehicle.
        """
        self.__isUnderRequesting = True
        vehDossier = yield self.itemsCache.items.requestUserVehicleDossier(int(databaseID), vehicleID)
        if vehDossier:
            self.onDataReceived(databaseID, vehicleID)
        else:
            LOG_ERROR("Couldn't receive vehicle dossier! Vehicle id: " + vehicleID + ', User id: ' + databaseID)
        self.__isUnderRequesting = False
        if self.__queuedVehicleData is not None:
            dbId = self.__queuedVehicleData[0]
            veh
