# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/frag_panel.py

# Import necessary modules and classes
from gui.Scaleform.daapi.view.meta.FragPanelMeta import FragPanelMeta
from battle_royale.gui.battle_control.controllers.vehicles_count_ctrl import IVehicleCountListener
from gui.battle_control.avatar_getter import getArena
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from gui.impl import backport
from gui.impl.gen import R

# Define the FragPanel class that inherits from FragPanelMeta and IVehicleCountListener
class FragPanel(IVehicleCountListener, FragPanelMeta):
    # Declare an empty __slots__ to prevent the creation of a __dict__ object
    __slots__ = ()
    
    # Define a class-level constant for the additional frag template
    __ADDITIONAL_FRAG_TEMPLATE = '<font color="#333333">[&nbsp;<font color="#999999">{}</font>&nbsp;]</font>'
    
    # Implement the setFrags method from IVehicleCountListener
    def setFrags(self, frags, isPlayerVehicle):
        # Call the as_setRightFieldS method with the frags parameter
        self.as_setRightFieldS(frags)

    # Implement the setTotalCount method from IVehicleCountListener
    def setTotalCount(self, vehicles, teams):
        # Check if the bonus type has any of the SQUADS values
        isSquad = ARENA_BONUS_TYPE_CAPS.checkAny(getArena().bonusType, ARENA_BONUS_TYPE_CAPS.SQUADS)
        # Convert the vehicles count to a string
        countText = str(vehicles)
        # If it's
