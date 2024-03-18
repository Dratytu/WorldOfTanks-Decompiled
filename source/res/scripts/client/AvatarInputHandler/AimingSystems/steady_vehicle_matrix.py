# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/AvatarInputHandler/AimingSystems/steady_vehicle_matrix.py

import math_utils
import BigWorld
import Math
from cgf_obsolete_script.py_component import Component

class SteadyVehicleMatrixCalculator(Component):
    # Provides output matrix and stabilized matrix for aiming systems

    @property
    def outputMProv(self):
        # Output matrix provider
        return self.__outputMProv

    @property
    def stabilisedMProv(self):
        # Stabilized matrix provider
        return self.__stabilisedMProv

    def __init__(self):
        # Initialize the component
        self.__outputMProv = Math.WGCombinedMP()  # Output matrix provider
        self.__stabilisedMProv = Math.WGAdaptiveMatrixProvider()  # Stabilized matrix provider

    def __relinkToIdentity(self):
        # Relink the output matrix provider to the identity matrix
        self.__outputMProv.rotationSrc = math_utils.createIdentityMatrix()
        self.__outputMProv.translationSrc = self.__outputMProv.rotationSrc
        self.__stabilisedMProv.target = self.__outputMProv.rotationSrc

    def relinkSources(self):
        # Relink the matrix providers to the vehicle's matrices
        vehicle = BigWorld.player().getVehicleAttached()
        if vehicle is None or vehicle.isHidden:
            # If there's no attached vehicle or it's hidden, relink to the identity matrix
            self.__relinkToIdentity()
            return
        else:
            type_descriptor = vehicle.typeDescriptor
            if type_descriptor.isPitchHullAimingAvailable:
                # If pitch hull aiming is available, use the ground-placing matrix for rotation
                # and the stabilized matrix for translation
                self.__outputMProv.rotationSrc = vehicle.filter.groundPlacingMatrixFiltered
                self.__outputMProv.translationSrc = vehicle.filter.stabilisedMatrix
            else:
                # Otherwise, use the stabilized matrix for both rotation and translation
                self.__outputMProv.rotationSrc = vehicle.filter.stabilisedMatrix
                self.__outputMProv.translationSrc = self.__outputMProv.rotationSrc
            self.__stabilisedMProv.target = vehicle.filter.stabilisedMatrix
            return
