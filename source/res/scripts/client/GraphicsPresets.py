# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/GraphicsPresets.py

import BigWorld
import ResMgr

# The resource file for the graphics settings presets
graphicsPresetsResource = 'system/data/graphics_settings_presets.xml'

class GraphicsPresets:

    def __init__(self):
        # Open the resource file and initialize the presets object
        sect = ResMgr.openSection(graphicsPresetsResource)
        self.entries = {}
        self.entryNames = []
        self.selectedOption = -1
        
        # Iterate through each group of settings in the resource file
        for group in sect.values():
            if group.asString != '':
                entry = {}
                
                # For each setting in the group, add it to the entry dictionary
                for setting in group.values():
                    if setting.name == 'entry':
                        entry[setting.readString('label')] = setting.readInt('activeOption')

                self.entries[group.asString] = entry
                self.entryNames.append(group.asString)

        # Set the selected option based on the current graphics settings
        self.setSelectedOption()

    def setSelectedOption(self):
        self.selectedOption = -1
        currentOptionMap = {}
        
        # Create a map of the current graphics settings
        for currentOption in BigWorld.graphicsSettings():
            currentOptionMap[currentOption[0]] = currentOption[1]

        # Iterate through each entry and check if it matches the current graphics settings
        for i in range(0, len(self.entryNames)):
            foundOption = True
            for setting in self.entries[self.entryNames[i]].items():
                if currentOptionMap.get(setting[0]) != setting[1]:
                    foundOption = False
                    break

            if foundOption == True:
                self.selectedOption = i
                break

    def selectGraphicsOptions(self, option):
        # Set the graphics settings based on the selected entry
        currentOption = self.entries[self.entryNames[option]]
        for setting in currentOption.items():
            try:
                BigWorld.setGraphicsSetting(setting[0], setting[1])
            except:
                print 'selectGraphicsOptions: unable to set option ', setting[0]

        self.selectedOption = option
