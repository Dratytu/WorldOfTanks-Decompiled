# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/AvatarInputHandler/DynamicCameras/ArcadeCamera.py
import math
from collections import namedtuple
import BigWorld
import GUI
import Keys
import Math
from Math import Vector2, Vector3, Vector4, Matrix
import BattleReplay
import Settings
import constants
import math_utils
from AvatarInputHandler import cameras, aih_global_binding
from AvatarInputHandler.AimingSystems.ArcadeAimingSystem import ArcadeAimingSystem
from AvatarInputHandler.AimingSystems.ArcadeAimingSystemRemote import ArcadeAimingSystemRemote
from AvatarInputHandler.DynamicCameras import createOscillatorFromSection, CameraDynamicConfig, AccelerationSmoother, CameraWithSettings, calcYawPitchDelta
from AvatarInputHandler.VideoCamera import KeySensor
from AvatarInputHandler.cameras import readFloat, readVec2, ImpulseReason, FovExtended
from debug_utils import LOG_WARNING, LOG_ERROR
from helpers.CallbackDelayer import CallbackDelayer, TimeDeltaMeter

def getCameraAsSettingsHolder(settingsDataSec):
    return ArcadeCamera(settingsDataSec, None)


MinMax = namedtuple('MinMax', ('min', 'max'))

class CollisionVolumeGroup(namedtuple('CollisionVolumeGroup', ('minVolume', 'lowSpeedLimit', 'vehicleVisibilityLimit', 'approachSpeed', 'cameraSpeedFactor', 'criticalDistance', 'canSkip'))):

    @staticmethod
    def fromSection(dataSection):
        it = iter(CollisionVolumeGroup._fields)
        return CollisionVolumeGroup(dataSection.readFloat(next(it), 0.0), dataSection.readFloat(next(it), 0.0), dataSection.readFloat(next(it), 0.0), dataSection.readVector2(next(it), Math.Vector2(1.5, 10000.0)), dataSection.readFloat(next(it), 0.1), dataSection.readFloat(next(it), 5.0), dataSection.readBool(next(it), False))


VOLUME_GROUPS_NAMES = ['tiny',
 'small',
 'medium',
 'large']
_INERTIA_EASING = math_utils.Easing.exponentialEasing
ENABLE_INPUT_ROTATION_INERTIA = False

class _InputInertia(object):
    __ZOOM_DURATION = 0.5
    positionDelta = property(lambda self: self.__deltaEasing.value)
    fovZoomMultiplier = property(lambda self: self.__zoomMultiplierEasing.value)
    endZoomMultiplier = property(lambda self: self.__zoomMultiplierEasing.b)

    def __init__(self, minMaxZoomMultiplier, relativeFocusDist):
        self.__deltaEasing = _INERTIA_EASING(Vector3(0.0), Vector3(0.0), _InputInertia.__ZOOM_DURATION)
        fovMultiplier = math_utils.lerp(minMaxZoomMultiplier.min, minMaxZoomMultiplier.max, relativeFocusDist)
        self.__zoomMultiplierEasing = _INERTIA_EASING(fovMultiplier, fovMultiplier, _InputInertia.__ZOOM_DURATION)
        self.__minMaxZoomMultiplier = minMaxZoomMultiplier

    def glide(self, posDelta):
        self.__deltaEasing.reset(posDelta, Vector3(0.0), _InputInertia.__ZOOM_DURATION)

    def glideFov(self, newRelativeFocusDist):
        minMult, maxMult = self.__minMaxZoomMultiplier
        endMult = math_utils.lerp(minMult, maxMult, newRelativeFocusDist)
        self.__zoomMultiplierEasing.reset(self.__zoomMultiplierEasing.value, endMult, _InputInertia.__ZOOM_DURATION)

    def teleport(self, relativeFocusDist, minMaxZoomMultiplier=None):
        if minMaxZoomMultiplier is not None:
            self.__minMaxZoomMultiplier = minMaxZoomMultiplier
        self.__deltaEasing.reset(Vector3(0.0), Vector3(0.0), _InputInertia.__ZOOM_DURATION)
        fovMultiplier = math_utils.lerp(self.__minMaxZoomMultiplier.min, self.__minMaxZoomMultiplier.max, relativeFocusDist)
        self.__zoomMultiplierEasing.reset(fovMultiplier, fovMultiplier, _InputInertia.__ZOOM_DURATION)
        return

    def update(self, deltaTime):
        self.__deltaEasing.update(deltaTime)
        self.__zoomMultiplierEasing.update(deltaTime)

    def calcWorldPos(self, idealBasisMatrix):
        return idealBasisMatrix.translation + idealBasisMatrix.applyVector(self.__deltaEasing.value)


