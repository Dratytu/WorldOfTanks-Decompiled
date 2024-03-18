# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/PersonalMissionsQuestAwardScreenMeta.py

# This code defines a meta class for the PersonalMissionsQuestAwardScreen, which is a view in the GUI.
# The class inherits from the View class, which is a base class for all views in the GUI.
class PersonalMissionsQuestAwardScreenMeta(View):

    # This method is called when the user clicks the close button on the view.
    def closeView(self):
        # Prints an error message if the method is not overridden in the derived class.
        self._printOverrideError('closeView')

    # This method is called when the user clicks the link for the next quest.
    def onNextQuestLinkClick(self):
        self._printOverrideError('onNextQuestLinkClick')

    # This method is called when the user clicks the button for the next quest.
    def onNextQuestBtnClick(self):
        self._printOverrideError('onNextQuestBtnClick')

    # This method is called when the user clicks the recruit button.
    def onRecruitBtnClick(self):
        self._printOverrideError('onRecruitBtnClick')

    # This method is called when the user clicks the continue button.
    def onContinueBtnClick(self):
        self._printOverrideError('onContinueBtnClick')

    # This method is called when the user clicks the OK button.
    def onOkBtnClick(self):
        self._printOverrideError('onOkBtnClick')

    # This method sets the data for the view.
    def as_setDataS(self, data):
        # Returns the result of the flashObject's as_setData method if the DAAPI is initialized, otherwise returns None.
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None
