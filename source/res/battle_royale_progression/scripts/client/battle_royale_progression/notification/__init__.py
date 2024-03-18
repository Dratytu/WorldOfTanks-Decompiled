# This Python script contains the initialization code for Battle Royale progression notifications.

# Import necessary modules and classes.
from battle_royale_progression.notification.actions_handlers import ShowBRProgressionActionHandler
from gui.shared.system_factory import registerNotificationsActionsHandlers

# Define a function to register Battle Royale progression notification handlers.
def registerClientNotificationHandlers():
    # Register the ShowBRProgressionActionHandler to handle Battle Royale progression notifications.
    registerNotificationsActionsHandlers((ShowBRProgressionActionHandler,))

# Call the registerClientNotificationHandlers function to initialize the notification handlers.
registerClientNotificationHandlers()
