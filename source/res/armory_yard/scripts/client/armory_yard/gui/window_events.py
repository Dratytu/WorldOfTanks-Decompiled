# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/window_events.py

import logging
import typing
from CurrentVehicle import HeroTankPreviewAppearance
from frameworks.wulf import WindowFlags, WindowLayer, ViewFlags
from gui.Scaleform.Waiting import Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.pub.lobby_window import LobbyWindow
from gui.impl.pub.notification_commands import WindowNotificationCommand
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from gui.shop import showBuyGoldWebOverlay, Source
from helpers import dependency
from skeletons.gui.game_control import IArmoryYardController
from skeletons.gui.impl import INotificationWindowController

# Declare a logger for this module
_logger = logging.getLogger(__name__)

@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def showArmoryYardRewardWindow(bonuses, state, stage=0, closeCallback=None, showImmediately=True, notificationMgr=None):
    # Display the Armory Yard reward window with the given bonuses, state, and stage.
    # Optionally, provide a close callback and a flag to show the window immediately.
    # The window will be appended to the notification manager's queue if showImmediately is False.
    from armory_yard.gui.impl.lobby.feature.armory_yard_rewards_view import ArmoryYardRewardsWindow
    window = ArmoryYardRewardsWindow(bonuses, state, stage, closeCallback)
    if showImmediately:
        window.load()
    else:
        notificationMgr.append(WindowNotificationCommand(window))


@dependency.replace_none_kwargs(armoryYard=IArmoryYardController)
def showArmoryYardBuyWindow(armoryYard=None, parent=None, isBlurEnabled=False, onLoadedCallback=None):
    # Display the Armory Yard buy window if the Armory Yard is active.
    from armory_yard.gui.impl.lobby.feature.armory_yard_buy_view import ArmoryYardBuyWindow
    if armoryYard.isActive():
        window = ArmoryYardBuyWindow(parent=parent, isBlurEnabled=isBlurEnabled, onLoadedCallback=onLoadedCallback)
        window.load()


@dependency.replace_none_kwargs(armoryYard=IArmoryYardController)
def showArmoryYardBundlesWindow(armoryYard=None, parent=None, isBlurEnabled=False, onLoadedCallback=None):
    # Display the Armory Yard bundles window if the Armory Yard is active.
    from armory_yard.gui.impl.lobby.feature.armory_yard_bundles_view import ArmoryYardBundlesWindow
    if armoryYard.isActive():
        window = ArmoryYardBundlesWindow(parent=parent, isBlurEnabled=isBlurEnabled, onLoadedCallback=onLoadedCallback)
        window.load()


@dependency.replace_none_kwargs(armoryYard=IArmoryYardController)
def showArmoryYardBuyBundleWindow(bundleId, armoryYard=None, parent=None, isBlurEnabled=False, onLoadedCallback=None, onClosedCallback=None):
    # Display the Armory Yard buy bundle window if the Armory Yard is active.
    from armory_yard.gui.impl.lobby.feature.armory_yard_buy_bundle_view import ArmoryYardBuyBundleWindow
    if armoryYard.isActive():
        window = ArmoryYardBuyBundleWindow(bundleId, parent=parent, isBlurEnabled=isBlurEnabled, onLoadedCallback=onLoadedCallback, onClosedCallback=onClosedCallback)
        window.load()


def showArmoryYardVideoRewardWindow(vehicle):
    # Display the Armory Yard video reward window with the given vehicle.
    from armory_yard.gui.impl.lobby.feature.armory_yard_video_reward_view import ArmoryYardVideoRewardWindow
    if vehicle is None:
        _logger.error("Armory yard reward video isn't shown. Vehicle is None")
    else:
        window = ArmoryYardVideoRewardWindow(vehicle)
        window.load()
    return


@dependency.replace_none_kwargs(armoryYard=IArmoryYardController)
def showArmoryYardIntroWindow(closeCallback=None, parent=None, armoryYard=None, loadedCallback=None):
    # Display the Armory Yard intro window with the given close callback, parent, and loaded callback.
    from armory_yard.gui.impl.lobby.feature.armory_yard_intro_view import ArmoryYardIntroWindow
    finalRewardVehicle = armoryYard.getFinalRewardVehicle()
    if finalRewardVehicle:
        window = ArmoryYardIntroWindow(finalRewardVehicle, closeCallback, parent=parent, loadedCallback=loadedCallback)
        window.load()
    else:
        _logger.error("Final reward isn't found. Please check reward config")


def showBuyGoldForArmoryYard(goldPrice):
    # Show the buy gold overlay for Armory Yard with the given gold price.
    params = {'reason': '',
     'goldPrice': goldPrice,
     'source': Source.EXTERNAL}
    showBuyGoldWebOverlay(params)


def showArmoryYardVehiclePreview(vehTypeCompDescr, showHeroT
