# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/account_helpers/premium_info.py

# Import the PREMIUM_TYPE constant from the constants module
from constants import PREMIUM_TYPE

# Define a class named PremiumInfo
class PremiumInfo(object):

    # Initialize the class with an empty premium info dictionary and a premium mask
    def __init__(self):
        self._rawPremiumInfo = {p: 0 for p in PREMIUM_TYPE.TYPES_SORTED}
        self._rawPremiumInfo['premMask'] = 0

    # Update the premium info dictionary with a new dictionary
    def update(self, rawPremiumInfo):
        self._rawPremiumInfo.update(rawPremiumInfo)

    # Check if a specific premium type is active
    def isActivePremium(self, checkPremiumType):
        return self.activePremiumType >= checkPremiumType

    # Check if the user has any active premium
    @property
    def isPremium(self):
        return self.activePremiumType != PREMIUM_TYPE.NONE

    # Get the expiry time of the latest premium
    @property
    def totalPremiumExpiryTime(self):
        premiumMask = self._rawPremiumInfo['premMask']
        # Find the maximum expiry time among all active premium types
        return max(tuple((self._rawPremiumInfo[p] for p in PREMIUM_TYPE.TYPES_SORTED if bool(premiumMask & p))) + (0,))

    # Get the expiry time of the currently active premium
    @property
    def activePremiumExpiryTime(self):
        activePremiumType = self.activePremiumType
        return self._rawPremiumInfo[activePremiumType] if activePremiumType != PREMIUM_TYPE.NONE else 0

    # Get the type of the currently active premium
    @property
    def activePremiumType(self):
        return PREMIUM_TYPE.activePremium(self._rawPremiumInfo['premMask'])

    # Get a dictionary containing information about all premium types

