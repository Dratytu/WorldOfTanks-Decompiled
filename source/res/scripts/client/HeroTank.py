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

