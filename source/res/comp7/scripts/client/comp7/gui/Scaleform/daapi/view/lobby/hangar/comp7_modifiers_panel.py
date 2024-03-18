# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/hangar/comp7_modifiers_panel.py

# Import necessary modules and classes.
from comp7.constants import COMP7_SEASON_MODIFIERS_DOMAIN
from comp7.gui.impl.lobby.tooltips.comp7_modifiers_domain_tooltip_view import Comp7ModifiersDomainTooltipView
from frameworks.wulf import ViewFlags, ViewSettings, ViewModel
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

# Define Comp7ModifiersPanelInject class to handle the injection of components.
class Comp7ModifiersPanelInject(InjectComponentAdaptor):
    __slots__ = ('__view',)

    def __init__(self):
        # Initialize the superclass.
        super(Comp7ModifiersPanelInject, self).__init__()
        # Initialize the __view variable.
        self.__view = None
        return

    def _makeInjectView(self, *args):
        # Create an instance of Comp7ModifiersPanel and assign it to __view.
        self.__view = Comp7ModifiersPanel()
        # Return the __view instance.
        return self.__view

    def _dispose(self):
        # Dispose of the __view instance and call the superclass's dispose method.
        self.__view = None
        super(Comp7ModifiersPanelInject, self)._dispose()
        return


# Define Comp7ModifiersPanel class to create the view.
class Comp7ModifiersPanel(ViewImpl):

    def __init__(self, flags=ViewFlags.VIEW):
        # Initialize the superclass with the given flags and settings.
        settings = ViewSettings(R.views.lobby.comp7.SeasonModifier())
        settings.flags = flags
        settings.model = ViewModel()
        super(Comp7ModifiersPanel, self).__init__(settings)

    def createToolTipContent(self, event, contentID):
        # Create and return a Comp7ModifiersDomainTooltipView instance for the given event
