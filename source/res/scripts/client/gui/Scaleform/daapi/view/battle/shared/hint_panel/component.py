# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/hint_panel/component.py

import functools
import BigWorld
import CommandMapping
import SoundGroups
from cgf_components.zone_components import IBattleSessionProvider
from gui.Scaleform.daapi.view.battle.shared.hint_panel import plugins
from gui.Scaleform.daapi.view.meta.BattleHintPanelMeta import BattleHintPanelMeta
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from gui.shared import EVENT_BUS_SCOPE, events
from gui.shared.events import GameEvent
from gui.shared.utils.plugins import PluginsCollection
from helpers import dependency
from shared_utils import first

# BattleHintPanel class is responsible for managing hints in the battle.
class BattleHintPanel(BattleHintPanelMeta, IAbstractPeriodView):
    # Dependency injection for IBattleSessionProvider.
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(BattleHintPanel, self).__init__()
        # A dictionary to store hints for each button ID.
        self._hints = {}
        # A collection of hint plugins.
        self._plugins = None
        # A flag to track if the battle is loaded.
        self.__isBattleLoaded = False
        # A callback ID for invalidating button hints.
        self.__invalidateCallbackID = None
        return

    # Sets a hint for a button.
    def setBtnHint(self, btnID, hintData):
        if hintData:
            if btnID in self._hints:
              
