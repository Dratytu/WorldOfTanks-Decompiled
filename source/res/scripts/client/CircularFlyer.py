# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/CircularFlyer.py

import math
import BigWorld
import AnimationSequence
from Math import Matrix, Vector3
from debug_utils import LOG_CURRENT_EXCEPTION
from vehicle_systems.stricted_loading import makeCallbackWeak
import SoundGroups

class CircularFlyer(BigWorld.UserDataObject):
    """
    A class that represents a flyer object moving in a circular path.
    """

    def __init__(self):
        """
        Initializes a new instance of the CircularFlyer class.
        """
        BigWorld.UserDataObject.__init__(self)
        self.__prev_time = BigWorld.time()  # Previous time for calculating delta time.
        self.__angular_velocity = 2 * math.pi / self.rotation_period  # Angular velocity of the flyer.
        if not self.rotate_clockwise:
            self.__angular_velocity *= -1  # If rotating counter-clockwise, negate the angular velocity.
        self.__current_angle = 0.0  # Current angle of the flyer in radians.
        self.__update_callback_id = None  # Callback ID for updating the flyer's position.
        self.__model = None  # The 3D model of the flyer.
        self.__model_matrix = None  # The transformation matrix of the flyer's model.
        self.__sound = None  # The sound associated with the flyer.
        self.__animator = None  # The animation controller for the flyer's model.

        # Load the flyer's resources in the background.
        BigWorld.loadResourceListBG((self.model_name, self.pixie_name), makeCallbackWeak(self.__on_resources_loaded))

    def __del__(self):
        """
        Cleans up the CircularFlyer instance.
        """
        self.__clear()

    def __clear(self):
        """
        Clears all resources associated with the CircularFlyer instance.
        """
        if self.__update_callback_id is not None:
            BigWorld.cancelCallback(self.__update_callback_id)
        self.__update_callback_id = None

        if self.__sound is not None:
            self.__sound.stop()
            self.__sound.releaseMatrix()
            self.__sound = None

        if self.__model is not None:
            self.__animator = None
            BigWorld.delModel(self.__model)
            self.__model = None

    def __on_resources_loaded(self, resource_refs):
        """
        Called when the flyer's resources are loaded.

        :param resource_refs: A dictionary containing the loaded resources.
        """
        if self.guid not in BigWorld.userDataObjects:
            return

        self.__clear()

        if self.model_name in resource_refs.failedIDs:
            return

        try:
            self.__model = resource_refs[self.model_name]
            self.__model_matrix = Matrix()
            self.__model_matrix.setIdentity()

            servo = BigWorld.Servo(self.__model_matrix)
            self.__model.addMotor(servo)

            BigWorld.addModel(self.__model)

            if self.action_name != '':
                clip_resource = self.__model.deprecatedGetAnimationClipResource(self.action_name)
                if clip_resource:
                    space_id = BigWorld.player().spaceID
                    loader = AnimationSequence.Loader(clip_resource, space_id)
                    animator = loader.loadSync()
                    animator.bindTo(AnimationSequence.ModelWrapperContainer(self.__model, space_id))
                    animator.start()
                    self.__animator = animator

            if self.pixie_name != '' and self.pixie_name not in resource_refs.failedIDs:
                pixie_node = self.__model.node(self.pixie_hard_point)
                pixie_node.attach(resource_refs[self.pixie_name])

            if self.sound_name != '':
                self.__sound = SoundGroups.g_instance.getSound3D(self.__model_matrix, self.sound_name)

        except Exception:
            LOG_CURRENT_EXCEPTION()
            self.__model = None
            return

        self.__prev_time = BigWorld.time()
        self.__update()

    def __update(self):
        """
        Updates the flyer's position and orientation.
        """
        self.__update_callback_id = None
        self.__update_callback_id = BigWorld.callback(0.0, self.__update)

        cur_time = BigWorld.time()
        dt = cur_time - self.__prev_time
        self.__prev_time = cur_time

        self.__current_angle += self.__angular_velocity * dt
        if self.__current_angle > 2 * math.pi:
            self.__current_angle -= 2 * math.pi
        elif self.__current_angle < -2 * math.pi:
            self.__current_angle += 2 * math.pi

        radial_position = Vector3(self.radius * math.sin(self.__current_angle), 0, self.radius * math.cos(self.__current_angle))
        model_yaw = self.__current_angle
        if self.rotate_clockwise:
            model_yaw += math.pi / 2
        else:
            model_yaw -= math.pi / 2

        local_matrix = Matrix()
        local_matrix.setRotateY(model_yaw)
        local_matrix.translation = radial_position

        self.__model_matrix.setRotateYPR((self.yaw, self.pitch, self.roll))
        self.__model_matrix.translation = self.position

        self.__model_matrix.preMultiply(local_matrix)

