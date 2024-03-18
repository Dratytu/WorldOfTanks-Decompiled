# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: frontline/scripts/common/frontline_common/constants.py

# Define a class for account settings keys
class AccountSettingsKeys(object):
    # EVENT_KEY is used to store frontline keys
    EVENT_KEY = 'frontline_keys'
    
    # SKILL_POINTS_SHOWN is used to store whether skill points are shown
    SKILL_POINTS_SHOWN = 'points_shown'
    
    # WELCOME_SCREEN_VIEWED is used to store whether the welcome screen has been viewed
    WELCOME_SCREEN_VIEWED = 'welcome_screen_viewed'

# Define the default settings for an account
ACCOUNT_DEFAULT_SETTINGS = {
    AccountSettingsKeys.EVENT_KEY: {
        AccountSettingsKeys.SKILL_POINTS_SHOWN: {},  # Empty dict to store skill points settings
        AccountSettingsKeys.WELCOME_SCREEN_VIEWED: {}  # Empty dict to store welcome screen viewed status
    }
}

