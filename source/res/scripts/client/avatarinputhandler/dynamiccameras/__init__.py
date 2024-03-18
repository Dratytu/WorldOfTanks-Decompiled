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

# Define a function to create a matrix for crosshair
def createCrosshairMatrix(offsetFromNearPlane):
    # Calculate the near plane
    nearPlane = BigWorld.projection().nearPlane
    # Create a translation matrix with the given offset from the near plane
    return math_utils.createTranslationMatrix(Vector3(0, 0, nearPlane + offsetFromNearPlane))


# Define a function to create an oscillator from a section
def createOscillatorFromSection(oscillatorSection, constraintsAsAngle=True):
    # Read the constraints from the section
    constraints = readVec3(oscillatorSection, 'constraints', (0.0, 0.0, 0.0), (175.0, 175.0, 175.0), 10.0)
    # If constraintsAsAngle is True, convert the constraints to radians
    if constraintsAsAngle:
        constraints = Vector3((math.radians(constraints.x), math.radians(constraints.y), math.radians(constraints.z)))
    # Get the constructor parameters based on the name of the oscillator section
    constructorParams = {'oscillator': __getOscillatorParams,
     'noiseOscillator': __getNoiseOscillatorParams,
     'randomNoiseOscillatorFlat': __getRandomNoiseOscillatorFlatParams,
     'randomNoiseOscillatorSpherical': __getRandomNoiseOscillatorSphericalParams}.get(oscillatorSection.name, __getOscillatorParams)(oscillatorSection)
    # Create an oscillator instance based on the name of the oscillator section
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


# Define a function to calculate the yaw and pitch delta
def calcYawPitchDelta(cfg, curSense, dx, dy):
    # Calculate the yaw and pitch delta based on the given parameters
    return (dx * curSense * (-1 if cfg['horzInvert'] else 1), dy * curSense * (-1 if cfg['vertInvert'] else 1))


# Define a function to get the oscillator parameters
def __getOscillatorParams(oscillatorSection):
    # Return the oscillator parameters based on the given section
    return [readFloat(oscillatorSection, 'mass', 1e-05, 9000, 3.5), readVec3(oscillatorSection, 'stiffness', (1e-05, 1e-05, 1e-05), (9000, 9000, 9000), 60.0), readVec3(oscillatorSection, 'drag', (1e-05, 1e-05, 1e-05), (9000, 9000, 9000), 9.0)]


# Define a function to get the noise oscillator parameters
def __getNoiseOscillatorParams(oscillatorSection):
    # Return the noise oscillator parameters based on the given section
    return [readFloat(oscillatorSection, 'mass', 1e-05, 9000, 3.5), readVec3(oscillatorSection, 'stiffness', (1e-05, 1e-05, 1e-05), (9000, 9000, 9000), 60.0), readVec3(oscillatorSection, 'drag', (1e-05, 1e-05, 1e-05), (9000, 9000, 9000), 9.0)]


# Define a function to get the random noise oscillator flat parameters
def __getRandomNoiseOscillatorFlatParams(oscillatorSection):
    # Return the random noise oscillator flat parameters based on the given section
    return [readFloat(oscillatorSection, 'mass', 1e-05, 9000, 3.5), readFloat(oscillatorSection, 'stiffness', 1e-05, 9000, 3.5), readFloat(oscillatorSection, 'drag', 1e-05, 9000, 3.5)]


# Define a function to get the random noise oscillator spherical parameters
def __getRandomNoiseOscillatorSphericalParams(oscillatorSection):
    # Get the random noise oscillator flat parameters based on the given section
    oscillatorParams = __getRandomNoiseOscillatorFlatParams(oscillatorSection)
    # Append the scale coefficient to the parameters
    oscillatorParams.append(readVec3(oscillatorSection, 'scaleCoeff', Vector3(0.0), Vector3(9000), Vector3(1.0)))
    # Return the parameters
    return oscillatorParams


# Define a CameraDynamicConfig class
class CameraDynamic
