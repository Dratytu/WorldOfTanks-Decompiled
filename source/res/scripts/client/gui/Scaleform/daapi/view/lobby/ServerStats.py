# Python bytecode 2.7 (decompiled from Python 2.7)


import logging
import BigWorld
import constants
from wg_async import wg_await, wg_async
from gui.Scaleform.daapi.view.servers_data_provider import ServersDataProvider
from gui.impl.dialogs.builders import ResSimpleDialogBuilder
from gui.impl.dialogs.dialogs import showSimple
from gui.impl.gen import R
from gui.impl.pub.dialog_window import DialogFlags
from gui.prb_control.entities.base.legacy.listener import ILegacyListener
from helpers import dependency
from helpers import i18n
from predefined_hosts import g_preDefinedHosts, HOST_AVAILABILITY, REQUEST_RATE
from gui import GUI_SETTINGS
from gui.shared import events
from gui.shared.utils.functions import makeTooltip
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.Scaleform.daapi.view.meta.ServerStatsMeta import ServerStatsMeta
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.game_control import IServerStatsController, IReloginController


_logger = logging.getLogger(__name__)


class ServerStats(ServerStatsMeta, ILegacyListener):
    serverStats = dependency.descriptor(IServerStatsController)
    reloginCtrl = dependency.descriptor(IReloginController)
    connectionMgr = dependency.descriptor(IConnectionManager)
    _settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(ServerStats, self).__init__()
        self.__isListSelected = False


@wg_async
def relogin(self, peripheryID):
    # ...


def startListenCsisUpdate(self, startListen):
    # ...


def _populate(self):
    # ...


def _dispose(self):
    # ...


def _updateCurrentServerInfo(self):
    # ...


def _updateServersList(self):
    # ...


def _updateRoamingCtrl(self, event=None):
    # ...


def __onStatsReceived(self):
    # ...


def __onServersUpdate(self, _=None):
    # ...


def __onReloing(self, isCompleted):
    # ...
