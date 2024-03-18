# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/VehicleFireCircleEffectComponent.py

# Import necessary modules and constants
from battle_royale.gui.constants import BattleRoyaleEquipments
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
# Import VehicleAbilityBaseComponent class
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent
# Import vehicles and FireCircle from items and items.artefacts respectively
from items import vehicles
from items.artefacts import FireCircle
# Import first from shared_utils
from shared_utils import first

# Define the VehicleFireCircleEffectComponent class, which inherits from VehicleAbilityBaseComponent
class VehicleFireCircleEffectComponent(VehicleAbilityBaseComponent):
    
    # Class constants
    __CLASS_NAME = 'VehicleFireCircleEffectComponent'
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.FIRE_CIRCLE
    __MARKER_ID = BATTLE_MARKER_STATES.FIRE_CIRCLE_STATE

    def __init__(self):
        # Initialize the superclass with the timer view ID and marker ID
        super(VehicleFireCircleEffectComponent, self).__init__(self.__TIMER_VIEW_ID, self.__MARKER_ID)

    def _getDuration(self):
        # Return the duration of the fire circle effect as an integer
        return int(self.getEquipment().influenceZone.timer)

    @staticmethod
    def getEquipment():
        # Static method to get the fire circle equipment
        # Get the equipment ID for the Fire Circle item
        equipmentID = vehicles.g_cache.equipmentIDs().get(BattleRoyaleEquipments.FIRE_CIRCLE)
        # Get the equipment object for the Fire Circle item
        equipment = vehicles.g_cache.equipments()[equipmentID]
        return equipment

    def _destroy(self):
        # Override the _destroy method from the superclass
        super(VehicleFireCircleEffectComponent, self)._destroy()

        # Find another instance of this component, if it exists, and set its finish time
        otherComp = first([ comp for comp in self.entity.dynamicComponents.values() if isinstance(comp, VehicleFireCircleEffectComponent) and comp is not self ])
        if otherComp:
            otherComp.set_finishTime()
