# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RankedBattlesSeasonCompleteViewMeta.py

# This script defines a meta class RankedBattlesSeasonCompleteViewMeta, which is a subclass of WrapperViewMeta.
# WrapperViewMeta is a base class for views that wrap other views.
class RankedBattlesSeasonCompleteViewMeta(WrapperViewMeta):

    # showRating is a method that overrides the parent class method.
    # It prints an error message when called, as the method is not implemented in this class.
    def showRating(self):
        self._printOverrideError('showRating')

    # closeView is a method that overrides the parent class method.
    # It prints an error message when called, as the method is not implemented in this class.
    def closeView(self):
        self._printOverrideError('closeView')

    # onSoundTrigger is a method that overrides the parent class method.
    # It prints an error message when called, as the method is not implemented in this class.
    def onSoundTrigger(self, soundName):
        self._printOverrideError('onSoundTrigger')

    # as_setDataS is a method that calls the corresponding Flash method as_setData.
    # It checks if the DAAPI is initialized before making the call.
    def as_setDataS(self, data):
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None

    # as_setPlaceS is a method that calls the corresponding Flash method as_setPlace.
    # It checks if the DAAPI is initialized before making the call.
    def as_setPlaceS(self, value):
        return self.flashObject.as_setPlace(value) if self._isDAAPIInited() else None

    # as_setAwardsDataS is a method that calls the corresponding Flash method as_setAwardsData.
    # It checks if the DAAPI is initialized before
