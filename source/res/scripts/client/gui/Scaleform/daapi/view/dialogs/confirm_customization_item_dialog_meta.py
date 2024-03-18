# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/dialogs/confirm_customization_item_dialog_meta.py

import math
from CurrentVehicle import g_currentVehicle
from gui.Scaleform.daapi.view.dialogs import IDialogMeta
from gui.Scaleform.daapi.view.lobby.customization.sound_constants import SOUNDS
from gui.shared import events
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE, packActionTooltipData
from gui.shared.tooltips.formatters import i18n_make_string
from gui import SystemMessages
from gui.Scaleform.locale.DIALOGS import DIALOGS
from gui.shared.gui_items.processors.common import CustomizationsBuyer
from gui.shared.money import Currency, CurrencyCollection
from helpers import dependency
from items.components.c11n_constants import MAX_ITEMS_FOR_BUY_OPERATION
from skeletons.gui.game_control import ISoundEventChecker
from skeletons.gui.shared import IItemsCache

# Define a class for the types of operations: buy or sell
class Types(object):
    BUY = 0
    SELL = 1


# Define a class for the step size of the item count
class ItemsCountStepSize(object):
    STANDART = 1

