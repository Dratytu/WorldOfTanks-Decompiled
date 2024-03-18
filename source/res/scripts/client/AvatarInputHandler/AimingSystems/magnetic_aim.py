# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/AvatarInputHandler/AimingSystems/magnetic_aim.py

# Import necessary modules
from collections import namedtuple  # For creating custom tuple objects
from itertools import chain  # For chaining together multiple iterables
import math  # For mathematical operations
import BigWorld  # For accessing the game world and entities
from Math import Vector3, Matrix  # For working with vectors and matrices
import math_utils  # For various mathematical utility functions

# Define a class for magnetic aim settings
class MagneticAimSettings(object):
    # Class constant for the magnetic angle in degrees
    MAGNETIC_ANGLE = 2.25
    # Class constant for the key delay in seconds
    KEY_DELAY_SEC = 0.5

    # A static method to calculate the cosine of the magnetic angle
    @staticmethod
    def getMagneticAngle():
        return math.cos(math.radians(MagneticAimSettings.MAGNETIC_ANGLE))

# Define a namedtuple for storing information about a target vehicle
_TargetVeh = namedtuple('TargetVehicle', ('vehicleRef', 'dotResult', 'distance'))

# Define the magnetic aim processor function
def magneticAimProcessor(previousSimpleTarget=None, previousMagneticTarget=None):
    # If there is no current target, find a new target
    if BigWorld.target() is None:
        target = magneticAimFindTarget()
        # If a new target is found and it's different from the previous targets, set it as the new target
        if target and target != previousSimpleTarget and target != previousMagneticTarget:
            BigWorld.player().autoAim(target=target, magnetic=True)
            return target
    # Return the previous magnetic target
    return previousSimpleTarget

# Define the function for finding a target vehicle using magnetic aim
def magneticAimFindTarget():
    # Get the player's vehicle and aim camera
    vehicleAttached = BigWorld.player().getVehicleAttached()
    aimCamera = BigWorld.player().inputHandler.ctrl.camera
    aimCameraDirection = aimCamera.aimingSystem.matrixProvider.applyToAxis(2)
    # If there is no attached vehicle or it's not alive, return None
    if vehicleAttached is None or not vehicleAttached.isAlive():
        return
    # Initialize variables for the minimum angle vehicle and its dot result and distance
    minAngleVehicle = None
    # Iterate over all vehicles in the arena
    for vehicleID in BigWorld.player().arena.vehicles.iterkeys():
        vehicle = BigWorld.entity(vehicleID)
        # If the vehicle is None, continue to the next iteration
        if vehicle is None:
            continue
        # Check if the vehicle is an ally or the player's vehicle, or if it's not started or not alive, and continue to the next iteration if so
        allyOrSelfVehicle = vehicle.publicInfo['team'] == BigWorld.player().team or vehicle.isPlayerVehicle
        if allyOrSelfVehicle or not vehicle.isStarted or not vehicle.isAlive():
            continue
        # Calculate the vector from the aim camera to the vehicle, normalize it, and calculate its dot product with the aim camera direction
        vehiclePositionDirection = vehicle.position - aimCamera.camera.position
        vehiclePositionDirection.normalise()
        dotResult = vehiclePositionDirection.dot(aimCameraDirection)
        # Calculate the distance from the player's vehicle to the current vehicle
        targetDistance = vehicle.position - vehicleAttached.position
        # If the dot product is less than the magnetic angle, continue to the next iteration
        if dotResult < MagneticAimSettings.getMagneticAngle():
            continue
        # If the vehicle is not visible from the camera, continue to the next iteration
        if not isVehicleVisibleFromCamera(vehicle, aimCamera):
            continue
        # Create a namedtuple for the current vehicle with its dot result and distance
        veh = _TargetVeh(vehicleRef=vehicle, dotResult=dotResult, distance=targetDistance.length)
        # If the minimum angle vehicle is None or the dot result is greater than or equal to the minimum angle vehicle's dot result, update the minimum angle vehicle
        if minAngleVehicle is None or dotResult >= minAngleVehicle.dotResult:
            minAngleVehicle = veh
        # If the minimum angle vehicle is not None and the difference between the dot results is almost zero, and the distance is less than the minimum angle vehicle's distance, update the minimum angle vehicle
        if minAngleVehicle is not None and math_utils.almostZero(dotResult - minAngleVehicle.dotResult):
            if targetDistance.length < minAngleVehicle.distance:
                minAngleVehicle = veh

    # If a minimum angle vehicle was found, return it as the target vehicle, otherwise return None
    pickedVehicle = None
    if minAngleVehicle:
        pickedVehicle = minAngleVehicle.vehicleRef
    return pickedVehicle

# Define a function for generating points on a vehicle for visibility checks
def getVehiclePointsGen(vehicle):
    # Get the vehicle's type descriptor and hull position
    vehicleDesr = vehicle.typeDescriptor
    hullPos = vehicleDesr.chassis.hullPosition
    # Get the hull bounding box min, max, and hit tester
    hullBboxMin, hullBboxMax, _ = vehicleDesr.hull.hitTester.bbox
    # Get the turret position on the hull and its local top Y coordinate
    turretPosOnHull = vehicleDesr.hull.turretPositions[0]
    turretLocalTopY = max(hullBboxMax.y, turretPosOnHull.y + vehicleDesr.turret.hitTester.bbox[1].y)
    # Yield the hull position plus the local top Y coordinate as the first point
    yield Vector3(0.0, hullPos.y + turretLocalTopY, 0.0)
    # Get the gun position on the hull and yield the hull position plus the gun position as the second point
    gunPosOnHull = turretPosOnHull + vehicleDes
