# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/HangarVehicle.py

# Import necessary modules and dependencies
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates, CameraDistanceModes  # Import CameraMovementStates and CameraDistanceModes from hangar_camera_common
from ClientSelectableCameraVehicle import ClientSelectableCameraVehicle  # Import ClientSelectableCameraVehicle
from helpers import dependency  # Import dependency for managing class dependencies
from skeletons.gui.shared.utils import IHangarSpace  # Import IHangarSpace from skeletons.gui.shared.utils
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, events  # Import eventBus, EVENT_BUS_SCOPE, and events from gui.shared

# Define the HangarVehicle class, which inherits from ClientSelectableCameraVehicle
class HangarVehicle(ClientSelectableCameraVehicle):
    
    # Declare dependency for IHangarSpace
    hangarSpace = dependency.descriptor(IHangarSpace)  # Declare a dependency on IHangarSpace

    # Constructor for HangarVehicle class
    def __init__(self):
        # Initialize instance variables
        self.selectionId = ''  # A string variable to store the selection ID
        self.clickSoundName = ''  # A string variable to store the click sound name
        self.releaseSoundName = ''  # A string variable to store the release sound name
        self.mouseOverSoundName = ''  # A string variable to store the mouse-over sound name
        self.edgeMode = 0  # An integer variable to store the edge mode
        self.modelName = ''  # A string variable to store the model name
        # Call the constructor of the superclass
        super(HangarVehicle, self).__init__()
        # Set the camera distance state to custom
        self.camDistState = CameraDistanceModes.CUSTOM  # Set the camera distance state to custom

    # onEnterWorld method, called when the vehicle enters the world
    def onEnterWorld(self, prereqs):
        # Call the onEnterWorld method of the superclass
        super(HangarVehicle, self).onEnterWorld(prereqs)
        # Register event listeners
        self.hangarSpace.onSpaceCreate += self.__onSpaceCreated  # Register onSpaceCreate event listener
        g_eventBus.addListener(events.HangarCustomizationEvent.CHANGE_VEHICLE_MODEL_TRANSFORM, self.__changeVehicleModelTransform, scope=EVENT_BUS_SCOPE.LOBBY)  # Register CHANGE_VEHICLE_MODEL_TRANSFORM event listener
        g_eventBus.addListener(events.HangarCustomizationEvent.RESET_VEHICLE_MODEL_TRANSFORM, self.__resetVehicleModelTransform, scope=EVENT_BUS_SCOPE.LOBBY)  # Register RESET_VEHICLE_MODEL_TRANSFORM event listener
        # Disable the vehicle and set its state
        self.setEnable(False)  # Disable the vehicle
        self.setState(CameraMovementStates.ON_OBJECT)  # Set the vehicle state to ON_OBJECT

    # onLeaveWorld method, called when the vehicle leaves the world
    def onLeaveWorld(self):
        # Unregister event listeners
        self.hangarSpace.onSpaceCreate -= self.__onSpaceCreated  # Unregister onSpaceCreate event listener
        g_eventBus.removeListener(events.HangarCustomizationEvent.CHANGE_VEHICLE_MODEL_TRANSFORM, self.__changeVehicleModelTransform, scope=EVENT_BUS_SCOPE.LOBBY)  # Remove CHANGE_VEHICLE_MODEL_TRANSFORM event listener
        g_eventBus.removeListener(events.HangarCustomizationEvent.RESET_VEHICLE_MODEL_TRANSFORM, self.__resetVehicleModelTransform, scope=EVENT_BUS_SCOPE.LOBBY)  # Remove RESET_VEHICLE_MODEL_TRANSFORM event listener
        # Call the onLeaveWorld method of the superclass
        super(HangarVehicle, self).onLeaveWorld()

    # __onSpaceCreated method, called when the hangar space is created
    def __onSpaceCreated(self):
        self.setEnable(False)  # Disable the vehicle
        self.setState(CameraMovementStates.ON_OBJECT)  # Set the vehicle state to ON_OBJECT

    # _setStartValues method, used to set start values (empty implementation)
    def _setStartValues(self):
        pass

    # __changeVehicleModelTransform method, called when the vehicle model transform changes
    def __changeVehicleModelTransform(self, event):
        ctx = event.ctx  # Get the event context
        targetPos = ctx['targetPos']  # Get the target position from the context
        rotateYPR = ctx['rotateYPR']  # Get the rotate YPR from the context
        shadowYOffset = ctx['shadowYOffset']  # Get the shadow Y offset from the context
        # Update the vehicle model transform
        self._setVehicleModelTransform(targetPos, rotateYPR, shadowYOffset)  # Call _setVehicleModelTransform with targetPos, rotateYPR, and shadowYOffset

    # __resetVehicleModelTransform method, called when the vehicle model transform needs to be reset
    def __resetVehicleModelTransform(self, _):
        # Implement reset functionality here
