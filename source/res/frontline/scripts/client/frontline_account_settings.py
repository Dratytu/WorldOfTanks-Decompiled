# frontline/scripts/client/frontline_account_settings.py

# Importing AccountSettings from account_helpers and AccountSettingsKeys and ACCOUNT_DEFAULT_SETTINGS
# from frontline_common.constants for managing account settings related to the Frontline event.
from account_helpers import AccountSettings
from frontline_common.constants import AccountSettingsKeys, ACCOUNT_DEFAULT_SETTINGS

def getSettings(name):
    # Retrieve account settings for the given name (event key)
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)  # Fetch settings from the account
    return settings.get(name, ACCOUNT_DEFAULT_SETTINGS[AccountSettingsKeys.EVENT_KEY].get(name))  # Return the specific setting or the default value if not found


def setSettings(name, value):
    # Set account settings for the given name and value (event key and its corresponding setting)
    settings = AccountSettings.getSettings(AccountSettingsKeys.EVENT_KEY)  # Fetch current settings
    settings[name] = value  # Update or add the new setting
    AccountSettings.setSettings(AccountSettingsKeys.EVENT_KEY, settings)  # Save the updated settings


def getSkillPointsShown(seasonId):
    # Retrieve the skill points shown setting for the given season ID
    data = getSettings(AccountSettingsKeys.SKILL_POINTS_SHOWN)  # Fetch the skill points shown settings
    return data.get(seasonId, None)  # Return the specific season data or None if not found


def setSkillPointsShown(seasonId, pointsAmount):
    # Set the skill points shown setting for the given season ID and points amount
    return setSettings(AccountSettingsKeys.SKILL_POINTS_SHOWN, {seasonId: pointsAmount})  # Update the settings with the new data


def isWelcomeScreenViewed(seasonId):
    # Check if the welcome screen has been viewed for the given season ID
    data = getSettings(AccountSettingsKeys.WELCOME_SCREEN_VIEWED)  # Fetch the welcome screen viewed settings
    return data.get(
