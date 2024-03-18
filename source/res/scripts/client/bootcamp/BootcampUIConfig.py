# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bootcamp/BootcampUIConfig.py

# Import necessary modules
from copy import copy
import ResMgr
from soft_exception import SoftException

# Define the default battle ribbons settings
g_defaultBattleRibbonsSettings = {
    'damage': False,
    'kill': False,
    'armor': False,
    'ram': False,
    'spotted': False,
    'capture': False,
    'crits': False
}

# Set the path to the XML configuration file
XML_CONFIG_PATH = 'scripts/bootcamp_docs/battle_page_visibility.xml'

# Define a function to read UI settings from the file
def readUISettingsFile(path):
    settingsConfig = ResMgr.openSection(path)
    if settingsConfig is None:
        # Raise a SoftException if the config file cannot be opened
        raise SoftException("Can't open config file (%s)" % path)
    
    # Initialize dictionaries to store all prebattle and ribbons settings
    allPrebattleSettings = {}
    allRibbonsSettings = {}
    
    # Iterate over each section in the configuration file
    for name, section in settingsConfig.items():
        if name == 'lesson':
            # Extract the lesson ID and ribbons settings for this lesson
            lessonId = section['id'].asInt
            ribbonsSettings = copy(g_defaultBattleRibbonsSettings)
            ribString = section['ribbons'].asString
            ribbonNames = ribString.split()
            for ribName in ribbonNames:
                if ribName in ribbonsSettings:
                    ribbonsSettings[ribName] = True
            allRibbonsSettings[lessonId] = ribbonsSettings
            
            # Extract the prebattle settings for this lesson
            prebattleSettings = {}
            prebattleSection = section['prebattle']
            if prebattleSection.has_key('timeout'):
                prebattleSettings['timeout'] = prebattleSection['timeout'].asFloat
            allPrebattleSettings[lessonId] = prebattleSettings
    
    # Return the dictionaries containing all prebattle and ribbons settings
    return (allPrebattleSettings, allRibbonsSettings)

# Read the UI settings from the configuration file
g_prebattleSettings, g_battleRibbonsSettings = readUISettingsFile(XML_CONFIG_PATH)

# Define a function to get the battle ribbons settings for a given lesson ID
def getBattleRibbonsSettings(lessonId):
    return g_battleRibbonsSettings[lessonId]

# Define a function to get the prebattle settings
