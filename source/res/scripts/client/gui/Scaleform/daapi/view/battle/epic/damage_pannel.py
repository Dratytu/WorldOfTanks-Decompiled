# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic/damage_pannel.py

# Import necessary modules
import BigWorld
from gui.Scaleform.daapi.view.meta.EpicDamagePanelMeta import EpicDamagePanelMeta
from gui.Scaleform.daapi.view.battle.shared.damage_panel import DamagePanel

# Define the EpicDamagePanel class, which inherits from both DamagePanel and EpicDamagePanelMeta
class EpicDamagePanel(DamagePanel, EpicDamagePanelMeta):

    # Override the _populate method from DamagePanel
    def _populate(self):
        # Call the superclass's _populate method
        super(EpicDamagePanel, self)._populate()

        # Connect the onCrewRolesFactorUpdated signal from the playerDataComponent to the __setGeneralBonus method
        BigWorld.player().arena.componentSystem.playerDataComponent.onCrewRolesFactorUpdated += self.__setGeneralBonus

    # Override the _dispose method from DamagePanel
    def _dispose(self):
        # Call the superclass's _dispose method
        super(EpicDamagePanel, self)._dispose()

        # Check if BigWorld.player().arena exists and has a componentSystem attribute
        arena = BigWorld.player().arena if hasattr(BigWorld.player(), 'arena') else None
        if arena and hasattr(arena, 'componentSystem'):
            # Get the componentSystem attribute
            componentSystem = BigWorld.player().arena.componentSystem

            # Check if componentSystem exists and has a playerDataComponent attribute
            if componentSystem and hasattr(componentSystem, 'playerDataComponent'):
                # Disconnect the onCrewRolesFactorUpdated signal from the __setGeneralBonus method
                componentSystem.playerDataComponent.onCrewRolesFactorUpdated -= self.__setGeneralBonus

   
