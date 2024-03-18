# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/BCBattleSelector.py

import logging
from gui.Scaleform.daapi.view.lobby.header.BattleTypeSelectPopover import BattleTypeSelectPopover

# Initialize the logger for this module
_logger = logging.getLogger(__name__)

# Inherit from BattleTypeSelectPopover to customize the behavior of the base class
class BCBattleSelector(BattleTypeSelectPopover):

    # Override the as_updateS method to implement custom functionality
    def as_updateS(self, items, extraItems, isShowDemonstrator, demonstratorEnabled):
        # Log the received items for debugging purposes
        _logger.debug('BCBattleSelector, %s', items)

        # Iterate through the battle type items
        for battleTypeItem in items:
            # If the data is not 'random', set the disabled attribute to True
            if battleTypeItem['data'] != 'random':
                battleTypeItem['disabled'] = True

        # Call the superclass method with the modified items, extraItems, isShowDemonstrator, and demonstratorEnabled
        super(BCBattleSelector, self).as_updateS(items, extraItems, isShowDemonstrator, demonstratorEnabled)
