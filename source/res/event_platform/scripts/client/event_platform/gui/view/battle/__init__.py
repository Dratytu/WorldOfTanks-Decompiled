# Python bytecode 2.7 (decompiled from Python 2.7)

# This script is a part of the event_platform package and contains the initialization for the battle-related views.

# Import necessary modules and classes.
from frameworks.wulf import WindowLayer  # For handling window layers.
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS  # For defining view aliases.

# Import the EventBattlePage class, which is a custom Scaleform view for event battles.
from event_platform.gui.impl.event_battle_page import EventBattlePage

# Import necessary classes and functions from the gui.Scaleform.framework package.
from gui.Scaleform.framework import ViewSettings, ScopeTemplates

# Define the __all__ variable to list the public components of this module.
__all__ = ('EventBattlePage',)

# Define a function to return context menu handlers. Currently, this function does not contain any code.
def getContextMenuHandlers():
    pass


# Define a function to return view settings. This function initializes the EventBattlePage view with its settings.
def getViewSettings():
    return (
        ViewSettings(  # Create a ViewSettings instance.
            VIEW_ALIAS.CLASSIC_BATTLE_PAGE,  # Set the view alias to CLASSIC_BATTLE_PAGE.
            EventBattlePage,  # Set the view class to EventBattlePage.
            'battlePage.swf',  # Set the SWF file name.
            WindowLayer.VIEW,  # Set the window layer to VIEW.
            None,  # Set the custom context menu handlers to None.
            ScopeTemplates.DEFAULT_SCOPE  # Set the scope template to DEFAULT_SCOPE.
        ),
    )


# Define a function to return business handlers. Currently, this function does not contain any code.
def getBusinessHandlers():
    pass

