# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/cgf_components/zone_components.py

import functools
import logging
import BigWorld
import CGF
import GenericComponents
import Triggers
import UIComponents
from cgf_script.component_meta_class import ComponentProperty as CompProp, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery, onProcessQuery, autoregister
from constants import IS_CLIENT
from helpers import dependency

# Define a custom exception for invalid zone types
class InvalidZoneType(Exception):
    pass


if IS_CLIENT:
    from skeletons.gui.battle_session import IBattleSessionProvider
    from Vehicle import Vehicle
    from gui.battle_control import avatar_getter
else:
    avatar_getter = None

    class IBattleSessionProvider(object):
        pass


    class Vehicle(object):
        pass


_logger = logging.getLogger(__name__)

class ZoneUINotificationType(object):
    DANGER_ZONE = 'dangerZone'
    WARNING_ZONE = 'warningZone'
    MAP_DEATH_ZONE = 'mapDeathZone'


@registerComponent
class ZoneMarker(object):
    """
    Component for defining a zone marker.
    """
    category = 'UI'
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = 'Zone Marker'

    def __init__(self):
        super(ZoneMarker, self).__init__()
        self.id = None
        self.startTime = 0
        self.finishTime = 0
        return

    @property
    def duration(self):
        """
        Returns the duration of the zone marker.
        """
        return max(self.finishTime - self.startTime, 0)

    @property
    def markerProgress(self):
        """
        Returns the progress of the zone marker as a percentage.
        """
        if self.isActive():
            restTime = self.finishTime - BigWorld.serverTime()
            if self.duration and restTime > 0:
                return float(restTime) / self.duration * 100

    def isActive(self):
        """
        Returns True if the zone marker is active, False otherwise.
        """
        return self.finishTime >= BigWorld.serverTime() >= self.startTime


@registerComponent
class ZoneUINotification(object):
    """
    Component for defining a zone UI notification.
    """
    category = 'UI'
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = 'Zone UI Notification'
    trigger = CompProp(type=CGFMetaTypes.LINK, editorName='Trigger', value=Triggers.AreaTriggerComponent)
    zoneType = CompProp(type=CGFMetaTypes.STRING, editorName='Zone Type', value=ZoneUINotificationType.DANGER_ZONE, annotations={'comboBox': {ZoneUINotificationType.WARNING_ZONE: ZoneUINotificationType.WARNING_ZONE,
                  ZoneUINotificationType.DANGER_ZONE: ZoneUINotificationType.DANGER_ZONE,
                  ZoneUINotificationType.MAP_DEATH_ZONE: ZoneUINotificationType.MAP_DEATH_ZONE}})

    def __init__(self):
        super(ZoneUINotification, self).__init__()
        self.id = None
        self.startTime = 0
        self.finishTime = 0
        self.enterReactionID = None
        self.exitReactionID = None
        self.inZoneVehicles = set([])
        return

    def isActive(self):
        """
        Returns True if the zone UI notification is active, False otherwise.
        """
        return self.finishTime >= BigWorld.serverTime()


@autoregister(presentInAllWorlds=True, domain=CGF.DomainOption.DomainClient)
class MapZoneManager(CGF.ComponentManager):
    """
    Component manager for handling map zones.
    """
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    queryUINotifications = CGF.QueryConfig(ZoneUINotification)

    def __init__(self):
        super(MapZoneManager, self).__init__()
        self.__subscriptionsCount = 0

    @onAddedQuery(CGF.GameObject, ZoneMarker, GenericComponents.TransformComponent, tickGroup='PostHierarchy')
    def onMarkerToZoneAdded(self, go, zoneMarker, transform):
        """
        Called when a zone marker is added to a game object.
        """
        _logger.debug('on marker to zone added')
        zoneMarker.id = go.id
        mapZones = self.__guiSessionProvider.shared.mapZones
        if mapZones:
            mapZones.addMarkerToZone(zoneMarker, transform.worldTransform)

    @onRemovedQuery(ZoneMarker)
    def onMakerFromZoneRemoved(self, zoneMarker):
        """
        Called when a zone marker is removed from a zone.
        """
        _logger.debug('on maker from zone removed')
        mapZones = self.__guiSessionProvider.shared.mapZones
        if mapZones:
            mapZones.removeMarkerFromZone(zoneMarker)

    @onProcessQuery(ZoneMarker, tickGroup='Simulation', period=1.0)
    def onMarkerUpdated(self, zoneMarker):
        """
        Called to update the progress of a zone marker.
        """
        _logger.debug('on marker updated')
        mapZones = self.__guiSessionProvider.shared.mapZones
        if mapZones and zoneMarker.isActive():
            mapZones.onMarkerProgressUpdated(zoneMarker)

    @onAddedQuery(CGF.GameObject, ZoneUINotification)
    def onZoneUINotificationAdded(self
