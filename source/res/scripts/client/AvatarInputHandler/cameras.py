# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/AvatarInputHandler/cameras.py

# The ImpulseReason class defines various reasons for applying impulses to the camera
class ImpulseReason(object):
    # Represents a shot by the local player
    MY_SHOT = 0
    # Represents a hit on the local player
    ME_HIT = 1
    # Represents a shot by another player
    OTHER_SHOT = 2
    # Represents a splash event
    SPLASH = 3
    # Represents a collision event
    COLLISION = 4
    # Represents a vehicle explosion event
    VEHICLE_EXPLOSION = 5
    # Represents a projectile hit event
    PROJECTILE_HIT = 6
    # Represents a high-explosive (HE) explosion event
    HE_EXPLOSION = 7


# The ICamera interface defines the basic methods that a camera implementation should have
class ICamera(object):

    def create(self, **args):
        """
        Creates the camera instance.

        :param args: Additional keyword arguments for creating the camera.
        """
        pass

    def destroy(self):
        """
        Destroys the camera instance.
        """
        pass

    def enable(self, **args):
        """
        Enables the camera.

        :param args: Additional keyword arguments for enabling the camera.
        """
        pass

    def disable(self):
        """
        Disables the camera.
        """
        pass

    def getConfigValue(self, name):
        """
        Retrieves a configuration value from the camera.

        :param name: The name of the configuration value.
        :return: The configuration value.
        """
        pass

    def getUserConfigValue(self, name):
        """
        Retrieves a user-defined configuration value from the camera.

        :param name: The name of the user-defined configuration value.
        :return: The user-defined configuration value.
        """
        pass

    def setUserConfigValue(self, name, value):
        """
        Sets a user-defined configuration value in the camera.

        :param name: The name of the user-defined configuration value.
        :param value: The new value for the user-defined configuration value.
        """
        pass

    def update(self, dx, dy, dz, updatedByKeyboard):
        """
        Updates the camera position and orientation.

        :param dx: Change in the X axis.
        :param dy: Change in the Y axis.
        :param dz: Change in the Z axis.
        :param updatedByKeyboard: Indicates whether the update was triggered by keyboard input.
        """
        pass

    def autoUpdate(self):
        """
        Updates the camera automatically.
        """
        pass

    def applyImpulse(self, position, impulse, reason=ImpulseReason.ME_HIT):
        """
        Applies an impulse to the camera.

        :param position: The position of the impulse.
        :param impulse: The magnitude of the impulse.
        :param reason: The reason for the impulse (optional).
        """
        pass

    def applyDistantImpulse(self, position, impulseValue, reason=ImpulseReason.ME_HIT):
        """
        Applies a distant impulse to the camera.

        :param position: The position of the distant impulse.
        :param impulseValue: The magnitude of the distant impulse.
        :param reason: The reason for the distant impulse (optional).
        """
        pass

    def getReasonsAffectCameraDirectly(self):
        """
        Retrieves the reasons that directly affect the camera.

        :return: A list of reasons.
        """
        pass


# The FreeCamera class is a concrete implementation of the ICamera interface
class FreeCamera(object):
    # The camera property returns the internal camera instance
    camera = property(lambda self: self.__cam)

    def __init__(self):
        """
        Initializes the FreeCamera instance.
        """
        self.__cam = BigWorld.FreeCamera()

    def create(self):
        """
        Creates the camera instance.
        """
        pass

    def destroy(self):
        """
        Destroys the camera instance.
        """
        self.__cam = None
        return

    def enable(self, camMat=None):
        """
        Enables the camera.

        :param camMat: The camera matrix (optional).
        """
        if camMat is not None:
            self.__cam.set(camMat)
        BigWorld.camera(self.__cam)
        BigWorld.enableFreeCameraModeForShadowManager(True)
        return

    def disable(self):
        """
        Disables the camera.
        """
        BigWorld.enableFreeCameraModeForShadowManager(False)

    def setWorldMatrix(self, matrix):
        """
        Sets the world matrix for the camera.

        :param matrix: The new world matrix.
        """
        matrix = Math.Matrix(matrix)
        matrix.invert()
        self.__cam.set(matrix)

    def getWorldMatrix(self):
        """
        Retrieves the world matrix for the camera.

        :return: The world matrix.
        """
        return Math.Matrix(self.__cam.invViewMatrix)

    def handleKey(self, event):
        """
        Handles a keyboard event for the camera.

        :param event: The keyboard event.
        :return: The result of handling the event.
        """
        return self.__cam.handleKeyEvent(event)

    def handleMouse(self, dx, dy, dz):
        """
        Handles a mouse event for the camera.

        :param dx: Change in the X axis.
        :param dy: Change in the Y axis.
        :param dz: Change in the Z axis.
        """
        return self.__cam.handleMouseEvent(BigWorld.MouseEvent(dx, dy, dz, (0, 
