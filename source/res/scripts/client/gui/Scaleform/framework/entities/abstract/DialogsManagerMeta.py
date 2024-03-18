# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/DialogsManagerMeta.py

# The base class for managing dialogs in the Scaleform framework
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DialogsManagerMeta(BaseDAAPIComponent):
    """
    The DialogsManagerMeta class is responsible for managing dialogs in the Scaleform framework.
    It is built on top of the BaseDAAPIComponent class.
    """

    def showSimpleI18nDialog(self, i18nKey, handlers):
        """
        Displays a simple dialog with a localized message.

        :param i18nKey: The key of the localized message to be displayed.
        :type i18nKey: str
        :param handlers: A dictionary of handlers for the dialog's buttons.
        :type handlers: dict
        """
        # Print an error message indicating that the method has been overridden
        self._printOverrideError('showSimpleI18nDialog')
