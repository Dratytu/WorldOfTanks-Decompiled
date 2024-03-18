# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/VehicleInfoWindow.py

import typing
from debug_utils import LOG_ERROR
from gui.impl import backport
from gui.impl.gen import R
from gui.Scaleform import MENU
from gui.Scaleform.daapi.view.meta.VehicleInfoMeta import VehicleInfoMeta
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE
from gui.shared.formatters import getRoleTextWithLabel
from gui.shared.items_parameters import formatters
from gui.shared.utils import AUTO_RELOAD_PROP_NAME, TURBOSHAFT_ENGINE_POWER, TURBOSHAFT_SPEED_MODE_SPEED, TURBOSHAFT_SWITCH_TIME, TURBOSHAFT_INVISIBILITY_MOVING_FACTOR, TURBOSHAFT_INVISIBILITY_STILL_FACTOR, ROCKET_ACCELERATION_ENGINE_POWER, ROCKET_ACCELERATION_SPEED_LIMITS, ROCKET_ACCELERATION_REUSE_AND_DURATION, DUAL_ACCURACY_COOLING_DELAY, SHOT_DISPERSION_ANGLE
from helpers import i18n, dependency
from items import tankmen
from items.components.crew_skins_constants import NO_CREW_SKIN_ID
from nation_change.nation_change_helpers import iterVehTypeCDsInNationGroup
from nation_change_helpers.client_nation_change_helper import getChangeNationTooltip
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IVehicleComparisonBasket
from skeletons.gui.shared import IItemsCache
from skeletons.gui.lobby_context import ILobbyContext
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from account_helpers import AccountSettings
from account_helpers.AccountSettings import NATION_CHANGE_VIEWED
if typing.TYPE_CHECKING:
    from account_helpers.settings_core.ServerSettingsManager import ServerSettingsManager  # NoQA


class _Highlight(object):
    """
    A helper class to highlight specific parameters of a vehicle.
    """
    __slots__ = ('__checker', '__highlight')

    def __init__(self, checker):
        """
        Initialize the _Highlight object with a checker function.

        :param checker: A function that checks if the parameter should be highlighted.
        """
        super(_Highlight, self).__init__()
        self.__highlight = None
        self.__checker = checker
        return

    def __nonzero__(self):
        """
        Check if the parameter should be highlighted.

        :return: True if the parameter should be highlighted, False otherwise.
        """
        if self.__highlight is None:
            self.__highlight = self.__checker()
        return self.__highlight


def _highlightsMap(settings, vehicle=None):
    """
    Create a mapping of parameters and their highlight status.

    :param settings: The settings to use for highlighting.
    :param vehicle: The vehicle to check for dual accuracy.
    :return: A dictionary of parameter names and their corresponding _Highlight objects.
    """
    config = (    (    (AUTO_RELOAD_PROP_NAME,), _Highlight(lambda : settings.checkAutoReloadHighlights(increase=True))),
     (    (TURBOSHAFT_ENGINE_POWER,
       TURBOSHAFT_SPEED_MODE_SPEED,
       TURBOSHAFT_SWITCH_TIME,
       TURBOSHAFT_INVISIBILITY_STILL_FACTOR,
       TURBOSHAFT_INVISIBILITY_MOVING_FACTOR), _Highlight(lambda : settings.checkTurboshaftHighlights(increase=True))),
     (    (ROCKET_ACCELERATION_ENGINE_POWER, ROCKET_ACCELERATION_SPEED_LIMITS, ROCKET_ACCELERATION_REUSE_AND_DURATION), _Highlight(lambda : settings.checkRocketAccelerationHighlights(increase=True))),
     (    (DUAL_ACCURACY_COOLING_DELAY, SHOT_DISPERSION_ANGLE), _Highlight(lambda : vehicle.descriptor.hasDualAccuracy and settings.checkDualAccuracyHighlights(increase=True))))
    mapping = [ zip(params, [highlight] * len(params)) for params, highlight in config ]
    return dict([ item for sub in mapping for item in sub ])


class VehicleInfoWindow(VehicleInfoMeta):
    """
    The VehicleInfoWindow class is responsible for displaying vehicle information in a pop-up window.
    """
    _itemsCache = dependency.descriptor(IItemsCache)
    _comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)
    _settingsCore = dependency.descriptor(ISettingsCore)
    _lobbyContext = dependency.instance(ILobbyContext)

    def __init__(self, ctx=None):
        """
        Initialize the VehicleInfoWindow with a vehicle compact descriptor.

        :param ctx: The context dictionary that may contain the vehicle compact descriptor.
        """
        super(VehicleInfoWindow, self).__init__()
        self.__vehicleCompactDescr = ctx.get('vehicleCompactDescr', 0)
        serverSettings = self._settingsCore.serverSettings
        vehicle = self._itemsCache.items.getItemByCD(self.__vehicleCompactDescr)
        self.__highlightsMap = _highlightsMap(serverSettings, vehicle)

    def onCancelClick(self):
        """
        Close the window when the cancel button is clicked.
        """
        self.destroy()

    def onWindowClose(self):
        """
        Close the window when it is
