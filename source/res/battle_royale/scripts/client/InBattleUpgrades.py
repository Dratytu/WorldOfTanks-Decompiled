# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/InBattleUpgrades.py

# Import necessary modules
import BigWorld
from aih_constants import CTRL_MODE_NAME
from debug_utils import LOG_NOTE
from wotdecorators import noexcept

# Define the UpgradeInProgressComponent class
class UpgradeInProgressComponent(object):
    """
    A placeholder for the UpgradeInProgressComponent class.
    """
    pass


# Define the InBattleUpgrades class
class InBattleUpgrades(BigWorld.DynamicScriptComponent):

    # onEnterWorld method is called when the component enters the world
    def onEnterWorld(self, *args):
        """
        A placeholder for the onEnterWorld method.
        """
        pass

    # onLeaveWorld method is called when the component leaves the world
    def onLeaveWorld(self, *args):
        """
        A placeholder for the onLeaveWorld method.
        """
        pass

    # upgradeVehicle method upgrades the vehicle with the given indCD
    def upgradeVehicle(self, indCD):
        """
        Upgrades the vehicle with the given indCD.

        :param indCD: The index and compact descriptor of the upgrade.
        """
        self.cell.upgradeVehicle(indCD)

    # onVehicleUpgraded method is called when the vehicle is upgraded
    def onVehicleUpgraded(self, newVehCompactDescr, newVehOutfitCompactDescr):
        """
        Called when the vehicle is upgraded.

        :param newVehCompactDescr: The compact descriptor of the new vehicle.
        :param newVehOutfitCompactDescr: The compact descriptor of the new vehicle's outfit.
        """
        vehicle = self.entity
        vehicle.isUpgrading = True

        # Remove the existing UpgradeInProgressComponent, if it exists
        if vehicle.entityGameObject.findComponentByType(UpgradeInProgressComponent):
            vehicle.entityGameObject.removeComponentByType(UpgradeInProgressComponent)

        # Create a new UpgradeInProgressComponent
        vehicle.entityGameObject.createComponent(UpgradeInProgressComponent)

        # Call the private __onVehicleUpgraded method
        self.__onVehicleUpgraded(vehicle, newVehCompactDescr, newVehOutfitCompactDescr)

        # Remove the UpgradeInProgressComponent after a short delay
        def removeUpgrageInProgressComponent():
            if vehicle and vehicle.entityGameObject:
                vehicle.entityGameObject.removeComponentByType(UpgradeInProgressComponent)

        BigWorld.callback(0, removeUpgrageInProgressComponent)
        vehicle.isUpgrading = False

    # __onVehicleUpgraded method is a private method called by onVehicleUpgraded
    @noexcept
    def __onVehicleUpgraded(self, vehicle, newVehCompactDescr, newVehOutfitCompactDescr):
        """
        A private method called by onVehicleUpgraded to handle vehicle upgrades.

        :param vehicle: The upgraded vehicle.
        :param newVehCompactDescr: The compact descriptor of the new vehicle.
        :param newVehOutfitCompactDescr: The compact descriptor of the new vehicle's outfit.
        """
        vehicleID = vehicle.id
        if vehicle.isPlayerVehicle:
            inputHandler = BigWorld.player().inputHandler
            arcadeState = None
            if inputHandler.ctrlModeName == CTRL_MODE_NAME.ARCADE:
                arcadeState = inputHandler.ctrl.camera.cloneState()
            inputHandler.onControlModeChanged(CTRL_MODE_NAME.ARCADE, initialVehicleMatrix=vehicle.matrix, arcadeState=arcadeState)

        progressionCtrl = vehicle.guiSessionProvider.dynamic.progression
        if progressionCtrl is not None:
            progressionCtrl.vehicleVisualChangingStarted(vehicleID)

        vehicle.respawnVehicle(vehicleID, newVehCompactDescr, newVehOutfitCompactDescr)
        return

    # testClientMethod is a placeholder method
    def testClientMethod(self):
        """
        A placeholder method for testClientMethod.
        """
        pass

    # set_upgradeReadinessTime method is called when the upgrade readiness time changes
    def set_upgradeReadinessTime(self, prev):
        """
        Called when the upgrade readiness time changes.

        :param prev: The previous upgrade readiness time.
        """
        LOG_NOTE('Vehicle upgrade readiness time changed')
        vehicle = self.entity
        ctrl = vehicle.guiSessionProvider.dynamic.progression
        if ctrl is not None and vehicle.id == BigWorld.player().playerVehicleID:
            ctrl.updateVehicleReadinessTime(self.upgradeReadinessTime.totalTime, self.upgradeReadinessTime.reason)
        return


# Define the onBattleRoyalePrerequisites function
def onBattleRoyalePrerequisites(vehicle, oldTypeDescriptor):
    """
    Checks if the vehicle meets the prerequisites for Battle Royale mode.

    :param vehicle: The vehicle to check.
    :param oldTypeDescriptor: The old type descriptor of the vehicle.
    :return: True if the vehicle meets the prerequisites, False otherwise.
    """
    if 'battle_royale' not in vehicle.typeDescriptor.type.tags:
        return False
    if not oldTypeDescriptor:
        return True
    forceReloding = False
    for moduleName in ('gun', 'turret', 'chassis'):
        oldModule = getattr(oldTypeDescriptor, moduleName)
       
