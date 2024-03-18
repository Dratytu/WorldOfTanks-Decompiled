# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/battle_control/matrix_factory.py

import BigWorld  # Import the BigWorld module for accessing game world entities and matrices
import Math  # Import the Math module for matrix and vector operations
from debug_utils import LOG_WARNING, LOG_CURRENT_EXCEPTION  # Import logging functions for error handling
from gui.battle_control.avatar_getter import getInputHandler  # Import function for getting input handler
from gui.battle_control.battle_constants import VEHICLE_LOCATION  # Import vehicle location constants

# Function to create a MatrixProvider for a vehicle entity in the game world
def makeVehicleEntityMP(vehicle):
    provider = Math.WGTranslationOnlyMP()  # Create a MatrixProvider for translation-only updates
    provider.source = vehicle.matrix  # Set the source matrix to the vehicle's matrix
    return provider  # Return the MatrixProvider


# Function to create a copy of a MatrixProvider for a vehicle entity in the game world
def makeVehicleEntityMPCopy(vehicle):
    provider = Math.WGTranslationOnlyMP()  # Create a MatrixProvider for translation-only updates
    provider.source = Math.Matrix(vehicle.matrix)  # Set the source matrix to a copy of the vehicle's matrix
    return provider  # Return the MatrixProvider


# Function to create a MatrixProvider for a position in the game world
def makePositionMP(position):
    provider = Math.WGReplayAwaredSmoothTranslationOnlyMP()  # Create a MatrixProvider for smooth translation-only updates
    matrix = Math.Matrix()  # Create a new matrix
    matrix.setTranslate(position)  # Set the matrix's translation to the given position
    provider.source = matrix  # Set the source matrix to the new matrix
    return provider  # Return the MatrixProvider


# Function to get the matrix of an entity in the game world by its ID
def getEntityMatrix(entityID):
    try:
        return BigWorld.entities[entityID].matrix  # Try to get the matrix of the entity by its ID
    except AttributeError:
        LOG_CURRENT_EXCEPTION()  # Log any AttributeError exceptions
        return None  # Return None if an exception occurred

    return None  # Return None if the function reaches the end without returning


# Function to get the MatrixProvider and vehicle location for a given vehicle ID and positions dictionary
def getVehicleMPAndLocation(vehicleID, positions):
    vehicle = BigWorld.entities.get(vehicleID)  # Get the vehicle entity by its ID
    location = VEHICLE_LOCATION.UNDEFINED  # Initialize the vehicle location to an undefined value
    provider = None  # Initialize the MatrixProvider to None
    if vehicle is not None and vehicle.isStarted:  # If the vehicle entity exists and is started
        provider = makeVehicleEntityMP(vehicle)  # Create a MatrixProvider for the vehicle
        location = VEHICLE_LOCATION.AOI  # Set the vehicle location to AOI (Area of Interest)
    elif vehicleID in positions:  # If the vehicle ID is in the positions dictionary
        provider = makePositionMP(positions[vehicleID])  # Create a MatrixProvider for the position
        location = VEHICLE_LOCATION.FAR  # Set the vehicle location to FAR
    return (provider, location)  # Return the MatrixProvider and vehicle location


# Function to create a MatrixProvider for a vehicle entity based on its location and positions dictionary
def makeVehicleMPByLocation(vehicleID, location, positions):
    provider = None  # Initialize the MatrixProvider to None
    if location in (VEHICLE_LOCATION.AOI, VEHICLE_LOCATION.AOI_TO_FAR):  # If the vehicle location is AOI or AOI_TO_FAR
        vehicle = BigWorld.entities.get(vehicleID)  # Get the vehicle entity by its ID
        if vehicle is not None and vehicle.isStarted:  # If the vehicle entity exists and is started
            if location == VEHICLE_LOCATION.AOI_TO_FAR:  # If the vehicle location is AOI_TO_FAR
                provider = makeVehicleEntityMPCopy(vehicle)  # Create a copy of the MatrixProvider for the vehicle
            else:  # If the vehicle location is AOI
                provider = makeVehicleEntityMP(vehicle)  # Create the MatrixProvider for the vehicle
        else:  # If the vehicle entity does not exist or is not started
            LOG_WARNING('Entity of vehicle is not found to given location', vehicleID, location)  # Log a warning
    elif location == VEHICLE_LOCATION.FAR:  # If the vehicle location is FAR
        if vehicleID in positions:  # If the vehicle ID is in the positions dictionary
            provider = makePositionMP(positions[vehicleID])  # Create a MatrixProvider for the position
        else:  # If the vehicle ID is not in the positions dictionary
            LOG_WARNING('Position of vehicle is not found in the arena.positions', vehicleID, location)  # Log a warning
    return provider  # Return the MatrixProvider


# Function to convert a Matrix to a LastSpottedVehicle Matrix
def convertToLastSpottedVehicleMP(matrix):
    converted = Math.WGReplayAwaredSmoothTranslationOnlyMP()  # Create a MatrixProvider for smooth translation-only updates
    converted.source = Math.Matrix(matrix.source)  # Set the source matrix to a copy of the given matrix
    return converted  # Return the converted MatrixProvider


# Function to create a MatrixProvider for the Arcade Camera
def makeArcadeCameraMatrix():
    matrix = Math.WGCombinedMP()  # Create a MatrixProvider for combined updates
    matrix.translationSrc = BigWorld.player().getOwnVehicleMatrix()  # Set the translation source to the player's own vehicle matrix
    matrix.rotationSrc = BigWorld.camera().invViewMatrix  # Set the rotation source to the inverse of the camera's view matrix
    return matrix  # Return the MatrixProvider


# Function to create a MatrixProvider for the Vehicle Turret
