# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanSearchWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ClanSearchWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def search(self, text):
        self._printOverrideError('search')

    def previousPage(self):
        self._printOverrideError('previousPage')

    def nextPage(self):
        self._printOverrideError('nextPage')

    def dummyButtonPress(self):
        self._printOverrideError('dummyButtonPress')

    def as_getDPS(self):
        return self.flashObject.as_getDP() if self._isDAAPIInited() else None

    def as_setInitDataS(self, data):
        """
        :param data: Represented by ClanSearchWindowInitDataVO (AS)
        """
        return self.flashObject.as_setInitData(data) if self._isDAAPIInited() else None

    def as_setStateDataS(self, data):
        """
        :param data: Represented by ClanSearchWindowStateDataVO (AS)
        """
        return self.flashObject.as_setStateData(data) if self._isDAAPIInited() else None

    def as_setDummyS(self, data):
        """
        :param data: Represented by DummyVO (AS)
        """
        return self.flashObject.as_setDummy(data) if self._isDAAPIInited() else None

    def as_setDummyVisibleS(self, visible):
        return self.flashObject.as_setDummyVisible(visible) if self._isDAAPIInited() else None