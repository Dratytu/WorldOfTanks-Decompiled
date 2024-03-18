# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/battle_loading.py

# Import necessary modules and classes
from gui.Scaleform.daapi.view.meta.BattleRoyaleLoadingMeta import BattleRoyaleLoadingMeta
from gui.impl.gen.resources import R  # Resource container for localization and other resources
from gui.impl import backport  # Helper class for backporting string resources

# Define the BattleLoading class, which inherits from BattleRoyaleLoadingMeta
class BattleLoading(BattleRoyaleLoadingMeta):

    # Override the _populate method to set up the view
    def _populate(self):
        # Call the superclass method to set up basic view properties
        super(BattleLoading, self)._populate()

        # Get the arena descriptor from the session provider
        arena_dp = self.sessionProvider.getArenaDP()

        # Extract various pieces of data from the arena descriptor
        battle_type = arena_dp.getPersonalDescription().getFrameLabel()
        title = backport.text(R.strings.battle_royale.fullStats.title())
        sub_title = backport.text(R.strings.battle_royale.fullStats.subTitle())
        description = backport.text(R.strings.battle_royale.fullStats.description())

        # Pass the extracted data to the setHeaderData SSC handler
        self.as_setHeaderDataS({'battleType': battle_type,
                                'title': title,
                                'subTitle': sub_title,
                                'description': description})

    # Override the _formatTipTitle method to format the tooltip title
    def _formatTipTitle(self, tip_title_text):
        return tip_title_text

    # Override the _formatTipBody method to format the tooltip body
    def _formatTipBody(self, tip_
