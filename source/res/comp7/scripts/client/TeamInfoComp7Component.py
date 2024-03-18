# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: comp7/scripts/client/TeamInfoComp7Component.py

import typing
import VOIP
from constants import REQUEST_COOLDOWN
from gui.battle_control import avatar_getter
from gui.battle_control.arena_info.arena_vos import Comp7Keys
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider

