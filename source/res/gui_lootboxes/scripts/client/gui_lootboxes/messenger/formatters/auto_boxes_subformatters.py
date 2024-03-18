class IAutoLootBoxSubFormatter(object):
    """
    Interface for loot box subformatters that format messages related to specific groups of loot boxes.
    """


class AutoLootBoxSubFormatter(IAutoLootBoxSubFormatter):
    """
    Base class for loot box subformatters that provides a method for checking if a loot box belongs to a specific group.
    """


class AsyncAutoLootBoxSubFormatter(WaitItemsSyncFormatter, AutoLootBoxSubFormatter):
    """
    Class that extends WaitItemsSyncFormatter and AutoLootBoxSubFormatter to format messages related to loot boxes asynchronously, waiting for item synchronization before processing the message.
    """


class EventBoxesFormatter(AsyncAutoLootBoxSubFormatter):
    """
    Class that extends AsyncAutoLootBoxSubFormatter and is used to format messages related to event loot boxes.
    This class overrides the _isBoxOfThisGroup method to check if a loot box is an event loot box and provides specific message templates and text resources.
    """


class LunarNYEnvelopeAutoOpenFormatter(AsyncAutoLootBoxSubFormatter):
    """
    Class that extends AsyncAutoLootBoxSubFormatter and is used to format messages related to Lunar New Year envelopes.
    This class provides specific methods for formatting achievements, customizations, and decals, as well as message templates and text resources.
    """
