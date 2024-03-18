# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/base_stats.py

# Import necessary modules and classes.
from gui.Scaleform.daapi.view.meta.StatsBaseMeta import StatsBaseMeta
from gui.shared import events  # Events module for handling game events
from helpers import dependency  # For dependency injection
from skeletons.gui.battle_session import IBattleSessionProvider  # Session provider interface

# Define the StatsBase class, inheriting from StatsBaseMeta.
class StatsBase(StatsBaseMeta):
    # Inject the IBattleSessionProvider dependency.
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

