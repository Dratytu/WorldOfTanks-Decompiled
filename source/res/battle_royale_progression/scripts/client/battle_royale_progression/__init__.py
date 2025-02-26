# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale_progression/scripts/client/battle_royale_progression/__init__.py

def initProgression():
    # Import necessary modules for initializing battle royale progression
    from gui.game_control import registerBRProgressionAwardControllers, registerBRGameControllers
    from gui.gui_constants import registerSystemMessagesTypes
    from messenger.formatters import registerMessengerClientFormatters
    from notification import registerClientNotificationHandlers

    # Register system message types for battle royale progression
    registerSystemMessagesTypes()

    # Register battle royale progression award controllers
    registerBRProgressionAwardControllers()

    # Register client notification handlers for battle royale progression
    registerClientNotificationHandlers()

    # Register messenger client formatters for battle royale progression
    registerMessengerClientFormatters()


