# Python bytecode 2.7 (decompiled from Python 2.7)

# Embedded file name: scripts/client/bwobsolete_helpers/PyGUI/VisualStateComponent.py

import sys
from bwdebug import ERROR_MSG
import ResMgr  # ResMgr is used for opening external resource files

# A class representing a visual state in a game component
class VisualState(object):

    def onSave(self, dataSection):
        """
        Save the visual state to a data section.
        :param dataSection: The data section to save to. This is a pydoc.Section object.
        """
        pass

    def onLoad(self, dataSection):
        """
        Load the visual state from a data section.
        :param dataSection: The data section to load from. This is a pydoc.Section object.
        """
        pass

    def apply(self, componentScript):
        """
        Apply the visual state to a component script.
        :param componentScript: The component script to apply to.
        """
        pass

    def _readMappingSection(self, dataSection):
        """
        Read a mapping section from a data section.
        :param dataSection: The data section to read from. This is a pydoc.Section object.
        :return: A tuple of the mapping type and the mapping.
        """
        mappingName = dataSection.asString.strip()
        mappingType = mappingName if mappingName else 'UV'
        mapping = [None,
                   None,
                   None,
                   None]
        mapping[0] = dataSection.readVector2('coords0')
        mapping[1] = dataSection.readVector2('coords1')
        mapping[2] = dataSection.readVector2('coords2')
        mapping[3] = dataSection.readVector2('coords3')
        mapping = tuple(mapping)
        return (mappingType, mapping)

    def _writeMappingSection(self, dataSection, mappingType, mapping):
        """
        Write a mapping section to a data section.
        :param dataSection: The data section to write to. This is a pydoc.Section object.
        :param mappingType: The type of mapping.
        :param mapping: The mapping to write.
        """
        dataSection.asString = mappingType
        dataSection.writeVector2('coords0', mapping[0])
        dataSection.writeVector2('coords1', mapping[1])
        dataSection.writeVector2('coords2', mapping[2])
        dataSection.writeVector2('coords3', mapping[3])

# A class representing a component that has visual states
class VisualStateComponent(object):

    def __init__(self, component, visualStateClassName):
        """
        Initialize the visual state component.
        :param component: The component that this visual state component is for.
        :param visualStateClassName: The name of the class that represents the visual states.
        """
        self.visualStateClassName = visualStateClassName
        self._visualStates = {}

    def onSave(self, dataSection):
        """
        Save the visual state component to a data section.
        :param dataSection: The data section to save to. This is a pydoc.Section object.
        """
        dataSection.writeString('visualStates', self.visualStateClassName)
        visualStatesSection = dataSection._visualStates
        for stateName, state in self._visualStates.items():
            stateSection = visualStatesSection.createSection(stateName)
            state.onSave(stateSection)

    def onLoad(self, dataSection):
        """
        Load the visual state component from a data section.
        :param dataSection: The data section to load from. This is a pydoc.Section object.
        """
        if dataSection.has_key('visualStates'):
            visualStatesSection = dataSection._visualStates
            if visualStatesSection.has_key('external'):
                extName = visualStatesSection._external.asString
                ext = ResMgr.openSection(extName)
                if ext is not None:
                    visualStatesSection = ext
                else:
                    ERROR_MSG("Failed to open external visual state '%s'." % extName)
            self.visualStateClassName = visualStatesSection.asString
            components = self.visualStateClassName.strip('"').split('.')
            module = __import__('__main__')
            for comp in components[:-1]:
                module = getattr(module, comp)

            visualStateClass = getattr(module, components[-1])
            for stateName, stateSection in visualStatesSection.items():
                visualState = visualStateClass()
                visualState.onLoad(stateSection)
                self._visualStates[stateName] = visualState

        return

    def setVisualState(self, stateName):
        """
        Set the visual state of the component.
        :param stateName: The name of the visual state to set.
        """
        state = self._visualStates.get(stateName, None)
        if state:
            state.apply(self)
        else:
            ERROR_MSG("No Visual State '%s' on %s" % (stateName, self))
        return
