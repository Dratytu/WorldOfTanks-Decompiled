# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/managers/ColorSchemeManager.py

# Import necessary modules
import BigWorld
from gui.Scaleform.framework.entities.abstract.ColorSchemeManagerMeta import ColorSchemeManagerMeta
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from gui.doc_loaders import GuiColorsLoader
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider

# Define the ColorSchemeManager class
class ColorSchemeManager(ColorSchemeManagerMeta):
    # Inject the ISettingsCore dependency
    settingsCore = dependency.descriptor(ISettingsCore)

    # Initialize the class
    def __init__(self):
        # Call the parent constructor
        super(ColorSchemeManager, self).__init__()
        # Load color schemes
        self.colors = GuiColorsLoader.load()

    # Get the color group based on the user's color blind setting
    def getColorGroup(self):
        return 'color_blind' if self.settingsCore.getSetting('isColorBlind') else 'default'

    # Get the RGBA value for a given scheme name
    def getRGBA(self, schemeName):
        return self.colors.getSubScheme(schemeName, self.getColorGroup())['rgba']

    # Get the color scheme for a given scheme name
    def getColorScheme(self, schemeName):
        scheme = self.colors.getSubScheme(schemeName, self.getColorGroup())
        transform = scheme['transform']
        return {'aliasColor': scheme['alias_color'],
         'rgb': self._packRGB(scheme['rgba']),
         'adjust': {'offset': scheme['adjust']['offset'].tuple()},
         'transform': {'mult': transform['mult'].tuple(),
                       'offset': transform['offset'].tuple()}}

    # Get the isColorBlind setting
    def getIsColorBlind(self):
        return self.settingsCore.getSetting('isColorBlind')

    # Update the color schemes
    def update(self):
        self.as_updateS()

    # Populate the class with necessary data
    def _populate(self):
        super(ColorSchemeManager, self)._populate()
        self.settingsCore.onSettingsChanged += self.__onAccountSettingsChange

    # Dispose of the class
    def _dispose(self):
        self.settingsCore.onSettingsChanged -= self.__onAccountSettingsChange
        super(ColorSchemeManager, self)._dispose()

    # Pack RGB values into a single integer
    @classmethod
    def _packRGB(cls, rgba):
        return (int(rgba[0]) << 16) + (int(rgba[1]) << 8) + (int(rgba[2]) << 0)

    # Make RGB values from a sub-scheme
    @classmethod
    def _makeRGB(cls, subScheme):
        return cls._packRGB(subScheme.get('rgb', (0, 0, 0, 0)))

    # Make adjust tuple from a sub-scheme
    @classmethod
    def _makeAdjustTuple(cls, subScheme):
        return subScheme['adjust']['offset']

    # Handle account settings change
    def __onAccountSettingsChange(self, diff):
        if 'isColorBlind' in diff:
            self.update()

# Define the BattleColorSchemeManager class
class BattleColorSchemeManager(ColorSchemeManager, IArenaVehiclesController):
    # Inject the IBattleSessionProvider dependency
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    # Initialize the class
    def __init__(self):
        # Call the parent constructor
        super(BattleColorSchemeManager, self).__init__()

    # Update color schemes and set 3D flag colors
    def update(self):
        super(BattleColorSchemeManager, self).update()
        self.__set3DFlagsColors()

    # Invalidate arena info and set 3D flag colors
    def invalidateArenaInfo(self):
        self.__set3DFlagsColors()

    # Populate the class with necessary data
    def _populate(self):
        super(BattleColorSchemeManager, self)._populate()
        self.__set3DFlagsEmblem()
        from PlayerEvents import g_playerEvents
        g_playerEvents.onTeamChanged += self.__onTeamChanged
        self.sessionProvider.addArenaCtrl(self)

    # Dispose of the class
    def _dispose(self):
        self.sessionProvider.removeArenaCtrl(self)
        from PlayerEvents import g_playerEvents
        g_playerEvents.onTeamChanged -= self.__onTeamChanged
        super(BattleColorSchemeManager, self)._dispose()

    # Set 3D flag colors based on the team
    def __set3DFlagsColors(self):
        arenaDP = self.sessionProvider.getArenaDP()
        if arenaDP is None:
            return
        teamsOnArena = arenaDP.getTeamsOnArena()
        group = self.getColorGroup()
        allyColor = self.colors.getSubScheme('flag_team_green', group)['rgba']
        enemyColor = self.colors.getSubScheme('flag_team_red', group)['rgba']
        for teamIdx in teamsOnArena:
            color = allyColor if arenaDP.isAllyTeam(teamIdx) else enemyColor
            BigWorld.wg_setFlagColor
