# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/ContactInfo.py

import Settings # Importing the Settings module

class ContactInfo(object):
    # Class level constants for the keys used in the settings
    KEY_USER = 'user'
    KEY_HOST = 'host'
    KEY_EMAIL = 'email'
    KEY_PASSWORD = 'password'
    KEY_REMEMBER = 'remember'

    def __init__(self):
        # Initialize instance variables
        self.host = None
        self.user = None
        self.email = None
        self.password = None
        self.rememberPassword = False
        
        # Check if the login data section exists in the settings
        self.__checkLoginDataSection()
        
        # Read local login data from the settings
        self.readLocalLoginData()
        return

    def readLocalLoginData(self):
        # Read data from the login data section in the settings
        ds = self.getLoginDataSection()
        self.host = ds.readString(self.KEY_HOST)
        self.user = ds.readString(self.KEY_USER)
        self.email = ds.readString(self.KEY_EMAIL)
        self.password = ds.readString(self.KEY_PASSWORD)
        self.rememberPassword = bool(ds.readString(self.KEY_REMEMBER))

    def writeLocalLoginData(self):
        # Write data to the login data section in the settings
        ds = self.getLoginDataSection()
        ds.writeString(self.KEY_HOST, self.host)
        ds.writeString(self.KEY_USER, self.user)
        ds.writeString(self.KEY_EMAIL, self.email)
        ds.writeString(self.KEY_PASSWORD, self.password)
        ds.writeString(self.KEY_REMEMBER, str(self.rememberPassword))

    def getLoginDataSection(self):
        # Get the login data section from the settings
        return Settings.g_instance.userPrefs[Settings.KEY_LOGIN_INFO]

    def __checkLoginDataSection(self):
        # Check if the login data section exists in the settings
        up = Settings.g_instance.userPrefs
        if not up.has_key(Settings.KEY_LOGIN_INFO):
            # If not, create a new section
            up.write(Settings.KEY_LOGIN_INFO,
