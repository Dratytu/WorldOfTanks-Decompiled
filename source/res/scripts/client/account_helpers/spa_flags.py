# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/spa_flags.py

# Import necessary modules and functions
from external_strings_utils import strtobool, InvalidStringValueException
from shared_utils.account_helpers.diff_utils import synchronizeDicts
from constants import SPA_ATTRS

# Define the SPAFlags class
class SPAFlags(object):
    # Class constructor
    def __init__(self, syncData):
        # Call the constructor of the superclass
        super(SPAFlags, self).__init__()

        # Initialize class variables
        self.__account = None  #: The account associated with the flags
        self.__syncData = syncData  #: The sync data provided during initialization
        self.__cache = {}  #: The cache for storing flag values
        self.__ignore = True  #: A flag to ignore flag updates when the account is not a player

    # Callback method for when the account becomes a player
    def onAccountBecomePlayer(self):
        """
        Callback method for when the account becomes a player.
        Sets the __ignore flag to False.
        """
        self.__ignore = False

    # Callback method for when the account stops being a player
    def onAccountBecomeNonPlayer(self):
        """
        Callback method for when the account stops being a player.
        Sets the __ignore flag to True.
        """
        self.__ignore = True

    # Method to set the account
    def setAccount(self, account):
        """
        Method to set the account.
        :param account: The account to be set
        """
        self.__account = account

    # Method to synchronize the flags with the given diff
    def synchronize(self, diff):
        """
        Method to synchronize the flags with the given diff.
        Updates the internal __cache attribute with the new flag values.
        :param diff: The diff data containing the flag updates
        """
        # Get the cache diff and the SPA cache from the diff
        cacheDiff = diff.get('cache', None)
        spaCache = cacheDiff.get('SPA', None) if cacheDiff else None

        # Initialize an item diff dictionary
        itemDiff = {}

        # If there is SPA cache, iterate over the client attributes
        if spaCache:
            for key in SPA_ATTRS.toClientAttrs():
                value = spaCache.get(key, None)
                if value:
                    try:
                        # Try to convert the value to a boolean
                        itemDiff[key] = strtobool(value)
                    except InvalidStringValueException:
                        # If it fails, keep the original value
                        itemDiff[key] = value

        # Synchronize the item diff with the cache

