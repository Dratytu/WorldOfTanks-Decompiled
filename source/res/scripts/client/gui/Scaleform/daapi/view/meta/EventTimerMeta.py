# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/EventTimerMeta.py

import gui.Scaleform.framework.entities.BaseDAAPIComponent as BaseDAAPIComponent # Importing BaseDAAPIComponent class from the Scaleform framework.

class EventTimerMeta(BaseDAAPIComponent):

    # as_updateTimeS(self, value):
    # This method is used to update the time displayed in the timer.
    def as_updateTimeS(self, value):
        return self.flashObject.as_updateTime(value) if self._isDAAPIInited() else None # If the DAAPI is initialized, call the corresponding Flash method with the provided 'value' as an argument. Otherwise, return None.

    # as_setTimerStateS(self, state):
    # This method is used to set the state of the timer.
    def as_setTimerStateS(self, state):
        return self.flashObject.as_setTimerState(state) if self._isDAAPIInited() else None # If the DAAPI is initialized, call the corresponding Flash method with the provided 'state' as an argument. Otherwise, return None.

    # as_playFxS(self):
    # This method is used to play a visual effect (FX) on the timer.
    def as_playFxS(self):
        return self.flashObject.as_playFx() if self._isDAAPIInited() else None # If the DAAPI is initialized, call the corresponding Flash method. Otherwise, return None.

    # as_updateTitleS(self, value):
    # This method is used to update the title of the timer.
    def as_updateTitleS(self, value):
        return self.flashObject.as_updateTitle(value) if self._isDAAPIInited() else None # If the DAAPI is initialized, call the corresponding Flash method with the provided 'value' as an argument. Otherwise, return None.

    # as_updateProgressBarS(self, value, vis):
   
