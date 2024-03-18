import typing
from abc import ABC, abstractmethod
from pathlib import Path

import ResMgr
from soft_exception import SoftException

from battle_modifiers_ext.constants_ext import REMAPPING_XML_PATH, RemappingNames

ERR_TEMPLATE = "[Remapping] {} for remapping '{}'"

class IComposer(ABC):
    @abstractmethod
    def getValue(self, ctx, oldValue):
        pass

    @abstractmethod
    def getValues(self, oldValue):
        pass

