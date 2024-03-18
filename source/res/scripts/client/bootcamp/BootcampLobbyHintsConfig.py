# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/bootcamp/BootcampLobbyHintsConfig.py

# Import necessary modules
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from Bootcamp import BOOTCAMP_UI_COMPONENTS

# Define the BootcampLobbyHintsConfig class
class BootcampLobbyHintsConfig:
    # Initialize the battleButton attribute
    battleButton = {
        # Specify the viewAlias, path, hideBorder, and customHint properties
        'viewAlias': VIEW_ALIAS.BOOTCAMP_INTRO_VIDEO,
        'path': 'btnSelect',
        'hideBorder': True,
        'customHint': 'BCIconTextBigButtonFxUI'
    }

    # Initialize the objects attribute as a dictionary
    objects = {
        # Define the InBattleRepairKit object
        'InBattleRepairKit': {
            # Specify the viewAlias, path, slotIndex, customHint, and padding properties
            'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
            'path': 'consumablesPanel:index=slotIndex',
            'slotIndex': 4,
            'customHint': 'BCHudConsumableHintUI',
            'padding': {'left': 6,
                        'right': -6,
                        'top': 28,
                        'bottom': -6}
        },

        # Define the InBattleHealKit object
        'InBattleHealKit': {
            # Specify the viewAlias, path, slotIndex, customHint, and padding properties
            'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
            'path': 'consumablesPanel:index=slotIndex',
            'slotIndex': 3,
            'customHint': 'BCHudConsumableHintUI',
            'padding': {'left': 6,
                        'right': -6,
                        'top': 28,
                        'bottom': -6}
        },

        # Define the InBattleExtinguisher object
        'InBattleExtinguisher': {
            # Specify the viewAlias, path, slotIndex, customHint, and padding properties
            'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
            'path': 'consumablesPanel:index=slotIndex',
            'slotIndex': 5,
            'customHint': 'BCHudConsumableHintUI',
            'padding': {'left': 6,
                        'right': -6,
                        'top': 28,
                        'bottom': -6}
        },

        # Define the FragCorrelationBar object
        'FragCorrelationBar': {
            # Specify the viewAlias, path, padding, and customHint properties
            'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
            'path': 'fragCorrelationBar',
            'padding': {'bottom': -7},
            'customHint': 'BCAppearFragCorrelationHintUI'
        },

        # Define the Minimap object
        'Minimap': {
            # Specify the viewAlias, path, padding, and customHint properties
            'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
            'path': 'minimap.mapHit',
            'padding': {'left': -15,
                        'top': -15,
                        'right': 2,
                        'bottom': 2},
            'customHint': 'BCHudMinimapHintUI'
        },

        # Define the ConsumablesAppear object
        'ConsumablesAppear': {
            # Specify the viewAlias, path, slotIndex, customHint, and padding properties
            'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
            'path': 'consumablesPanel:index=slotIndex.iconLoader',
            'slotIndex': 4,
            'customHint': 'BCAppearEquipmentHintUI'
        },

        # Define the MinimapAppear object
        'MinimapAppear': {
            # Specify the viewAlias, path, padding, and customHint properties
            'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
            'path': 'minimap.background',
            'padding': {'left': -14,
                        'right': 1,
                        'top': -14,
                        'bottom': 1},
            'customHint': 'BCAppearMinimapHintUI'
        },

        # Define the ConsumableSlot4 object
        'ConsumableSlot4': {
            # Specify the viewAlias, path, slotIndex, customHint, and padding properties
            'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
            'path': 'consumablesPanel:index=slotIndex.iconLoader',
            'slotIndex': 3,
            'customHint': 'BCHudTintHintUI'
        },

        # Define the ConsumableSlot5 object
        'ConsumableSlot5': {
            # Specify the viewAlias, path, slotIndex, customHint, and padding properties
            'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
            'path': 'consumablesPanel:index=slotIndex.iconLoader',
            'slotIndex': 4,
            'customHint': 'BCHudTintHintUI'
        },

        # Define the ConsumableSlot6 object
        'ConsumableSlot6': {
            # Specify the viewAlias, path, slotIndex, customHint, and padding properties
            'viewAlias': VIEW_ALIAS.BOOTCAMP_BATTLE_PAGE,
            'path': 'consumablesPanel:index=slotIndex.iconLoader',
            'slotIndex': 5,
            'customHint': 'BCHudTintHintUI'
        },

        # Define the DamagePanelHealthbar object
        'Damage
