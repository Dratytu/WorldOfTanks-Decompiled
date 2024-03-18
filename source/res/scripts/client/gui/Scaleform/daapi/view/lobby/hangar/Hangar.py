# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/Hangar.py
import logging # Import the logging module for logging messages
from functools import partial # Import the partial function for creating partial functions
import typing # Import the typing module for type hints
import BigWorld # Import the BigWorld module for working with the game world
from CurrentVehicle import g_currentVehicle # Import g_currentVehicle from CurrentVehicle for accessing the current vehicle
from HeroTank import HeroTank # Import HeroTank from HeroTank for working with hero tanks
from PlayerEvents import g_playerEvents # Import g_playerEvents from PlayerEvents for handling player events
from account_helpers import AccountSettings # Import AccountSettings from account_helpers for accessing account settings
from account_helpers.AccountSettings import NATION_CHANGE_VIEWED # Import NATION_CHANGE_VIEWED from AccountSettings for accessing the nation change viewed setting
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS # Import SETTINGS_SECTIONS from ServerSettingsManager for accessing settings sections
from battle_pass_common import BATTLE_PASS_CONFIG_NAME # Import BATTLE_PASS_CONFIG_NAME from battle_pass_common for accessing the battle pass configuration name
from constants import Configs, DOG_TAGS_CONFIG, PREBATTLE_TYPE, QUEUE_TYPE, RENEWABLE_SUBSCRIPTION_CONFIG # Import various constants from constants for working with game constants
from frameworks.wulf import WindowFlags, WindowLayer, WindowStatus # Import various window-related classes and flags from frameworks.wulf
from gui.ClientUpdateManager import g_clientUpdateManager # Import g_clientUpdateManager from ClientUpdateManager for handling client updates
from gui.Scaleform.Waiting import Waiting # Import Waiting from Scaleform.Waiting for showing and hiding waiting messages
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS # Import VIEW_ALIAS from settings.views for accessing view aliases
from gui.Scaleform.daapi.view.lobby.LobbySelectableView import LobbySelectableView # Inherit from LobbySelectableView for implementing a lobby selectable view
from gui.Scaleform.daapi.view.lobby.epicBattle import epic_helpers # Import epic_helpers from epicBattle for working with epic battles
from gui.Scaleform.daapi.view.lobby.hangar.carousel_event_entry_widget import isAnyEntryVisible # Import isAnyEntryVisible from carousel_event_entry_widget for checking if any carousel event entry is visible
from gui.Scaleform.daapi.view.lobby.mapbox import mapbox_helpers # Import mapbox_helpers from mapbox for working with mapbox
from gui.Scaleform.daapi.view.meta.HangarMeta import HangarMeta # Inherit from HangarMeta for implementing the hangar view meta
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA # Import POP_UP_CRITERIA from containers for defining pop-up criteria
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams # Import SFViewLoadParams from loaders for defining view load parameters
from gui.Scaleform.genConsts.DAILY_QUESTS_WIDGET_CONSTANTS import DAILY_QUESTS_WIDGET_CONSTANTS # Import DAILY_QUESTS_WIDGET_CONSTANTS from genConsts.DAILY_QUESTS_WIDGET_CONSTANTS for accessing daily quests widget constants
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES # Import HANGAR_ALIASES from genConsts.HANGAR_ALIASES for accessing hangar aliases
from gui.Scaleform.genConsts.HANGAR_CONSTS import HANGAR_CONSTS # Import HANGAR_CONSTS from genConsts.HANGAR_CONSTS for accessing hangar constants
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS # Import TOOLTIPS_CONSTANTS from genConsts.TOOLTIPS_CONSTANTS for accessing tooltips constants
from gui.game_control.links import URLMacros # Import URLMacros from game_control.links for working with map links
from gui.game_loading.resources.consts import Milestones # Import Milestones from game_loading.resources.consts for accessing game loading milestones
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates, CameraRelatedEvents # Import CameraMovementStates and CameraRelatedEvents from hangar_camera_common for working with hangar cameras
from gui.hangar_presets.hangar_gui_helpers import ifComponentAvailable # Import ifComponentAvailable from hangar_presets.hangar_gui_helpers for checking if a component is available
from gui.impl import backport # Import backport from impl for working with backported strings
from gui.impl.gen import R # Import R from impl.gen for accessing generated resource keys
from gui.marathon.marathon_event import MarathonEvent # Import MarathonEvent from marathon.marathon_event for working with marathon events
from gui.periodic_battles.models import PrimeTimeStatus # Import PrimeTimeStatus from periodic_battles.models for working with prime time statuses
from gui.prb_control import prb_getters # Import prb_getters from prb_control for working with prb getters
from gui.prb_control.ctrl_events import g_prbCtrlEvents # Import g_prbCtrlEvents from prb_control.ctrl_events for working with prb control events
from gui.prb_control.entities.listener import IGlobalListener # Inherit from IGlobalListener for implementing a global listener
from gui.promo.hangar_teaser_widget import TeaserViewer # Import TeaserViewer from promo.hangar_teaser_widget for working with hangar teasers
from gui.
