# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/HangarVehicle.py

# Import necessary modules and dependencies
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates, CameraDistanceModes
from ClientSelectableCameraVehicle import ClientSelectableCameraVehicle
from helpers import dependency
from skeletons.gui.shared.utils import IHangarSpace
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, events

# Define the HangarVehicle class, which inherits from ClientSelectableCameraVehicle
class HangarVehicle(ClientSelectableCameraVehicle):
    
    # Declare dependency for IHangarSpace
    hangarSpace = dependency.descriptor(IHangarSpace)

    # Constructor for HangarVehicle class
    def __init__(self):
        # Initialize instance variables
        self.selectionId = ''
        self.clickSoundName = ''
        self.releaseSoundName = ''
        self.mouseOverSoundName = ''
        self.edgeMode = 0
        self.modelName = ''
        # Call the constructor of the superclass
        super(HangarVehicle, self).__init__()
        # Set the camera distance state to custom
        self.camDistState = CameraDistanceModes.CUSTOM

    # onEnterWorld method, called when the vehicle enters the world
    def onEnterWorld(self, prereqs):
        # Call the onEnterWorld method of the superclass
        super(HangarVehicle, self).onEnterWorld(prereqs)
        # Register event listeners
        self.hangarSpace.onSpaceCreate += self.__onSpaceCreated
        g_eventBus.addListener(events.HangarCustomizationEvent.CHANGE_VEHICLE_MODEL_TRANSFORM, self.__changeVehicleModelTransform, scope=EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.addListener(events.HangarCustomizationEvent.RESET_VEHICLE_MODEL_TRANSFORM, self.__resetVehicleModelTransform, scope=EVENT_BUS_SCOPE.LOBBY)
        # Disable the vehicle and set its state
        self.setEnable(False)
        self.setState(CameraMovementStates.ON_OBJECT)

    # onLeaveWorld method, called when the vehicle leaves the world
    def onLeaveWorld(self):
        # Unregister event listeners
        self.hangarSpace.onSpaceCreate -= self.__onSpaceCreated
        g_eventBus.removeListener(events.HangarCustomizationEvent.CHANGE_VEHICLE_MODEL_TRANSFORM, self.__changeVehicleModelTransform, scope=EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.removeListener(events.HangarCustomizationEvent.RESET_VEHICLE_MODEL_TRANSFORM, self.__resetVehicleModelTransform, scope=EVENT_BUS_SCOPE.LOBBY)
        # Call the onLeaveWorld method of the superclass
        super(HangarVehicle, self).onLeaveWorld()

    # __onSpaceCreated method, called when the hangar space is created
    def __onSpaceCreated(self):
        self.setEnable(False)
        self.setState(CameraMovementStates.ON_OBJECT)

    # _setStartValues method, used to set start values (empty implementation)
    def _setStartValues(self):
        pass

    # __changeVehicleModelTransform method, called when the vehicle model transform changes
    def __changeVehicleModelTransform(self, event):
        ctx = event.ctx
        targetPos = ctx['targetPos']
        rotateYPR = ctx['rotateYPR']
        shadowYOffset = ctx['shadowYOffset']
        # Update the vehicle model transform
        self._setVehicleModelTransform(targetPos, rotateYPR, shadowYOffset)

    # __resetVehicleModel
