# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LoginQueueWindowMeta.py

from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class LoginQueueWindowMeta(AbstractWindowView):
    # onCancelClick method is called when the user clicks on the cancel button in the login queue window
    def onCancelClick(self):
        self._printOverrideError('onCancelClick')

    # onAutoLoginClick method is called when the user clicks on the auto-login button in the login queue window
    def onAutoLoginClick(self):
        self._printOverrideError('onAutoLoginClick')

    # as_setTitleS method sets the title of the login queue window
    def as_setTitleS(self, title):
        return self.flashObject.as_setTitle(title) if self._isDAAPIInited() else None

    # as_setMessageS method sets the message displayed in the login queue window
    def as_setMessageS(self, message):
        return self.flashObject.as_setMessage(message) if self._isDAAPIInited() else None

    # as_setCancelLabelS method sets the label of the cancel button in the login queue window
    def as_setCancelLabelS(self, cancelLabel):
        return self.flashObject.as_setCancelLabel(cancelLabel) if self._isDAAPIInited() else None

    # as_showAutoLoginBtnS method shows or hides the auto-login button in the login queue window
    def as_showAutoLoginBtnS(self, value):
        return self.flashObject.as_showAutoLoginBtn(value) if self._isDAAPIInited() else None
