# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/ingame_help/fun_random_pages.py

from constants import ARENA_GUI_TYPE # Importing ARENA_GUI_TYPE constant from constants module
from fun_random.gui.ingame_help import HelpPagePriority # Importing HelpPagePriority enum from fun_random.gui.ingame_help module
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher # Importing FunSubModesWatcher mixin from fun_random.gui.feature.util.fun_mixins module
from fun_random.gui.feature.util.fun_wrappers import hasBattleSubMode # Importing hasBattleSubMode decorator from fun_random.gui.feature.util.fun_wrappers module
from fun_random.gui.Scaleform.daapi.view.battle.hint_panel.hint_panel_plugin import HelpHintContext # Importing HelpHintContext enum from fun_random.gui.Scaleform.daapi.view.battle.hint_panel.hint_panel_plugin module
from gui.impl import backport # Importing backport module
from gui.ingame_help.detailed_help_pages import addPage, DetailedHelpPagesBuilder # Importing addPage function and DetailedHelpPagesBuilder class from gui.ingame_help.detailed_help_pages module
from gui.shared.formatters import text_styles # Importing text_styles module from gui.shared.formatters module

class FunRandomHelpPagesBuilder(DetailedHelpPagesBuilder, FunSubModesWatcher):
    # Class inheriting from DetailedHelpPagesBuilder and FunSub
