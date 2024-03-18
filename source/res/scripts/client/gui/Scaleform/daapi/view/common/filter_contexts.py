# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/common/filter_contexts.py

# A class to represent a filter setup context
class FilterSetupContext(object):
    """
    A class that holds the context for a filter setup.
    """

    def __init__(self, ctx=None, asset=None):
        """
        Initialize the FilterSetupContext object with a context dictionary and an asset string.
        The asset string can contain format placeholders that will be replaced with values from the context dictionary.
        :param ctx: A dictionary of context variables
        :param asset: A string containing format placeholders
        """
        self.ctx = ctx or {} # Set the context to an empty dictionary if it is None
        self.asset = asset or '' # Set the asset to an empty string if it is None
        self.asset = self.asset.format(**self.ctx) # Format the asset string with values from the context dictionary


# A function to generate a dictionary of FilterSetupContext objects for various filters
def getFilterSetupContexts(xpRateMultiplier):
    """
    Generate a dictionary of FilterSetupContext objects for various filters.
    The dictionary contains the following filters: favorite, elite, premium, igr, bonus, battleRoyale, rented, debut_boxes.
    :param xpRateMultiplier: A number representing the XP rate multiplier
    :return: A dictionary of FilterSetupContext objects
    """
    return {'favorite': FilterSetupContext(asset='favorite'),
     'elite': FilterSetupContext(asset='elite_small_icon'),
     'premium': FilterSetupContext(asset='prem_small_icon'),
     'igr': FilterSetupContext(asset='premium_small'),
     'bonus': FilterSetupContext(ctx={'multiplier': xpRateMultiplier}, asset='bonus_x{multiplier}'),
     'battleRoyale': FilterSetupContext(asset='battle_royale_toggle'),
     'rented': FilterSetupContext(asset='marathon/time_icon'),
     'debut_boxes': FilterSetupContext(asset='debut_boxes_filter')}


# A function to generate a dictionary of FilterSetupContext objects for various filters in a popover
def getFilterPopoverSetupContexts(xpRateMultiplier):
    """
    Generate a dictionary of FilterSetupContext objects for various filters in a popover.
    The dictionary contains the following filters: favorite, elite, premium, igr, bonus, rented, event, isCommonProgression, crystals, clanRented, ranked, debut_boxes.
    :param xpRateMultiplier: A number representing the XP rate multiplier
    :return: A dictionary of FilterSetupContext objects
    """
    return {'favorite': FilterSetupContext(asset='favorite_medium'),
     'elite': FilterSetupContext(asset
