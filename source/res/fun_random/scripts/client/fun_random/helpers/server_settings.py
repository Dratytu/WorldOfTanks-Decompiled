# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/helpers/server_settings.py

from collections import namedtuple
from fun_random_common.fun_constants import DEFAULT_ASSETS_PACK, DEFAULT_SETTINGS_KEY, DEFAULT_PRIORITY, UNKNOWN_WWISE_REMAPPING, UNKNOWN_EVENT_ID, FunSubModeImpl
from shared_utils import makeTupleByDict

# Define a namedtuple for FunSubModeClientConfig with the following fields:
# subModeImpl: The implementation of the subscription mode
# assetsPointer: The pointer to the assets
# settingsKey: The key for settings
# priority: The priority level
# wwiseRemapping: The Wwise remapping
# battleModifiersDescr: The battle modifiers description
# infoPageUrl: The URL for the info page
class FunSubModeClientConfig(namedtuple('_FunSubModeClientConfig', ('subModeImpl', 'assetsPointer', 'settingsKey', 'priority', 'wwiseRemapping', 'battleModifiersDescr', 'infoPageUrl'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        # Set default values for the fields and update with the provided keyword arguments
        defaults = dict(subModeImpl=FunSubModeImpl.DEFAULT, assetsPointer=DEFAULT_ASSETS_PACK, settingsKey=DEFAULT_SETTINGS_KEY, priority=DEFAULT_PRIORITY, wwiseRemapping=UNKNOWN_WWISE_REMAPPING, battleModifiersDescr=(), infoPageUrl='')
        defaults.update(kwargs)
        return super(FunSubModeClientConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        # Return a new instance of the namedtuple with default values
        return cls(FunSubModeImpl.DEFAULT, DEFAULT_ASSETS_PACK, DEFAULT_SETTINGS_KEY, DEFAULT_PRIORITY, UNKNOWN_WWISE_REMAPPING, (), '')

# Define a namedtuple for FunSubModeFiltrationConfig with the following fields:
# levels: The levels
# forbiddenClassTags: The set of forbidden class tags
# forbiddenVehTypes: The set of forbidden vehicle types
# allowedVehTypes: The set of allowed vehicle types
class FunSubModeFiltrationConfig(namedtuple('FunSubModeFiltrationConfig', ('levels', 'forbiddenClassTags', 'forbiddenVehTypes', 'allowedVehTypes'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        # Set default values for the fields and update with the provided keyword arguments
        defaults = dict(levels=(), forbiddenClassTags=set(), forbiddenVehTypes=set(), allowedVehTypes=set())
        defaults.update(kwargs)
        return super(FunSubModeFiltrationConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        # Return a new instance of the namedtuple with default values
        return cls((), set(), set(), set())

# Define a namedtuple for FunSubModeSeasonalityConfig with the following fields:
# isEnabled: A boolean indicating whether the seasonality is enabled
# peripheryIDs: The set of periphery IDs
# seasons: A dictionary of seasons with integer keys and values
# primeTimes: A dictionary of prime times with integer keys and values
# cycleTimes: A tuple of cycle times
class FunSubModeSeasonalityConfig(namedtuple('FunSubModeSeasonalityConfig', ('isEnabled', 'peripheryIDs', 'seasons', 'primeTimes', 'cycleTimes'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        # Set default values for the fields and update with the provided keyword arguments
        defaults = dict(isEnabled=False, peripheryIDs=set(), seasons={}, primeTimes={}, cycleTimes=())
        defaults.update(kwargs)
        cls.__packSeasonalityConfig(defaults)
        return super(FunSubModeSeasonalityConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        # Return a new instance of the namedtuple with default values
        return cls(False, set(), {}, {}, ())

    def asDict(self):
        # Return a dictionary representation of the namedtuple
        return self._asdict()

    @classmethod
    def __packSeasonalityConfig(cls, data):
        # Pack the seasonality config data
        data['primeTimes'] = {int(peripheryID):value for peripheryID, value in data['primeTimes'].iteritems()}
        data['seasons'] = {int(seasonID):value for seasonID, value in data['seasons'].iteritems()}

# Define a namedtuple for FunSubModeConfig with the following fields:
# eventID: The ID of the event
# isEnabled: A boolean indicating whether the subscription mode is enabled
# seasonality: An instance of FunSubModeSeasonalityConfig
# filtration: An instance of FunSubModeFiltrationConfig
# client: An instance of FunSubModeClientConfig
class FunSubModeConfig(namedtuple('_FunSubModeConfig', ('eventID', 'isEnabled', 'seasonality', 'filtration', 'client'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        # Set default values for the fields and update with the provided keyword arguments
        defaults = dict(eventID=UNKNOWN_EVENT_ID, isEnabled=False, seasonality={}, filtration={}, client={})
        allowedFields = defaults.keys()
        defaults.update(kwargs)
        cls.__packConfigPart(FunSubModeClientConfig, 'client', defaults)
        cls.__packConfigPart(FunSubModeFiltrationConfig, 'filtration', defaults)
        cls.__packConfigPart(FunSubModeSeasonalityConfig, 'seasonality', defaults)
        defaults = cls.__filterAllowedFields(defaults, allowedFields)
        return super(FunSubModeConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        # Return a new instance of the namedtuple with default values
        return cls(UNKNOWN_EVENT_ID, False, {}, {}, {})

    @classmethod
    def __
