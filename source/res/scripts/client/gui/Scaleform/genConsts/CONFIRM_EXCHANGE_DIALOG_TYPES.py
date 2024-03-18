# This module defines the different types of dialogs that can be displayed in the
# ConfirmExchangeDialog, which is used to confirm the exchange of various items
# in the game.

class CONFIRM_EXCHANGE_DIALOG_TYPES(object):
    # The different types of icons that can be displayed in the ConfirmExchangeDialog.
    # VEHICLE_ICON: A vehicle icon.
    # MODULE_ICON: A module icon.
    # PLATFORM_PACK_ICON: A platform pack icon.
    VEHICLE_ICON = 1
    MODULE_ICON = 2
    PLATFORM_PACK_ICON = 3

    # The different states that the ConfirmExchangeDialog can be in.
    # NORMAL_STATE: The default state.
    # NOT_ENOUGH_GOLD_STATE: The state where the player does not have enough gold
    #
