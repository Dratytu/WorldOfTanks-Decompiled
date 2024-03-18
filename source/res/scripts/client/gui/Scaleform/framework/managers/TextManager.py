# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/framework/managers/TextManager.py

import debug_utils
from gui.Scaleform.framework.entities.abstract.TextManagerMeta import TextManagerMeta  # Importing the base class for the TextManager.
from gui.Scaleform.genConsts.TEXT_MANAGER_STYLES import TEXT_MANAGER_STYLES as _TMS  # Importing the predefined text styles.
from gui.shared.formatters import text_styles  # Importing the module that contains text style formatting functions.

# Subclassing the base TextManagerMeta class to create a custom text manager.
class TextManager(TextManagerMeta):

    def __init__(self):
        super(TextManager, self).__init__()
        self.__styles = text_styles.getRawStyles([v for k, v in _TMS.__dict__.iteritems() if not k.startswith('_')])  # Initializing the styles dictionary with the predefined text styles.

    # A method to retrieve a text style by its name.
    def getTextStyle(self, style):
        if style in self.__styles:
            result = self.__styles[style]
        else:
            debug_utils.LOG_ERROR('Style is not found', style)  # Logging an error if the requested style is not found.
            result = ''
        return result

    def _dispose(self):
        self.__styles.clear()
        super(TextManager, self)._dispose()  # Disposing of the base TextManagerMeta instance.


# Defining a class for text icons.
class TextIcons(object):
    CHECKMARK_ICON = 'checkmark'
    NUT_ICON = 'nut'
    PERCENT_ICON = 'percent'
    ALERT_ICON = 'alert'
    INFO_ICON = 'info'
    PREMIUM_IGR_SMALL = 'premiumIgrSmall'
    PREMIUM_IGR_BIG = 'premiumIgrBig'
    ORDER_IN_PROGRESS_ICON = 'order_in_progress'
    CLOCK_ICON = 'clock'
    NOT_AVAILABLE = 'notAvailable'
    LEVEL_5 = 'level5'
    LEVEL_10 = 'level10'
    SWORDS = 'swords'
    HUMANS = 'humans'
    CREDITS = 'credits'
    GOLD = 'gold'
    XP = 'xp'
    FREE_XP = 'freeXP'
    ARROW_BUTTON = 'arrowButton'
    NO_SEASON = 'noSeason'
    ICONS = (NUT_ICON,
     PERCENT_ICON,
     ALERT_ICON,
     INFO_ICON,
     PREMIUM_IGR_SMALL,
     PREMIUM_IGR_BIG,
    
