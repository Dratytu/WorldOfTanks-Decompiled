# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/abilities/influence_zones.py
import math
import CGF
import Math
import GenericComponents
import CombatSelectedArea
import math_utils
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from battle_royale.abilities.area_abilities import AreaAbilityVisualizer
from cgf_components.marker_component import CombatMarker
from cgf_script.bonus_caps_rules import bonusCapsManager
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from constants import IS_CLIENT
from items import vehicles

# Client-side imports
if IS_CLIENT:
    from skeletons.gui.battle_session import IBattleSessionProvider
    from InfluenceZone import InfluenceZone
else:
    # Server-side placeholders
    class Vehicle(object):
        pass

    class InfluenceZone(object):
        pass

    class IBattleSessionProvider(object):
        pass

# Register the InfluenceZoneMultiVisualizer component
@registerComponent
class InfluenceZoneMultiVisualizer(object):
    # Component properties
    editorTitle = 'Influence Zone Multi Visualizer'
    category = 'Abilities'
    domain = CGF.DomainOption.DomainClient
    influencePrefab = ComponentProperty(type=CGFMetaTypes.STRING, value='', editorName='Influence prefab', annotations={'path': '*.prefab'})
    rotateFromCenter = ComponentProperty(type=CGFMetaTypes.BOOL, value=False, editorName='Rotate from center')

# Register the InfluenceZoneTerrainArea component
@registerComponent
class InfluenceZoneTerrainArea(object):
    # Component properties
    editorTitle = 'Influence Zone Terrain Area'
    category = 'Abilities'
    domain = CGF.DomainOption.DomainClient
    fullZoneVisual = ComponentProperty(type=CGFMetaTypes.STRING, value='', editorName='Full Zone Visual', annotations={'path': '*.visual'})
    dropOffset = ComponentProperty(type=CGFMetaTypes.FLOAT, value=1000.0, editorName='Drop Offset')

    def __init__(self):
        super(InfluenceZoneTerrainArea, self).__init__()
        self.fullZoneArea = None

# Register the InfluenceZoneEquipmentComponent component
@registerComponent
class InfluenceZoneEquipmentComponent(object):
    # Component properties
    editorTitle = 'Influence Zone Equipment'
    domain = CGF.DomainOption.DomainClient
    userVisible = False
    radius = ComponentProperty(type=CGFMetaTypes.FLOAT, value=0, editorName='Radius')
    zonesCount = ComponentProperty(type=CGFMetaTypes.INT, value=0, editorName='Zones Count')
    zoneRadius = ComponentProperty(type=CGFMetaTypes.FLOAT, value=0, editorName='Zone Radius')

    def __int__(self):
        self.equipment = None

    def setupEquipment(self, equipment):
        self.equipment = equipment
        self.radius = equipment.radius
        self.zonesCount = equipment.zonesCount
        self.zoneRadius = equipment.influenceZone.radius

# Bonus caps manager for battle royale and client domain
@bonusCapsManager(ARENA_BONUS_TYPE_CAPS.BATTLEROYALE, CGF.DomainOption.DomainClient)
class InfluenceZoneVisualizationManager(CGF.ComponentManager):
    # Class variables
    __guiSessionProvider = dependency.descriptor(IBattleSessionProvider)
    ALLY_MARKER_POSTFIX = 'Ally'
    ENEMY_MARKER_POSTFIX = 'Enemy'

    # onInfluenceZoneSpawn method
    @onAddedQuery(InfluenceZone, CGF.GameObject)
    def onInfluenceZoneSpawn(self, influenceZone, go):
        # Load equipment and spawn influence zone

    # __multipositionSpawn method
    def __multipositionSpawn(self, go, multivisualizer, influenceZone, equipment, radius):
        # Spawn multiple influence zones

    # terrainAreaInit method
    @onAddedQuery(GenericComponents.TransformComponent, InfluenceZoneEquipmentComponent, InfluenceZoneTerrainArea)
    def terrainAreaInit(self, transform, influenceZoneEquipment, terrainArea):
        # Initialize terrain area

    # terrainAreaDestroy method
    @onRemovedQuery(InfluenceZoneEquipmentComponent, InfluenceZoneTerrainArea)
    def terrainAreaDestroy(self, influenceZoneEquipment, terrainArea):
        # Destroy terrain area
