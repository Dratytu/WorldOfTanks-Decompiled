# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/AvatarInputHandler/DynamicCameras/__init__.py

# Import necessary modules
import math
from collections import defaultdict
import BigWorld
import Math
from Math import Vector3, Matrix
import math_utils
from AvatarInputHandler.cameras import readVec3, ICamera, readFloat, ImpulseReason
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore

# Define a utility function to create a translation matrix for crosshair
def createCrosshairMatrix(offsetFromNearPlane):
    # Calculate the near plane distance using BigWorld's projection
    nearPlane = BigWorld.projection().nearPlane
    # Create a translation matrix with the given offset from the near plane
    return math_utils.createTranslationMatrix(Vector3(0, 0, nearPlane + offsetFromNearPlane))


# Define a function to create an oscillator based on a given section
def createOscillatorFromSection(oscillatorSection, constraintsAsAngle=True):
    # Read the constraints from the section and convert them to radians if requested
    constraints = readVec3(oscillatorSection, 'constraints', (0.0, 0.0, 0.0), (175.0, 175.0, 175.0), 10.0)
    if constraintsAsAngle:
        constraints = Vector3((math.radians(constraints.x), math.radians(constraints.y), math.radians(constraints.z)))
    # Determine the constructor parameters based on the oscillator section name
    constructorParams = {'oscillator': __getOscillatorParams,
     'noiseOscillator': __getNoiseOscillatorParams,
     'randomNoiseOscillatorFlat': __getRandomNoiseOscillatorFlatParams,
     'randomNoiseOscillatorSpherical': __getRandomNoiseOscillatorSphericalParams}.get(oscillatorSection.name, __getOscillatorParams)(oscillatorSection)
    # Create the oscillator instance based on the constructor parameters
    oscillator = None
    if oscillatorSection.name == 'noiseOscillator':
        oscillator = Math.PyNoiseOscillator(*constructorParams)
    elif oscillatorSection.name == 'randomNoiseOscillatorFlat':
        oscillator = Math.PyRandomNoiseOscillatorFlat(*constructorParams)
    elif oscillatorSection.name == 'randomNoiseOscillatorSpherical':
        oscillator = Math.PyRandomNoiseOscillatorSpherical(*constructorParams)
    else:
        constructorParams.append(constraints)
        oscillator = Math.PyOscillator(*constructorParams)
    # Return the created oscillator
    return oscillator


# Define a function to calculate the yaw and pitch delta based on the given parameters
def calcYawPitchDelta(cfg, curSense, dx, dy):
    # Calculate the yaw and pitch delta and return them as a tuple
    return (dx * curSense * (-1 if cfg['horzInvert'] else 1), dy * curSense * (-1 if cfg['vertInvert'] else 1))


# Define a helper function to extract oscillator parameters from a section
def __getOscillatorParams(oscillatorSection):
    # Read the mass, stiffness, and drag values from the section and return them as a tuple
    return [readFloat(oscillatorSection, 'mass', 1e-05, 9000, 3.5), readVec3(oscillatorSection, 'stiffness', (1e-05, 1e-05, 1e-05), (9000, 9000, 9000), 60.0), readVec3(oscillatorSection, 'drag', (1e-05, 1e-05, 1e-05), (9000, 9000, 9000), 9.0)]


# Define helper functions to extract oscillator parameters from a section for different oscillator types
def __getNoiseOscillatorParams(oscillatorSection):
    return __getOscillatorParams(oscillatorSection)


def __getRandomNoiseOscillatorFlatParams(oscillatorSection):
    return [readFloat(oscillatorSection, 'mass', 1e-05, 9000, 3.5), readFloat(oscillatorSection, 'stiffness', 1e-05, 9000, 3.5), readFloat(oscillatorSection, 'drag', 1e-05, 9000, 3.5)]


def __getRandomNoiseOscillatorSphericalParams(oscillatorSection):
    # Read the oscillator parameters and scale coefficient from the section
    oscillatorParams = __getRandomNoiseOscillatorFlatParams(oscillatorSection)
    oscillatorParams.append(readVec3(oscillatorSection, 'scaleCoeff', Vector3(0.0), Vector3(9000), Vector3(1.0)))
    # Return the oscillator parameters
    return oscillatorParams


# Define a CameraDynamicConfig class to handle camera-related configurations
class CameraDynamicConfig(dict):
    # Define a class variable to map impulse reasons to strings
    REASONS_AS_STR = {ImpulseReason.MY_SHOT: 'shot',
     ImpulseReason.ME_HIT: 'hit',
     ImpulseReason.OTHER_SHOT: 'otherShot',
     ImpulseReason.SPLASH: 'splash',
     ImpulseReason.COLLISION: 'collision',
     ImpulseReason.VEHICLE_EXPLOSION: 'vehicleExplosion',
     ImpulseReason.PROJECTILE_HIT: 'projectileHit',
     ImpulseReason.HE_EXPLOSION: 'vehicleExplosion'}

    # Initialize the class