class ArcadeCamera(CameraWithSettings, CallbackDelayer, TimeDeltaMeter):
    REASONS_AFFECT_CAMERA_DIRECTLY = (ImpulseReason.MY_SHOT,
     ImpulseReason.OTHER_SHOT,
     ImpulseReason.VEHICLE_EXPLOSION,
     ImpulseReason.HE_EXPLOSION)
    _DYNAMIC_ENABLED = True

    @staticmethod
    def enableDynamicCamera(enable):
        ArcadeCamera._DYNAMIC_ENABLED = enable

    @staticmethod
    def isCameraDynamic():
        return ArcadeCamera._DYNAMIC_ENABLED

    _FILTER_LENGTH = 5
    _DEFAULT_MAX_ACCELERATION_DURATION = 1.5
    _FOCAL_POINT_CHANGE_SPEED = 100.0
    _FOCAL_POINT_MIN_DIFF = 5.0
    _MIN_REL_SPEED_ACC_SMOOTHING = 0.7

    def getReasonsAffectCameraDirectly(self):
        return ArcadeCamera.REASONS_AFFECT_CAMERA_DIRECTLY

    def __getVehicleMProv(self):
        refinedMProv = self.__aimingSystem.vehicleMProv
        return refinedMProv.b.source

    def __setVehicleMProv(self, vehicleMProv):
        prevAimRel = self.__cam.aimPointProvider.a if self.__cam.aimPointProvider is not None else None
        refinedVehicleMProv = self.__refineVehicleMProv(vehicleMProv)
        self.__aimingSystem.vehicleMProv = refinedVehicleMProv
        self.__setupCameraProviders(refinedVehicleMProv)
        self.__cam.speedTreeTarget = self.__aimingSystem.vehicleMProv
        self.__aimingSystem.update(0.0)
        if prevAimRel is not None:
            self.__cam.aimPointProvider.a = prevAimRel
        baseTranslation = Matrix(refinedVehicleMProv).translation
        relativePosition = self.__aimingSystem.matrix.translation - baseTranslation
        self.__setCameraPosition(relativePosition)
        return

    camera = property(lambda self: self.__cam)
    angles = property(lambda self: (self.__aimingSystem.yaw, self.__aimingSystem.pitch))
    aimingSystem = property(lambda self: self.__aimingSystem)
    vehicleMProv = property(__getVehicleMProv, __setVehicleMProv)
    __aimOffset = aih_global_binding.bindRW(aih_global_binding.BINDING_ID.AIM_OFFSET)

    def __init__(self, dataSec, defaultOffset=None):
        super(ArcadeCamera, self).__init__()
        CallbackDelayer.__init__(self)
        TimeDeltaMeter.__init__(self)
        self.__shiftKeySensor = None
        self.__movementOscillator = None
        self.__impulseOscillator = None
        self.__noiseOscillator = None
        self.__dynamicCfg = CameraDynamicConfig()
        self.__accelerationSmoother = None
        self._readConfigs(dataSec)
        self.__onChangeControlMode = None
        self.__aimingSystem = None
        self.__curSense = 0
        self.__curScrollSense = 0
        self.__postmortemMode = False
        self.__focalPointDist = 1.0
        self.__autoUpdateDxDyDz = Vector3(0.0)
        self.__updatedByKeyboard = False
        self.__isCamInTransition = False
        if defaultOffset is not None:
            self.__defaultAimOffset = defaultOffset
            self.__cam = BigWorld.HomingCamera(self.__adCfg['enable'])
            if self.__adCfg['enable']:
                self.__cam.initAdvancedCollider(self.__adCfg['fovRatio'], self.__adCfg['rollbackSpeed'], self.__adCfg['minimalCameraDistance'], self.__adCfg['speedThreshold'], self.__adCfg['minimalVolume'])
                for group_name in VOLUME_GROUPS_NAMES:
                    self.__cam.addVolumeGroup(self.__adCfg['volumeGroups'][group_name])

            self.__cam.aimPointClipCoords = defaultOffset
        else:
            self.__defaultAimOffset = Vector2()
            self.__cam = None
        self.__cameraTransition = BigWorld.TransitionCamera()
        return

    @staticmethod
    def _getConfigsKey():
        return ArcadeCamera.__name__

    def create(self, pivotPos, onChangeControlMode=None, postmortemMode=False):
        super(ArcadeCamera, self).create()
        self.__onChangeControlMode = onChangeControlMode
        self.__postmortemMode = postmortemMode
        targetMat = self.getTargetMProv()
        aimingSystemClass = ArcadeAimingSystemRemote if BigWorld.player().isObserver() else ArcadeAimingSystem
        self.__aimingSystem = aimingSystemClass(self.__refineVehicleMProv(targetMat), pivotPos.y, pivotPos.z, self.__calcAimMatrix(), self._cfg['angleRange'], not postmortemMode)
        if self.__adCfg['enable']:
            self.__aimingSystem.initAdvancedCollider(self.__adCfg['fovRatio'], self.__adCfg['rollbackSpeed'], self.__adCfg['minimalCameraDistance'], self.__adCfg['speedThreshold'], self.__adCfg['minimalVolume'])
            for group_name in VOLUME_GROUPS_NAMES:
                self.__aimingSystem.addVolumeGroup(self.__adCfg['volumeGroups'][group_name])

        self.setCameraDistance(self._cfg['startDist'])
        self.__aimingSystem.pitch = self._cfg['startAngle']
        self.__aimingSystem.yaw = Math.Matrix(targetMat).yaw
        self.__updateAngles(0, 0)
        cameraPosProvider = Math.Vector4Translation(self.__aimingSystem.matrix)
        self.__cam.cameraPositionProvider = cameraPosProvider

    def getTargetMProv(self):
        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isPlaying and replayCtrl.playerVehicleID != 0:
            vehicleID = replayCtrl.playerVehicleID
        else:
            vehicleID = BigWorld.player().playerVehicleID
        return BigWorld.entity(vehicleID).matrix

    def reinitMatrix(self):
        self.__setVehicleMProv(self.getTargetMProv())

    def setToVehicleDirection(self):
        matrix = Math.Matrix(self.getTargetMProv())
        self.setYawPitch(matrix.yaw, matrix.pitch)

    def destroy(self):
        self.disable()
        self.__onChangeControlMode = None
        self.__cam = None
        self.__cameraTransition = None
        if self.__aimingSystem is not None:
            self.__aimingSystem.destroy()
            self.__aimingSystem = None
        CallbackDelayer.destroy(self)
        CameraWithSettings.destroy(self)
        return

    def getPivotSettings(self):
        return self.__aimingSystem.getPivotSettings()

    def setPivotSettings(self, heightAboveBase, focusRadius):
        self.__aimingSystem.setPivotSettings(heightAboveBase, focusRadius)

    def __setDynamicCollisions(self, enable):
        if self.__cam is not None:
            self.__cam.setDynamicCollisions(enable)
        if self.__aimingSystem is not None:
            self.__aimingSystem.setDynamicCollisions(enable)
        return

    def focusOnPos(self, preferredPos):
        self.__aimingSystem.focusOnPos(preferredPos)

    def shiftCamPos(self, shift=None):
        matrixProduct = self.__aimingSystem.vehicleMProv
        shiftMat = matrixProduct.a
        if shift is not None:
            camDirection = Math.Vector3(math.sin(self.angles[0]), 0, math.cos(self.angles[0]))
            normal = Math.Vector3(camDirection)
            normal.x = camDirection.z
            normal.z = -camDirection.x
            shiftMat.translation += camDirection * shift.z + Math.Vector3(0, 1, 0) * shift.y + normal * shift.x
        else:
            shiftMat.setIdentity()
        return

    def enable(self, preferredPos=None, closesDist=False, postmortemParams=None, turretYaw=None, gunPitch=None, camTransitionParams=None):
        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isRecording:
            replayCtrl.setAimClipPosition(self.__aimOffset)
        self.measureDeltaTime()
        camDist = None
        vehicle = BigWorld.player().getVehicleAttached()
        initialVehicleMatrix = BigWorld.player().getOwnVehicleMatrix() if vehicle is None else vehicle.matrix
        vehicleMProv = initialVehicleMatrix
        if not self.__postmortemMode:
            if closesDist:
                camDist = self._cfg['distRange'][0]
        elif postmortemParams is not None:
            self.__aimingSystem.yaw = postmortemParams[0][0]
            self.__aimingSystem.pitch = postmortemParams[0][1]
            camDist = postmortemParams[1]
        else:
            camDist = self._cfg['distRange'][1]
        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isPlaying:
            camDist = None
            vehicle = BigWorld.entity(replayCtrl.playerVehicleID)
            if vehicle is not None:
                vehicleMProv = vehicle.matrix
        if camDist is not None:
            self.setCameraDistance(camDist)
        else:
            self.__inputInertia.teleport(self.__calcRelativeDist())
        self.vehicleMProv = vehicleMProv
        self.__setDynamicCollisions(True)
        self.__aimingSystem.enable(preferredPos, turretYaw, gunPitch)
        self.__aimingSystem.aimMatrix = self.__calcAimMatrix()
        if camTransitionParams is not None and BigWorld.camera() is not self.__cam:
            cameraTransitionDuration = camTransitionParams.get('cameraTransitionDuration', -1)
            if cameraTransitionDuration > 0:
                self.__setupCameraTransition(cameraTransitionDuration)
            else:
                BigWorld.camera(self.__cam)
        else:
            BigWorld.camera(self.__cam)
        self.__cameraUpdate()
        self.delayCallback(0.0, self.__cameraUpdate)
        from gui import g_guiResetters
        g_guiResetters.add(self.__onRecreateDevice)
        return

    def __setupCameraTransition(self, duration):
        self.__cameraTransition.start(BigWorld.camera().matrix, self.__cam, duration)
        BigWorld.camera(self.__cameraTransition)
        invMatrix = Math.Matrix()
        invMatrix.set(BigWorld.camera().invViewMatrix)
        previousAimVector = invMatrix.applyToAxis(2)
        self.setYawPitch(previousAimVector.yaw, -previousAimVector.pitch)
        self.__isCamInTransition = True

    def _handleSettingsChange(self, diff):
        if 'fov' in diff or 'dynamicFov' in diff:
            self.__inputInertia.teleport(self.__calcRelativeDist(), self.__calculateInputInertiaMinMax())

    def _updateSettingsFromServer(self):
        super(ArcadeCamera, self)._updateSettingsFromServer()
        if self.settingsCore.isReady:
            ucfg = self._userCfg
            ucfg['sniperModeByShift'] = self.settingsCore.getSetting('sniperModeByShift')
            cfg = self._cfg
            cfg['sniperModeByShift'] = ucfg['sniperModeByShift']

    def __calculateInputInertiaMinMax(self):
        if self.settingsCore.getSetting('dynamicFov'):
            _, minFov, maxFov = self.settingsCore.getSetting('fov')
            kMin = minFov / maxFov
        else:
            kMin = 1.0
        return MinMax(kMin, 1.0)

    def restartCameraTransition(self, duration):
        if self.__cam is not None and not self.__cameraTransition.isInTransition():
            self.__isCamInTransition = True
            self.__cameraTransition.start(BigWorld.camera().matrix, self.__cam, duration)
        return

    def __refineVehicleMProv(self, vehicleMProv):
        vehicleTranslationOnly = Math.WGTranslationOnlyMP()
        vehicleTranslationOnly.source = vehicleMProv
        refinedMatrixProvider = Math.MatrixProduct()
        refinedMatrixProvider.a = math_utils.createIdentityMatrix()
        refinedMatrixProvider.b = vehicleTranslationOnly
        return refinedMatrixProvider

    def __setupCameraProviders(self, vehicleMProv):
        vehiclePos = Math.Vector4Translation(vehicleMProv)
        cameraPositionProvider = Math.Vector4Combiner()
        cameraPositionProvider.fn = 'ADD'
        cameraPositionProvider.a = Vector4(0, 0, 0, 0)
        cameraPositionProvider.b = vehiclePos
        cameraAimPointProvider = Math.Vector4Combiner()
        cameraAimPointProvider.fn = 'ADD'
        cameraAimPointProvider.a = Vector4(0, 0, 1, 0)
        cameraAimPointProvider.b = vehiclePos
        self.__cam.cameraPositionProvider = cameraPositionProvider
        self.__cam.aimPointProvider = cameraAimPointProvider
        self.__cam.pivotPositionProvider = self.__aimingSystem.positionAboveVehicleProv

    def __setCameraPosition(self, relativeToVehiclePosition):
        self.__cam.cameraPositionProvider.a = Vector4(relativeToVehiclePosition.x, relativeToVehiclePosition.y, relativeToVehiclePosition.z, 1.0)

    def __setCameraAimPoint(self, relativeToVehiclePosition):
        self.__cam.aimPointProvider.a = Vector4(relativeToVehiclePosition.x, relativeToVehiclePosition.y, relativeToVehiclePosition.z, 1.0)

    def disable(self):
        from gui import g_guiResetters
        if self.__onRecreateDevice in g_guiResetters:
            g_guiResetters.remove(self.__onRecreateDevice)
        self.__setDynamicCollisions(False)
        self.__cam.speedTreeTarget = None
        if self.__shiftKeySensor is not None:
            self.__shiftKeySensor.reset(Math.Vector3())
        self.stopCallback(self.__cameraUpdate)
        self.__movementOscillator.reset()
        self.__impulseOscillator.reset()
        self.__noiseOscillator.reset()
        self.__accelerationSmoother.reset()
        self.__autoUpdateDxDyDz.set(0)
        self.__updatedByKeyboard = False
        dist = self.__calcRelativeDist()
        if dist is not None:
            self.__inputInertia.teleport(dist)
        FovExtended.instance().resetFov()
        return

    def update(self, dx, dy, dz, rotateMode=True, zoomMode=True, updatedByKeyboard=False):
        self.__curSense = self._cfg['keySensitivity'] if updatedByKeyboard else self._cfg['sensitivity']
        self.__curScrollSense = self._cfg['keySensitivity'] if updatedByKeyboard else self._cfg['scrollSensitivity']
        self.__updatedByKeyboard = updatedByKeyboard
        if updatedByKeyboard:
            self.__autoUpdateDxDyDz.set(dx, dy, dz)
        else:
            self.__autoUpdateDxDyDz.set(0)
            self.__update(dx, dy, dz, rotateMode, zoomMode, False)

    def setUserConfigValue(self, name, value):
        if name not in self._userCfg:
            return
        else:
            self._userCfg[name] = value
            if name not in ('keySensitivity', 'sensitivity', 'scrollSensitivity'):
                self._cfg[name] = self._userCfg[name]
                if name == 'fovMultMinMaxDist' and getattr(self, '_ArcadeCamera__aimingSystem', None) is not None:
                    self.__inputInertia.teleport(self.__calcRelativeDist(), value)
            else:
                self._cfg[name] = self._baseCfg[name] * self._userCfg[name]
            return

    def setCameraDistance(self, distance):
        distRange = self._cfg['distRange']
        clampedDist = math_utils.clamp(distRange[0], distRange[1], distance)
        self.__aimingSystem.distanceFromFocus = clampedDist
        self.__inputInertia.teleport(self.__calcRelativeDist())

    def getCameraDistance(self):
        return self.__aimingSystem.distanceFromFocus

    def setYawPitch(self, yaw, pitch):
        self.__aimingSystem.yaw = yaw
        self.__aimingSystem.pitch = pitch

    def __updateAngles(self, dx, dy):
        yawDelta, pitchDelta = calcYawPitchDelta(self._cfg, self.__curSense, dx, dy)
        self.__aimingSystem.handleMovement(yawDelta, -pitchDelta)
        return (self.__aimingSystem.yaw, self.__aimingSystem.pitch, 0)

    def __update(self, dx, dy, dz, rotateMode=True, zoomMode=True, isCallback=False):
        if not self.__aimingSystem:
            return
        else:
            prevPos = self.__inputInertia.calcWorldPos(self.__aimingSystem.matrix)
            if self.__isCamInTransition:
                self.__isCamInTransition = self.__cameraTransition.isInTransition()
            distChanged = False
            if zoomMode and dz != 0:
                prevDist = self.__aimingSystem.distanceFromFocus
                distDelta = dz * float(self.__curScrollSense)
                distMinMax = self._cfg['distRange']
                newDist = math_utils.clamp(distMinMax.min, distMinMax.max, prevDist - distDelta)
                floatEps = 0.001
                if abs(newDist - prevDist) > floatEps:
                    self.__aimingSystem.distanceFromFocus = newDist
                    self._userCfg['startDist'] = newDist
                    self.__inputInertia.glideFov(self.__calcRelativeDist())
                    self.__aimingSystem.aimMatrix = self.__calcAimMatrix()
                    distChanged = True
                if not self.__updatedByKeyboard:
                    if abs(newDist - prevDist) < floatEps and math_utils.almostZero(newDist - distMinMax.min):
                        if self.__onChangeControlMode is not None:
                            self.__onChangeControlMode()
                            return
            if rotateMode and not self.__isCamInTransition:
                self.__updateAngles(dx, dy)
            if ENABLE_INPUT_ROTATION_INERTIA and not distChanged:
                self.__aimingSystem.update(0.0)
            if ENABLE_INPUT_ROTATION_INERTIA or distChanged:
                worldDeltaPos = prevPos - self.__aimingSystem.matrix.translation
                matInv = Matrix(self.__aimingSystem.matrix)
                matInv.invert()
                self.__inputInertia.glide(matInv.applyVector(worldDeltaPos))
            return

    def __cameraUpdate(self):
        if not (self.__autoUpdateDxDyDz.x == 0.0 and self.__autoUpdateDxDyDz.y == 0.0 and self.__autoUpdateDxDyDz.z == 0.0):
            self.__update(self.__autoUpdateDxDyDz.x, self.__autoUpdateDxDyDz.y, self.__autoUpdateDxDyDz.z)
        inertDt = deltaTime = self.measureDeltaTime()
        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isPlaying:
            repSpeed = replayCtrl.playbackSpeed
            if repSpeed == 0.0:
                inertDt = 0.01
                deltaTime = 0.0
            else:
                inertDt = deltaTime = deltaTime / repSpeed
        self.__aimingSystem.update(deltaTime)
        virginShotPoint = self.__aimingSystem.getThirdPersonShotPoint()
        delta = self.__inputInertia.positionDelta
        sign = delta.dot(Vector3(0, 0, 1))
        self.__inputInertia.update(inertDt)
        delta = (delta - self.__inputInertia.positionDelta).length
        if delta != 0.0:
            self.__cam.setScrollDelta(math.copysign(delta, sign))
        FovExtended.instance().setFovByMultiplier(self.__inputInertia.fovZoomMultiplier)
        unshakenPos = self.__inputInertia.calcWorldPos(self.__aimingSystem.matrix)
        vehMatrix = Math.Matrix(self.__aimingSystem.vehicleMProv)
        vehiclePos = vehMatrix.translation
        fromVehicleToUnshakedPos = unshakenPos - vehiclePos
        deviationBasis = math_utils.createRotationMatrix(Vector3(self.__aimingSystem.yaw, 0, 0))
        impulseDeviation, movementDeviation, oscillationsZoomMultiplier = self.__updateOscillators(deltaTime)
        relCamPosMatrix = math_utils.createTranslationMatrix(impulseDeviation + movementDeviation)
        relCamPosMatrix.postMultiply(deviationBasis)
        relCamPosMatrix.translation += fromVehicleToUnshakedPos
        upRotMat = math_utils.createRotationMatrix(Vector3(0, 0, -impulseDeviation.x * self.__dynamicCfg['sideImpulseToRollRatio'] - self.__noiseOscillator.deviation.z))
        upRotMat.postMultiply(relCamPosMatrix)
        self.__cam.up = upRotMat.applyVector(Vector3(0, 1, 0))
        relTranslation = relCamPosMatrix.translation
        shotPoint = self.__calcFocalPoint(virginShotPoint, deltaTime)
        vehToShotPoint = shotPoint - vehiclePos
        self.__setCameraAimPoint(vehToShotPoint)
        self.__setCameraPosition(relTranslation)
        replayCtrl = BattleReplay.g_replayCtrl
        if replayCtrl.isPlaying and replayCtrl.isControllingCamera:
            aimOffset = replayCtrl.getAimClipPosition()
            if not BigWorld.player().isForcedGuiControlMode() and GUI.mcursor().inFocus:
                GUI.mcursor().position = aimOffset
        else:
            aimOffset = self.__calcAimOffset(oscillationsZoomMultiplier)
            if replayCtrl.isRecording:
                replayCtrl.setAimClipPosition(aimOffset)
        self.__cam.aimPointClipCoords = aimOffset
        self.__aimOffset = aimOffset
        if self.__shiftKeySensor is not None:
            self.__shiftKeySensor.update(1.0)
            if self.__shiftKeySensor.currentVelocity.lengthSquared > 0.0:
                self.shiftCamPos(self.__shiftKeySensor.currentVelocity)
                self.__shiftKeySensor.currentVelocity = Math.Vector3()
        return 0.0

    def __calcFocalPoint(self, shotPoint, deltaTime):
        aimStartPoint = self.__aimingSystem.matrix.translation
        aimDir = shotPoint - aimStartPoint
        distToShotPoint = aimDir.length
        if distToShotPoint < 0.001:
            return shotPoint
        aimDir /= distToShotPoint
        absDiff = abs(distToShotPoint - self.__focalPointDist)
        if absDiff < ArcadeCamera._FOCAL_POINT_MIN_DIFF or absDiff <= ArcadeCamera._FOCAL_POINT_CHANGE_SPEED * deltaTime:
            self.__focalPointDist = distToShotPoint
            return shotPoint
        changeDir = (distToShotPoint - self.__focalPointDist) / absDiff
        self.__focalPointDist += changeDir * ArcadeCamera._FOCAL_POINT_CHANGE_SPEED * deltaTime
        return aimStartPoint + aimDir * self.__focalPointDist

    def __calcAimOffset(self, oscillationsZoomMultiplier):
        fov = BigWorld.projection().fov
        aspect = cameras.getScreenAspectRatio()
        yTan = math.tan(fov * 0.5)
        xTan = yTan * aspect
        defaultX = self.__defaultAimOffset[0]
        defaultY = self.__defaultAimOffset[1]
        yawFromImpulse = self.__impulseOscillator.deviation.x * self.__dynamicCfg['sideImpulseToYawRatio']
        xImpulseDeviationTan = math.tan(-(yawFromImpulse + self.__noiseOscillator.deviation.x) * oscillationsZoomMultiplier)
        pitchFromImpulse = self.__impulseOscillator.deviation.z * self.__dynamicCfg['frontImpulseToPitchRatio']
        yImpulseDeviationTan = math.tan((pitchFromImpulse + self.__noiseOscillator.deviation.y) * oscillationsZoomMultiplier)
        totalOffset = Vector2((defaultX * xTan + xImpulseDeviationTan) / (xTan * (1 - defaultX * xTan * xImpulseDeviationTan)), (defaultY * yTan + yImpulseDeviationTan) / (yTan * (1 - defaultY * yTan * yImpulseDeviationTan)))
        return totalOffset

    def __calcRelativeDist(self):
        if self.__aimingSystem is not None:
            distRange = self._cfg['distRange']
            curDist = self.__aimingSystem.distanceFromFocus
            return (curDist - distRange[0]) / (distRange[1] - distRange[0])
        else:
            return

    def __calcCurOscillatorAcceleration(self, deltaTime):
        vehicle = BigWorld.player().getVehicleAttached()
        if vehicle is None:
            return Vector3(0, 0, 0)
        else:
            vehFilter = vehicle.filter
            curVelocity = getattr(vehFilter, 'velocity', Vector3(0.0))
            relativeSpeed = curVelocity.length / vehicle.typeDescriptor.physics['speedLimits'][0]
            if relativeSpeed >= ArcadeCamera._MIN_REL_SPEED_ACC_SMOOTHING:
                self.__accelerationSmoother.maxAllowedAcceleration = self.__dynamicCfg['accelerationThreshold']
            else:
                self.__accelerationSmoother.maxAllowedAcceleration = self.__dynamicCfg['accelerationMax']
            acceleration = self.__accelerationSmoother.update(vehicle, deltaTime)
            yawMat = math_utils.createRotationMatrix((-self.__aimingSystem.yaw, 0, 0))
            acceleration = yawMat.applyVector(-acceleration)
            oscillatorAcceleration = Vector3(acceleration.x, acceleration.y, acceleration.z)
            return oscillatorAcceleration * self.__dynamicCfg['accelerationSensitivity']

    def __updateOscillators(self, deltaTime):
        if not ArcadeCamera.isCameraDynamic():
            self.__impulseOscillator.reset()
            self.__movementOscillator.reset()
            self.__noiseOscillator.reset()
            return (Vector3(0), Vector3(0), 1.0)
        oscillatorAcceleration = self.__calcCurOscillatorAcceleration(deltaTime)
        self.__movementOscillator.externalForce += oscillatorAcceleration
        self.__impulseOscillator.update(deltaTime)
        self.__movementOscillator.update(deltaTime)
        self.__noiseOscillator.update(deltaTime)
        self.__impulseOscillator.externalForce = Vector3(0)
        self.__movementOscillator.externalForce = Vector3(0)
        self.__noiseOscillator.externalForce = Vector3(0)
        relDist = self.__calcRelativeDist()
        zoomMultiplier = math_utils.lerp(1.0, self.__dynamicCfg['zoomExposure'], relDist)
        impulseDeviation = Vector3(self.__impulseOscillator.deviation)
        impulseDeviation.set(impulseDeviation.x * zoomMultiplier, impulseDeviation.y * zoomMultiplier, impulseDeviation.z * zoomMultiplier)
        movementDeviation = Vector3(self.__movementOscillator.deviation)
        movementDeviation.set(movementDeviation.x * zoomMultiplier, movementDeviation.y * zoomMultiplier, movementDeviation.z * zoomMultiplier)
        return (impulseDeviation, movementDeviation, zoomMultiplier)

    def applyImpulse(self, position, impulse, reason=ImpulseReason.ME_HIT):
        adjustedImpulse, noiseMagnitude = self.__dynamicCfg.adjustImpulse(impulse, reason)
        yawMat = math_utils.createRotationMatrix((-self.__aimingSystem.yaw, 0, 0))
        impulseLocal = yawMat.applyVector(adjustedImpulse)
        self.__impulseOscillator.applyImpulse(impulseLocal)
        self.__applyNoiseImpulse(noiseMagnitude)

    def applyDistantImpulse(self, position, impulseValue, reason=ImpulseReason.ME_HIT):
        applicationPosition = self.__cam.position
        if reason == ImpulseReason.SPLASH:
            applicationPosition = Matrix(self.vehicleMProv).translation
        impulse = applicationPosition - position
        distance = impulse.length
        if distance < 1.0:
            distance = 1.0
        impulse.normalise()
        if reason == ImpulseReason.OTHER_SHOT and distance <= self.__dynamicCfg['maxShotImpulseDistance']:
            impulse *= impulseValue / distance
        elif reason == ImpulseReason.SPLASH or reason == ImpulseReason.HE_EXPLOSION:
            impulse *= impulseValue / distance
        elif reason == ImpulseReason.VEHICLE_EXPLOSION and distance <= self.__dynamicCfg['maxExplosionImpulseDistance']:
            impulse *= impulseValue / distance
        else:
            return
        self.applyImpulse(position, impulse, reason)

    def __applyNoiseImpulse(self, noiseMagnitude):
        noiseImpulse = math_utils.RandomVectors.random3(noiseMagnitude)
        self.__noiseOscillator.applyImpulse(noiseImpulse)

    def handleKeyEvent(self, isDown, key, mods, event=None):
        if self.__shiftKeySensor is None:
            return False
        elif BigWorld.isKeyDown(Keys.KEY_CAPSLOCK) and mods & 4:
            if key == Keys.KEY_C:
                self.shiftCamPos()
            return self.__shiftKeySensor.handleKeyEvent(key, isDown)
        else:
            self.__shiftKeySensor.reset(Math.Vector3())
            return False

    def reload(self):
        if not constants.IS_DEVELOPMENT:
            return
        import ResMgr
        ResMgr.purge('gui/avatar_input_handler.xml')
        cameraSec = ResMgr.openSection('gui/avatar_input_handler.xml/arcadeMode/camera/')
        self._reloadConfigs(cameraSec)

    def __calcAimMatrix(self):
        endMult = self.__inputInertia.endZoomMultiplier
        fov = FovExtended.instance().actualDefaultVerticalFov * endMult
        offset = self.__defaultAimOffset
        return cameras.getAimMatrix(-offset[0], -offset[1], fov)

    def _readConfigs(self, dataSec):
        if dataSec is None:
            LOG_WARNING('Invalid section <arcadeMode/camera> in avatar_input_handler.xml')
        super(ArcadeCamera, self)._readConfigs(dataSec)
        enableShift = dataSec.readBool('shift', False)
        if enableShift:
            movementMappings = dict()
            movementMappings[Keys.KEY_A] = Math.Vector3(-1, 0, 0)
            movementMappings[Keys.KEY_D] = Math.Vector3(1, 0, 0)
            movementMappings[Keys.KEY_Q] = Math.Vector3(0, 1, 0)
            movementMappings[Keys.KEY_E] = Math.Vector3(0, -1, 0)
            movementMappings[Keys.KEY_W] = Math.Vector3(0, 0, 1)
            movementMappings[Keys.KEY_S] = Math.Vector3(0, 0, -1)
            shiftSensitivity = dataSec.readFloat('shiftSensitivity', 0.5)
            self.__shiftKeySensor = KeySensor(movementMappings, shiftSensitivity)
            self.__shiftKeySensor.reset(Math.Vector3())
        dynamicsSection = dataSec['dynamics']
        self.__impulseOscillator = createOscillatorFromSection(dynamicsSection['impulseOscillator'], False)
        self.__movementOscillator = createOscillatorFromSection(dynamicsSection['movementOscillator'], False)
        self.__movementOscillator = Math.PyCompoundOscillator(self.__movementOscillator, Math.PyOscillator(1.0, Vector3(50), Vector3(20), Vector3(0.01, 0.0, 0.01)))
        self.__noiseOscillator = createOscillatorFromSection(dynamicsSection['randomNoiseOscillatorSpherical'])
        self.__dynamicCfg.readImpulsesConfig(dynamicsSection)
        self.__dynamicCfg['accelerationSensitivity'] = readFloat(dynamicsSection, 'accelerationSensitivity', -1000, 1000, 0.1)
        self.__dynamicCfg['frontImpulseToPitchRatio'] = math.radians(readFloat(dynamicsSection, 'frontImpulseToPitchRatio', -1000, 1000, 0.1))
        self.__dynamicCfg['sideImpulseToRollRatio'] = math.radians(readFloat(dynamicsSection, 'sideImpulseToRollRatio', -1000, 1000, 0.1))
        self.__dynamicCfg['sideImpulseToYawRatio'] = math.radians(readFloat(dynamicsSection, 'sideImpulseToYawRatio', -1000, 1000, 0.1))
        accelerationThreshold = readFloat(dynamicsSection, 'accelerationThreshold', 0.0, 1000.0, 0.1)
        self.__dynamicCfg['accelerationThreshold'] = accelerationThreshold
        self.__dynamicCfg['accelerationMax'] = readFloat(dynamicsSection, 'accelerationMax', 0.0, 1000.0, 0.1)
        self.__dynamicCfg['maxShotImpulseDistance'] = readFloat(dynamicsSection, 'maxShotImpulseDistance', 0.0, 1000.0, 10.0)
        self.__dynamicCfg['maxExplosionImpulseDistance'] = readFloat(dynamicsSection, 'maxExplosionImpulseDistance', 0.0, 1000.0, 10.0)
        self.__dynamicCfg['zoomExposure'] = readFloat(dynamicsSection, 'zoomExposure', 0.0, 1000.0, 0.25)
        accelerationFilter = math_utils.RangeFilter(self.__dynamicCfg['accelerationThreshold'], self.__dynamicCfg['accelerationMax'], 100, math_utils.SMAFilter(ArcadeCamera._FILTER_LENGTH))
        maxAccelerationDuration = readFloat(dynamicsSection, 'maxAccelerationDuration', 0.0, 10000.0, ArcadeCamera._DEFAULT_MAX_ACCELERATION_DURATION)
        self.__accelerationSmoother = AccelerationSmoother(accelerationFilter, maxAccelerationDuration)
        self.__inputInertia = _InputInertia(self.__calculateInputInertiaMinMax(), 0.0)
        advancedCollider = dataSec['advancedCollider']
        self.__adCfg = dict()
        cfg = self.__adCfg
        if advancedCollider is None:
            LOG_ERROR('<advancedCollider> dataSection is not found!')
            cfg['enable'] = False
        else:
            cfg['enable'] = advancedCollider.readBool('enable', False)
            cfg['fovRatio'] = advancedCollider.readFloat('fovRatio', 2.0)
            cfg['rollbackSpeed'] = advancedCollider.readFloat('rollbackSpeed', 1.0)
            cfg['minimalCameraDistance'] = self._cfg['distRange'][0]
            cfg['speedThreshold'] = advancedCollider.readFloat('speedThreshold', 0.1)
            cfg['minimalVolume'] = advancedCollider.readFloat('minimalVolume', 200.0)
            cfg['volumeGroups'] = dict()
            for group in VOLUME_GROUPS_NAMES:
                groups = advancedCollider['volumeGroups']
                cfg['volumeGroups'][group] = CollisionVolumeGroup.fromSection(groups[group])

        return

    def _readBaseCfg(self, dataSec):
        bcfg = self._baseCfg
        bcfg['keySensitivity'] = readFloat(dataSec, 'keySensitivity', 0, 10, 0.01)
        bcfg['sensitivity'] = readFloat(dataSec, 'sensitivity', 0, 10, 0.01)
        bcfg['scrollSensitivity'] = readFloat(dataSec, 'scrollSensitivity', 0, 10, 0.01)
        bcfg['angleRange'] = readVec2(dataSec, 'angleRange', (0, 0), (180, 180), (10, 110))
        distRangeVec = readVec2(dataSec, 'distRange', (1, 1), (100, 100), (2, 20))
        bcfg['distRange'] = MinMax(distRangeVec.x, distRangeVec.y)
        bcfg['minStartDist'] = readFloat(dataSec, 'minStartDist', bcfg['distRange'][0], bcfg['distRange'][1], bcfg['distRange'][0])
        bcfg['optimalStartDist'] = readFloat(dataSec, 'optimalStartDist', bcfg['distRange'][0], bcfg['distRange'][1], bcfg['distRange'][0])
        bcfg['angleRange'][0] = math.radians(bcfg['angleRange'][0]) - math.pi * 0.5
        bcfg['angleRange'][1] = math.radians(bcfg['angleRange'][1]) - math.pi * 0.5
        bcfg['fovMultMinMaxDist'] = MinMax(readFloat(dataSec, 'fovMultMinDist', 0.1, 100, 1.0), readFloat(dataSec, 'fovMultMaxDist', 0.1, 100, 1.0))

    def _readUserCfg(self):
        bcfg = self._baseCfg
        ucfg = self._userCfg
        dataSec = Settings.g_instance.userPrefs[Settings.KEY_CONTROL_MODE]
        if dataSec is not None:
            dataSec = dataSec['arcadeMode/camera']
        ucfg['horzInvert'] = False
        ucfg['vertInvert'] = False
        ucfg['sniperModeByShift'] = False
        ucfg['keySensitivity'] = readFloat(dataSec, 'keySensitivity', 0.0, 10.0, 1.0)
        ucfg['sensitivity'] = readFloat(dataSec, 'sensitivity', 0.0, 10.0, 1.0)
        ucfg['scrollSensitivity'] = readFloat(dataSec, 'scrollSensitivity', 0.0, 10.0, 1.0)
        ucfg['startDist'] = readFloat(dataSec, 'startDist', bcfg['distRange'][0], 500, bcfg['optimalStartDist'])
        if ucfg['startDist'] < bcfg['minStartDist']:
            ucfg['startDist'] = bcfg['optimalStartDist']
        ucfg['startAngle'] = readFloat(dataSec, 'startAngle', 5, 180, 60)
        ucfg['startAngle'] = math.radians(ucfg['startAngle']) - math.pi * 0.5
        ucfg['fovMultMinMaxDist'] = MinMax(readFloat(dataSec, 'fovMultMinDist', 0.1, 100, bcfg['fovMultMinMaxDist'].min), readFloat(dataSec, 'fovMultMaxDist', 0.1, 100, bcfg['fovMultMinMaxDist'].max))
        return

    def _makeCfg(self):
        bcfg = self._baseCfg
        ucfg = self._userCfg
        cfg = self._cfg
        cfg['keySensitivity'] = bcfg['keySensitivity']
        cfg['sensitivity'] = bcfg['sensitivity']
        cfg['scrollSensitivity'] = bcfg['scrollSensitivity']
        cfg['angleRange'] = bcfg['angleRange']
        cfg['distRange'] = bcfg['distRange']
        cfg['minStartDist'] = bcfg['minStartDist']
        cfg['horzInvert'] = ucfg['horzInvert']
        cfg['vertInvert'] = ucfg['vertInvert']
        cfg['keySensitivity'] *= ucfg['keySensitivity']
        cfg['sensitivity'] *= ucfg['sensitivity']
        cfg['scrollSensitivity'] *= ucfg['scrollSensitivity']
        cfg['startDist'] = ucfg['startDist']
        cfg['startAngle'] = ucfg['startAngle']
        cfg['fovMultMinMaxDist'] = ucfg['fovMultMinMaxDist']
        cfg['sniperModeByShift'] = ucfg['sniperModeByShift']

    def writeUserPreferences(self):
        ds = Settings.g_instance.userPrefs
        if not ds.has_key(Settings.KEY_CONTROL_MODE):
            ds.write(Settings.KEY_CONTROL_MODE, '')
        ucfg = self._userCfg
        ds = ds[Settings.KEY_CONTROL_MODE]
        ds.writeBool('arcadeMode/camera/horzInvert', ucfg['horzInvert'])
        ds.writeBool('arcadeMode/camera/vertInvert', ucfg['vertInvert'])
        ds.writeFloat('arcadeMode/camera/keySensitivity', ucfg['keySensitivity'])
        ds.writeFloat('arcadeMode/camera/sensitivity', ucfg['sensitivity'])
        ds.writeFloat('arcadeMode/camera/scrollSensitivity', ucfg['scrollSensitivity'])
        ds.writeFloat('arcadeMode/camera/startDist', ucfg['startDist'])
        ds.writeFloat('arcadeMode/camera/fovMultMinDist', ucfg['fovMultMinMaxDist'].min)
        ds.writeFloat('arcadeMode/camera/fovMultMaxDist', ucfg['fovMultMinMaxDist'].max)
        startAngle = math.degrees(ucfg['startAngle'] + math.pi * 0.5)
        ds.writeFloat('arcadeMode/camera/startAngle', startAngle)

    def __onRecreateDevice(self):
        self.__aimingSystem.aimMatrix = self.__calcAimMatrix()
