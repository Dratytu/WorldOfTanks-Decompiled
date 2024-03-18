# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/hangar_presets/__init__.py

# Importing necessary modules and classes
from constants import QUEUE_TYPE
from battle_royale.gui.hangar_presets.battle_royale_presets_reader import BattleRoyalePresetsReader
from battle_royale.gui.hangar_presets.battle_royale_presets_getter import BattleRoyalePresetsGetter, BattleRoyaleTournamentPresetsGetter
from gui.shared.system_factory import registerHangarPresetsReader, registerHangarPresetGetter

# Function to register Battle Royale specific hangar presets
def registerBattleRoyaleHangarPresets():
    # Register BattleRoyalePresetsReader as a hangar presets reader
    registerHangarPresetsReader(BattleRoyalePresetsReader)
    
    # Register BattleRoyalePresetsGetter as a hangar preset getter for QUEUE_TYPE.BATTLE_ROYALE
    registerHangarPresetGetter(QUEUE_TYPE.BATTLE_ROYALE, BattleRoyalePresetsGetter)
    
    # Register BattleRoyaleTournamentPresetsGetter as a hangar preset getter for QUEUE_TYPE.BATTLE_ROYALE_TOURNAMENT
    registerHangarPresetGetter(QUEUE_TYPE.BATTLE_ROYALE_TOURNAMENT, BattleRoyaleTournamentPresetsGetter)
