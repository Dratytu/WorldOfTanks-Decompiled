# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: frontline/scripts/client/VehicleFLRegenerationKitComponent.py

import BigWorld
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE

class VehicleFLRegenerationKitComponent(BigWorld.DynamicScriptComponent):
    """
    A component responsible for handling the Frontline Regeneration Kit.
    """

    def set_regenerationKit(self, _=None):
        """
        Sets the regeneration kit for the attached vehicle.

        :param _: Unused parameter
        """
        attachedVehicle = BigWorld.player().getVehicleAttached()
        if attachedVehicle is None:
            # Return if there's no attached vehicle
            return

        # Prepare healPointEnter data
        healPointEnter = {
            'senderKey': 'healPoint',
            'isSourceVehicle': None,
            'isInactivation': None if not self.regenerationKit['isActive'] else self.regenerationKit['isActive'],
            'endTime': self.regenerationKit['endTime'],
            'duration': self.regenerationKit['duration']
        }

        # If the component is attached to the vehicle, update the vehicle state
        if self.entity.id == attachedVehicle.id:
            self.entity.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.HEALING, healPointEnter)

        # If the component is not attached to the player's vehicle, invalidate the FLRegenerationKit feedback
        if not self.entity.isPlayerVehicle:
            ctrl = self.entity.guiSessionProvider.shared.feedback
            if ctrl is not None:
                ctrl.invalidateFLRegenerationKit(self.entity.id, self.regenerationKit)

        # Return after processing
        return

