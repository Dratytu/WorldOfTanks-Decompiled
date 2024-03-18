# Python bytecode 2.7 (decompiled from Python 2.7)

# This script is for a DetachedTurret entity, which is a separate entity representing a detached turret in the game world.

from soft_exception import SoftException  # Import SoftException for handling exceptions
import math_utils  # Import math_utils for various mathematical operations
import BigWorld  # Import BigWorld for entity and related functionalities
import Math  # Import Math for matrix and vector operations
from debug_utils import LOG_ERROR, LOG_DEBUG  # Import logging functions
import material_kinds  # Import material_kinds for material indexes
from VehicleEffects import DamageFromShotDecoder  # Import DamageFromShotDecoder for decoding hit points
from VehicleStickers import VehicleStickers  # Import VehicleStickers for managing vehicle stickers
from cgf_obsolete_script.py_component import Component  # Import Component for creating components
from cgf_obsolete_script.script_game_object import ScriptGameObject, ComponentDescriptor  # Import ScriptGameObject and ComponentDescriptor for game object and component management
from vehicle_systems.camouflages import prepareBattleOutfit  # Import prepareBattleOutfit for preparing vehicle outfit
from vehicle_systems.tankStructure import TankPartNames, TankNodeNames, ColliderTypes, getPartModelsFromDesc, ModelsSetParams, ModelStates  # Import tank structure related constants and functions
from helpers.EffectMaterialCalculation import calcSurfaceMaterialNearPoint  # Import calcSurfaceMaterialNearPoint for calculating surface material
from helpers.EffectsList import EffectsListPlayer, SoundStartParam, SpecialKeyPointNames  # Import EffectsListPlayer and related constants for managing effects
from helpers.bound_effects import ModelBoundEffects  # Import ModelBoundEffects for managing model-bound effects
from items import vehicles  # Import vehicles for vehicle-related data
from constants import SERVER_TICK_LENGTH  # Import SERVER_TICK_LENGTH for server tick length

_MIN_COLLISION_SPEED = 3.5  # Minimum collision speed for detecting collisions

class DetachedTurret(BigWorld.Entity, ScriptGameObject):  # DetachedTurret class inherits from BigWorld.Entity and ScriptGameObject

    allTurrets = list()  # List to store all detached turrets
    collisions = ComponentDescriptor()  # ComponentDescriptor for collision component

    def __init__(self):  # Constructor
        ScriptGameObject.__init__(self, self.spaceID, 'DetachedTurret')  # Initialize ScriptGameObject
        self.__vehDescr = vehicles.VehicleDescr(compactDescr=self.vehicleCompDescr)  # Initialize vehicle descriptor
        self.filter = BigWorld.WGTurretFilter()  # Initialize filter
        self.__detachConfirmationTimer = SynchronousDetachment(self)  # Initialize detach confirmation timer
        self.__detachConfirmationTimer.onInit()  # Call onInit method of detach confirmation timer
        self.__detachmentEffects = None  # Initialize detachment effects
        self.targetFullBounds = True  # Target full bounds
        self.targetCaps = [1]  # Target caps
        self.__isBeingPulledCallback = None  # Initialize isBeingPulledCallback
        self.__hitEffects = None  # Initialize hit effects
        self.__vehicleStickers = None  # Initialize vehicle stickers

    def reload(self):  # Reload method
        pass  # Placeholder

    def __prepareModelAssembler(self):  # Prepare model assembler method
        LOG_DEBUG('__prepareModelAssembler', self.__vehDescr.name, self.spaceID)  # Log debug information
        assembler = BigWorld.CompoundAssembler(self.__vehDescr.name, self.spaceID)  # Initialize assembler
        turretModel, gunModel = self.__getModels()  # Get turret and gun models
        assembler.addRootPart(turretModel, TankPartNames.TURRET)  # Add turret model as root part
        assembler.emplacePart(gunModel, TankNodeNames.GUN_JOINT, TankPartNames.GUN)  # Add gun model as part
        parts = {TankPartNames.TURRET: self.__vehDescr.turret,  # Define parts
                 TankPartNames.GUN: self.__vehDescr.gun}
        bspModels = ()  # Initialize bspModels
        for partName, part in parts.iteritems():  # Iterate through parts
            partID = TankPartNames.getIdx(partName)  # Get part index
            crashedHT = part.hitTesterManager.crashedModelHitTester  # Get crashed hit tester
            modelHT = part.hitTesterManager.modelHitTester  # Get model hit tester
            hitTester = crashedHT if crashedHT is not None else modelHT  # Choose hit tester
            bspModel = (partID, hitTester.bspModelName)  # Create bspModel
            bspModels = bspModels + (bspModel,)  # Add bspModel to bspModels

        collisionAssembler = BigWorld.CollisionAssembler(bspModels, self.spaceID)  # Initialize collision assembler
        return [assembler, collisionAssembler]  # Return assembler and collision assembler

    def __getModels(self):  # Get models method
        outfit = prepareBattleOutfit(self.outfitCD, self.__vehDescr, self.vehicleID)  # Prepare battle outfit
        style = outfit.style  # Get style
        if style is None:  # If no style
            return (self.__vehDescr.turret.models.exploded, self.__vehDescr.gun.models.exploded)  # Return exploded models
        else:  # If style exists
            modelsSetParams = ModelsSetParams(style.modelsSet, ModelStates.EXPLODED, [])  # Initialize modelsSetParams
            _, _, turretModel, gunModel = getPartModelsFromDesc(self.__vehDescr, modelsSetParams)  # Get part models
            return (turretModel, gunModel)  # Return turret and gun models

    def prerequisites
