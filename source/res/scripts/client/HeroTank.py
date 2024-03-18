# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/HeroTank.py

import math
import random
from typing import TYPE_CHECKING
import BigWorld
from ClientSelectableCameraVehicle import ClientSelectableCameraVehicle
from ClientSelectableCameraObject import ClientSelectableCameraObject
from CurrentVehicle import g_currentPreviewVehicle
from gui.hangar_vehicle_appearance import HangarVehicleAppearance
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates
from gui.limited_ui.lui_rules_storage import LuiRules
from gui.shared import events, EVENT_BUS_SCOPE, g_eventBus
from gui.shared.gui_items import GUI_ITEM_TYPE
from helpers import dependency
from items.components.c11n_constants import SeasonType
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.game_control import IHeroTankController, ILimitedUIController
from skeletons.gui.shared.utils import IHangarSpace
from vehicle_systems.tankStructure import ModelStates
from items import vehicles
from constants import IS_DEVELOPMENT

# Check if the code is being type-checked by a static analysis tool
if TYPE_CHECKING:
    from vehicle_outfit.outfit import Outfit as TOutfit
    from items.vehicles import VehicleDescrType


class _HeroTankAppearance(HangarVehicleAppearance):
    """
    A class representing the appearance of a hero tank in the hangar.
    """
    _heroTankCtrl = dependency.descriptor(IHeroTankController)
    _c11nService = dependency.descriptor(ICustomizationService)

    def __init__(self, spaceId, vEntity, turretYaw=0.0, gunPitch=0.0):
        """
        Initialize the hero tank appearance.

        :param spaceId: The ID of the space where the hero tank will be displayed.
        :param vEntity: The vehicle entity.
        :param turretYaw: The initial turret yaw angle.
        :param gunPitch: The initial gun pitch angle.
        """
        super(_HeroTankAppearance, self).__init__(spaceId, vEntity)
        self.__season = random.choice(SeasonType.COMMON_SEASONS)
        self.__turretYaw = turretYaw
        self.__gunPitch = gunPitch
        self.__typeDescriptor = vEntity.typeDescriptor

    def _getActiveOutfit(self, vDesc):
        """
        Get the active outfit for the hero tank.

        :param vDesc: The vehicle descriptor.
        :return: The active outfit.
        """
        styleId = self._heroTankCtrl.getCurrentTankStyleId()
        vehicleCD = vDesc.makeCompactDescr()
        if styleId:
            style = self._c11nService.getItemByID(GUI_ITEM_TYPE.STYLE, styleId)
            return style.getOutfit(self.__season, vehicleCD=vehicleCD)
        return self._c11nService.getEmptyOutfitWithNationalEmblems(vehicleCD)

    def _getTurretYaw(self):
        """
        Get the turret yaw angle.

        :return: The turret yaw angle.
        """
        return self.__turretYaw

    def _getGunPitch(self):
        """
        Get the gun pitch angle.

        :return: The gun pitch angle.
        """
        return self.__gunPitch


class HeroTank(ClientSelectableCameraVehicle):
    """
    A class representing a hero tank in the hangar.
    """
    _heroTankCtrl = dependency.descriptor(IHeroTankController)
    _hangarSpace = dependency.descriptor(IHangarSpace)
    __limitedUIController = dependency.descriptor(ILimitedUIController)

    def __init__(self):
        """
        Initialize the hero tank.
        """
        self.__heroTankCD = None
        self.__isHidden = False
        ClientSelectableCameraVehicle.__init__(self)

    def onEnterWorld(self, prereqs):
        """
        Called when the hero tank enters the world.

        :param prereqs: Not used in this method.
        """
        super(HeroTank, self).onEnterWorld(prereqs)
        self._hangarSpace.onHeroTankReady += self._updateHeroTank
        self._heroTankCtrl.onUpdated += self._updateHeroTank
        self._heroTankCtrl.onInteractive += self._updateInteractive
        self._heroTankCtrl.onHidden += self.__onHidden
        self.__limitedUIController.startObserve(LuiRules.HERO_TANK, self.__updateHeroTankVisibility)

    def onLeaveWorld(self):
        """
        Called when the hero tank leaves the world.
        """
        self._heroTankCtrl.onHidden -= self.__onHidden
        self._hangarSpace.onHeroTankReady -= self._updateHeroTank
        self._heroTankCtrl.onUpdated -= self._updateHeroTank
        self._heroTankCtrl.onInteractive -= self._updateInteractive
        self.__limitedUIController.stopObserve(LuiRules.HERO_TANK, self.__updateHeroTankVisibility)
        super(HeroTank, self).onLeaveWorld()

    def onMouseClick(self):
        """
        Called when the hero tank is clicked.

        :return: Whether the camera should switch to the hero tank.
        """
        ClientSelectableCameraObject.switchCamera(self, 'HeroTank')
        return self.state != CameraMovementStates.FROM_OBJECT

    def removeModelFromScene(self):
        """
        Remove the hero tank model from the scene.
        """
        if self.isVehicleLoaded:
            self._onVehicleDestroy()
            self.removeVehicle()
        self.__heroT
