# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/VehicleGunRotator.py

import math
import weakref
from functools import partial
from math import pi, fmod
import BattleReplay
import BigWorld
import Math
import math_utils
from AvatarInputHandler import AimingSystems
from constants import SERVER_TICK_LENGTH, AIMING_MODE, VEHICLE_SIEGE_STATE
from gun_rotation_shared import calcPitchLimitsFromDesc, calcGunPitchCorrection, getLocalAimPoint
from helpers import dependency
from projectile_trajectory import getShotAngles
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID

class VehicleGunRotator(object):
    """
    Class for rotating the vehicle's turret and gun to aim at a target point.
    """

    # Constants
    __INSUFFICIENT_TIME_DIFF = 0.02  # Minimum time difference for updating rotation
    __MAX_TIME_DIFF = 0.2  # Maximum time difference for updating rotation
    ANGLE_EPS = 1e-06  # Angle threshold for considering angles equal
    __ROTATION_TICK_LENGTH = SERVER_TICK_LENGTH  # Length of rotation update tick
    __AIMING_PERFECTION_DELAY = 1.0  # Delay for aiming perfection
    __AIMING_PERFECTION_RANGE = math.radians(5.0)  # Aiming perfection range
    __TURRET_YAW_ALLOWED_ERROR_FACTOR = 0.4  # Turret yaw allowed error factor
    __TURRET_YAW_ALLOWED_ERROR_CONST = math.radians(8.0)  # Turret yaw allowed error constant
    USE_LOCK_PREDICTION = True  # Use lock prediction
    settingsCore = dependency.descriptor(ISettingsCore)  # Settings core dependency
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)  # Battle session provider dependency

    def __init__(self, avatar):
        """
        Initialize the VehicleGunRotator instance.

        :param avatar: The avatar object
        """
        self._avatar = weakref.proxy(avatar)
        self.__isStarted = False
        self.__prevSentShotPoint = None
        self.__targetLastShotPoint = False
        self.__lastShotPoint = Math.Vector3(0, 0, 0)
        self.__shotPointSourceFunctor = self.__shotPointSourceFunctor_Default
        self.__maxTurretRotationSpeed = 0.0
        self.__maxGunRotationSpeed = 0.0
        self.__speedsInitialized = False
        self.__turretYaw = 0.0
        self.__gunPitch = 
