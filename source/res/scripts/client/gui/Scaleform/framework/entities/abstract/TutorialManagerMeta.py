# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/TutorialManagerMeta.py

import gui.Scaleform.framework.entities.BaseDAAPIComponent  # Importing BaseDAAPIComponent to inherit its properties and methods

class TutorialManagerMeta(BaseDAAPIComponent):
    """
    This class is a meta for TutorialManager, which is used to manage tutorials in the game.
    It contains methods for handling tutorial events and updating tutorial data.
    """

    def onComponentFound(self, componentId, viewTutorialId):
        """
        Called when a tutorial component is found.
        :param componentId: The ID of the found component.
        :param viewTutorialId: The ID of the tutorial view.
        """
        self._printOverrideError('onComponentFound')

    def onComponentDisposed(self, componentId):
        """
        Called when a tutorial component is disposed.
        :param componentId: The ID of the disposed component.
        """
        self._printOverrideError('onComponentDisposed')

    def onTriggerActivated(self, componentId, triggerId, state):
        """
        Called when a tutorial trigger is activated.
        :param componentId: The ID of the component containing the trigger.
        :param triggerId: The ID of the activated trigger.
        :param state: The new state of the trigger.
        """
        self._printOverrideError('onTriggerActivated')

    def onEffectCompleted(self, componentId, effectType):
        """
        Called when a tutorial effect is completed.
        :param componentId: The ID of the component containing the effect.
        :param effectType: The type of the completed effect.
        """
        self._printOverrideError('onEffectCompleted')

    def onUbTrackedVarChanged(self, viewTutorialId, botNetID, varName, value):
        """
        Called when a tutorial tracked variable is changed.
        :param viewTutorialId: The ID of the tutorial view.
        :param botNetID: The ID of the bot network.
        :param varName: The name of the changed variable.
        :param value: The new value of the variable.
        """
        self._printOverrideError('onUbTrackedVarChanged')

    def as_setSystemEnabledS(self, value):
        """
        Sets the system enabled state.
        :param value: The new system enabled state.
        :return: None
        """
        return self.flashObject.as_setSystemEnabled(value) if self._isDAAPIInited() else None

    def as_setDescriptionsS(self, descriptions):
        """
        Sets the tutorial descriptions.
        :param descriptions: The new tutorial descriptions.
        :return: None
        """
        return self.flashObject.as_setDescriptions(descriptions) if self._isDAAPIInited() else None

    def as_setCriteriaS(self, criteriaName, criteriaValue):
        """
        Sets the tutorial criteria.
        :param criteriaName: The name of the criteria.
        :param criteriaValue: The value of the criteria.
        :return: None
        """
        return self.flashObject.as_setCriteria(criteriaName, criteriaValue) if self._isDAAPIInited() else None

    def as_setTriggersS(self, componentId, triggers):
        """
        Sets the tutorial triggers for a component.
        :param componentId: The ID of the component.
        :param triggers: The new triggers for the component.
        :return: None
        """
        return self.flashObject.as_setTriggers(componentId, triggers) if self._isDAAPIInited() else None

    def as_showEffectS(self, viewTutorialId, componentId, effType, builderData):
        """
        Shows a tutorial effect.
        :param viewTutorialId: The ID of the tutorial view.
        :param componentId: The ID of the component.
        :param effType: The type of the effect.
        :param builderData: The data for building the effect.
        :return: None
        """
        return self.flashObject.as_showEffect(viewTutorialId, componentId, effType, builderData) if self._isDAAPIInited() else None

    def as_hideEffectS(self, viewTutorialId, componentId, effType, builder):
        """
        Hides a tutorial effect.
        :param viewTutorialId: The ID of the tutorial view.
        :param componentId: The ID of the component.
        :param effType: The type of the effect.
        :param builder: The data for building the hiding effect.
        :return: None
        """
        return self.flashObject.as_hideEffect(viewTutorialId, componentId, effType, builder) if self._isDAAPIInited() else None

    def as_setComponentViewCriteriaS(self, componentId, viewTutorialId):
        """
        Sets the view criteria for a tutorial component.
        :param componentId: The ID of the component.
        :param viewTutorialId: The ID of the tutorial view.
        :return: None
        """
        return self.flashObject.as_setComponentViewCriteria(componentId
