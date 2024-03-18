# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/epic_random/battle_loading.py

# Importing the BattleLoading class from the shared battle loading module
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading, BattleLoadingTipSetting

# Defining the EpicRandomBattleLoading class that inherits from the BattleLoading class
class EpicRandomBattleLoading(BattleLoading):

    # Overriding the _getViewSettingByID method from the BattleLoading class
    def _getViewSettingByID(self, settingID):
        # Initializing the result dictionary
        result = {}
        
        # Checking if the settingID is equal to BattleLoadingTipSetting.OPTIONS.TEXT
        if settingID == BattleLoadingTipSetting.OPTIONS.TEXT:
            # Adding keys and values to the result dictionary based on the specific settings for this case
            result.update({'leftTeamTitleLeft': -418,
                           'rightTeamTitleLeft': 200,
                           'tipTitleTop': 536,
                           'tipBodyTop': 562,
                           'showTableBackground': True,
                           'showTipsBackground': False})
        else:
            # Adding keys and values to the result dictionary based on the general settings
            result.update({'leftTeamTitleLeft': -468,
                           'rightTeamTitleLeft': 255,
                           'tipTitleTop': 366,
                           'tipBodyTop': 397,
                           'showTableBackground': False,
                           'showTipsBackground': True})
        
        # Returning the result dictionary
        return result
