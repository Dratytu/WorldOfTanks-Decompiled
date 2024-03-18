# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanSearchWindowMeta.py

from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView  # Imported to inherit from AbstractWindowView

class ClanSearchWindowMeta(AbstractWindowView):

    # search function takes a single argument 'text' and prints an override error message
    def search(self, text):
        self._printOverrideError('search')

    # previousPage function prints an override error message
    def previousPage(self):
        self._printOverrideError('previousPage')

    # nextPage function prints an override error message
    def nextPage(self):
        self._printOverrideError('nextPage')

    # dummyButtonPress function prints an override error message
    def dummyButtonPress(self):
        self._printOverrideError('dummyButtonPress')

    # as_getDPS method returns the result of flashObject.as_getDP() if DAAPI is initialized, otherwise returns None
    def as_getDPS(self):
        return self.flashObject.as_getDP() if self._isDAAPIInited() else None

    # as_setInitDataS method sets the initial data using the 'data' argument if DAAPI is initialized, otherwise does nothing
    def as_setInitDataS(self, data):
        return self.flashObject.as_setInitData(data) if self._isDAAPIInited() else None

    # as_setStateDataS method sets the state data using the 'data' argument if DAAPI is initialized, otherwise does nothing
    def as_setStateDataS(self, data):
        return self.flashObject.as_setStateData(data) if self._isDAAPIInited() else None

    # as_setDummyS method sets the dummy data using the 'data' argument if DAAPI is initialized, otherwise does nothing
    def as_setDummyS(self, data):
        return self.flashObject.as_setDummy(data) if
