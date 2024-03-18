# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/bootcamp/disabled_settings.py

import resource_helper  # Import resource_helper to read settings from XML file
from debug_utils_bootcamp import LOG_DEBUG_DEV_BOOTCAMP  # Import LOG_DEBUG_DEV_BOOTCAMP for logging

class BCDisabledSettings(object):  # Create a class BCDisabledSettings that inherits from object

    def __init__(self):
        """
        Initialize the class with an empty list for storing disabled settings.
        Read the settings template from the XML file.
        """
        self.__disabledSettings = []  # Initialize an empty list for storing disabled settings
        self.__readSettingsTemplate()  # Call the method to read the settings template

    @property
    def disabledSetting(self):
        """
        A property decorator to iterate through the disabled settings list.
        Yield each item in the list one at a time.
        """
        for item in self.__disabledSettings:
            yield item

    def __readSettingsTemplate(self):
        """
        Log a message indicating that the BootCamp template settings are being read.
        Use resource_helper to read the XML file and extract the settings.
        Store the extracted settings in the self.__disabledSettings list.
        """
        LOG_DEBUG_DEV_BOOTCAMP('Reading BootCamp template settings')
        ctx, section = resource_helper.getRoot('gui/bootcamp_blocked_settings.xml')  # Get the root context and section of the XML file
        self.__disabledSettings = []  # Reset the disabled settings list
        for ctx, subSection in resource_helper.getIterator(ctx, section):
            item = resource_helper.readItem(ctx, subSection).value  # Read an item from the XML file
            if 'controlPath' in item:  # Check if the item has a 'controlPath' attribute
                path = item['controlPath'].split('/')  # Split the 'controlPath' attribute into a list of paths
