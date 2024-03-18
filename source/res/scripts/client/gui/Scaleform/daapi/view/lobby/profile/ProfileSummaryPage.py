# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/profile/ProfileSummaryPage.py

# Import necessary classes and functions
from gui.Scaleform.daapi.view.lobby.profile.ProfileSummary import ProfileSummary
from gui.Scaleform.locale.PROFILE import PROFILE

# Define the ProfileSummaryPage class, which inherits from ProfileSummary
class ProfileSummaryPage(ProfileSummary):

    # Constructor for the ProfileSummaryPage class
    def __init__(self, *args):
        # Call the constructor of the parent class
        ProfileSummary.__init__(self, *args)

    # Override the _getInitData method from the parent class
    def _getInitData(self):
        # Call the _getInitData method of the parent class and store the result in 'outcome'
        outcome = ProfileSummary._getInitData(self)

        # Define the 'nextAwardsLabel' key and assign the localized string for "Next Awards"
        outcome['nextAwardsLabel'] = PROFILE.SECTION_SUMMARY_LABELS_NEXTAWARDS

        # Define the 'nextAwardsErrorText' key and assign the localized string for an error related to "Next Awards"
        outcome['nextAwardsErrorText'] = PROFILE.SECTION_SUMMARY_ERRORTEXT_NEXTAWARDS

        # Return the updated 'outcome' dictionary
        return outcome

    # A method to get the global rating for a given user name
    def getGlobalRating(self, userName):
        # Return the global rating for the given user name using the itemsCache
        return self.itemsCache.items.stats.globalRating
