# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/__init__.py

from gui.Scaleform.framework.entities.View import View  # Importing the View class from the gui.Scaleform.framework.entities module

class LobbySubView(View):
    """
    A subview of the lobby that inherits from the base View class.
    """
    __background_alpha__ = 0.6  # A class-level variable that sets the background alpha value for this subview.

    def setEnvironment(self, app):
        """
        Sets the background alpha value for the given app instance.

        :param app: The app instance to set the background alpha value for.
        """
        app.setBackgroundAlpha(self.__background_alpha__)  # Sets the background alpha value for the given app instance using the class-level variable.
        super(LobbySubView, self).setEnvironment(app)  # Calls the superclass's setEnvironment method with the given app instance.
