# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/shared/tooltips/battle_royale_modules.py

from gui.Scaleform.daapi.view.common.battle_royale.params import getModuleParameters, getVehicleParameters  # Import functions for getting module and vehicle parameters
from gui.Scaleform.genConsts.ATLAS_CONSTANTS import ATLAS_CONSTANTS  # Import constants for the atlas icons
from gui.doc_loaders.battle_royale_settings_loader import getTreeModuleIcon, getTreeModuleHeader  # Import functions for getting module icons and headers
from gui.shared.formatters import text_styles  # Import text style functions
from gui.shared.gui_items import GUI_ITEM_TYPE  # Import constants for item types
from gui.shared.tooltips import TOOLTIP_TYPE, formatters  # Import tooltip types and formatter functions
from gui.shared.tooltips.common import BlocksTooltipData  # Import base class for tooltips

_TOOLTIP_MIN_WIDTH = 410  # Set minimum width for the tooltip

class BattleRoyaleModulesTooltip(BlocksTooltipData):

    def __init__(self, context):
        # Initialize the tooltip with a given context and set its content margin, margins, and width
        super(BattleRoyaleModulesTooltip, self).__init__(context, TOOLTIP_TYPE.MODULE)
        self._setContentMargin(top=0, left=0, bottom=20, right=20)
        self._setMargins(10, 15)
        self._setWidth(_TOOLTIP_MIN_WIDTH)

    def _packBlocks(self, *args, **kwargs):
        # Pack and return the blocks for the tooltip
        self.item, currentModule = self.context.buildItem(*args, **kwargs)
        items = super(BattleRoyaleModulesTooltip, self)._packBlocks()
        module = self.item
        if module is None:
            return []
        else:
            leftPadding = 20
            rightPadding = 20
            topPadding = 20
            textGap = -2
            headerBlock = HeaderBlockConstructor.construct(module)
            items.append(formatters.packBuildUpBlockData(headerBlock, padding=formatters.packPadding(left=leftPadding, right=rightPadding, top=topPadding)))
            paramsBlock = ParamsBlockConstructor.construct(module, currentModule, self._getVehicle())
            if paramsBlock:
                items.append(formatters.packBuildUpBlockData(paramsBlock, padding=formatters.packPadding(left=leftPadding, top=2), gap=textGap))
            return items

    def _getVehicle(self):
        # Return the vehicle object from the context
        return self.context.getVehicle()


class HeaderBlockConstructor(object):

    @classmethod
    def construct(cls, module):
        # Construct and return the header block for the tooltip
        return cls.__constructVehicle(module) if module.itemTypeID == GUI_ITEM_TYPE.VEHICLE else cls.__constructModule(module)

    @classmethod
    def __constructModule(cls, module):
        # Construct and return the header block for a module
        block = []
        moduleDescr = module.descriptor
        icon = getTreeModuleIcon(module)
        if icon:
            block.append(formatters.packAtlasIconTextBlockData(title=text_styles.highTitle(getTreeModuleHeader(module)), desc=text_styles.standard(moduleDescr.userString), atlas=ATLAS_CONSTANTS.COMMON_BATTLE_LOBBY, icon=icon, iconPadding=formatters.packPadding(right=12), txtGap=1, txtPadding=formatters.packPadding(top=7)))
        return block

    @classmethod
    def __constructVehicle(cls, vehicle):
        # Construct and return the header block for a vehicle
        block = []
        block.append(formatters.packAtlasIconTextBlockData(title=text_styles.highTitle(vehicle.userName), atlas=ATLAS_CONSTANTS.COMMON_BATTLE_LOBBY, icon='vehicle', iconPadding=formatters.packPadding(right=12), txtGap=1, txtPadding=formatters.packPadding(top=7)))
        return block


class ParamsBlockConstructor(object):

    @staticmethod
    def construct(module, currentModule, vehicle):
        # Construct and return the parameters block for the tooltip
        block = []
        if module.itemTypeID != GUI_ITEM_TYPE.VEHICLE:
            params = getModuleParameters(module, vehicle, currentModule)
            leftPadding = 40
        else:
            params = getVehicleParameters(vehicle)
            leftPadding = -45
        for item in params:
            bottomPadding = 10 if item.get('isLastInGroup', False) else 0
            block.append(formatters.packTextParameterBlockData(name=item['description'], value=item['value'], valueWidth=1
