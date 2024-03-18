# Python bytecode 2.7 (decompiled from Python 2.7)

# This script is part of the fun_random package, located in the scripts/client directory.
# It contains helper functions for generating tips.

import random
from cgf_components.marker_component import IBattleSessionProvider  # Interface for battle session providers
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher  # Mixin for monitoring fun submodes
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode  # Helper function for checking battle submode
from gui.impl.gen import R  # Helper class for accessing resource strings
from helpers import dependency  # Helper module for managing dependencies
from helpers.tips import TipsCriteria, TipData  # Classes for managing tips criteria and data

