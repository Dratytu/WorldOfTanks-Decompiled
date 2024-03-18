# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/cgf_components/hangar_rules.py

import CGF
from cgf_components.tooltip_component import TooltipManager  # Tooltip manager for displaying tooltips
from cgf_components.trigger_vse_component import TriggerVSEComponentsManager  # Manager for triggering VSE components
from cgf_components.token_component import TokenManager  # Manager for handling tokens

# Register managers and rules for CGF components
from cgf_script.managers_registrator import registerManager, Rule, registerRule

# Hover, highlight, and click managers for handling user interactions
from hover_component import HoverManager
from highlight_component import HighlightManager
from on_click_components import ClickManager

# Hangar camera manager for controlling the hangar camera
from hangar_camera_manager import HangarCameraManager

@registerRule  # Rule for handling selections in the hangar
class SelectionRule(Rule):
    category = 'Hangar rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(HoverManager)  # Register HoverManager for this rule
    def reg1(self):
        return None

    @registerManager(HighlightManager)  # Register HighlightManager for this rule
    def reg2(self):
        return None

    @registerManager(ClickManager)  # Register ClickManager for this rule
    def reg3(self):
        return None

    @registerManager(TooltipManager)  # Register TooltipManager for this rule
    def reg4(self):
        return None


@registerRule  # Rule for handling the camera in the hangar
class CameraRule(Rule):
    category = 'Hangar rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(HangarCameraManager)  # Register HangarCameraManager for this rule
    def reg1(self):
        return None


@registerRule  # Rule for handling tokens in the hangar
class HangarTokenRule(Rule):
    category = 'Hangar rules'
    domain = CGF.DomainOption.DomainClient

    @registerManager(TokenManager)  # Register TokenManager for this rule
    def reg1(self):
        return None

    @registerManager(TriggerVSEComponentsManager)  # Register TriggerVSEComponentsManager for this rule
    def
