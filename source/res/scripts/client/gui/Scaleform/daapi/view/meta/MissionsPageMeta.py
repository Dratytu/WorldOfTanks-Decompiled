# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/MissionsPageMeta.py

import gui.Scaleform.framework.entities.View as View

class MissionsPageMeta(View.View):
    """
    The MissionsPageMeta class is a subclass of the View class and represents a view for displaying missions.
    """

    def resetFilters(self):
        """
        The resetFilters method resets the filters for the missions view.
        """
        self._printOverrideError('resetFilters')

    def onTabSelected(self, alias, prefix):
        """
        The onTabSelected method is called when a tab is selected in the missions view.
        :param alias: The alias of the selected tab.
        :param prefix: The prefix of the selected tab.
        """
        self._printOverrideError('onTabSelected')

    def onClose(self):
        """
        The onClose method is called when the missions view is closed.
        """
        self._printOverrideError('onClose')

    def as_setTabsDataProviderS(self, dataProvider):
        """
        The as_setTabsDataProviderS method sets the data provider for the tabs in the missions view.
        :param dataProvider: The data provider for the tabs.
        :return: The result of the as_setTabsDataProvider call on the flash object.
        """
        return self.flashObject.as_setTabsDataProvider(dataProvider) if self._isDAAPIInited() else None

    def as_showFilterS(self, visible, topShadowVisible):
        """
        The as_showFilterS method shows or hides the filter in the missions view.
        :param visible: A boolean indicating whether the filter should be visible or not.
        :param topShadowVisible: A boolean indicating whether the top shadow should be visible or not.
        :return: The result of the as_showFilter call on the flash object.
        """
        return self.flashObject.as_showFilter(visible, topShadowVisible) if self._isDAAPIInited() else None

    def as_showFilterCounterS(self, countText, isFilterApplied):
        """
        The as_showFilterCounterS method shows the filter counter in
