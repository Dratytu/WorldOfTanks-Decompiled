# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/shared/tooltips/tankman.py
import math
from typing import List, Optional
import nations
from gui import makeHtmlString
from gui.game_control.restore_contoller import getTankmenRestoreInfo
from gui.Scaleform.genConsts.BLOCKS_TOOLTIP_TYPES import BLOCKS_TOOLTIP_TYPES
from gui.Scaleform.genConsts.ICON_TEXT_FRAMES import ICON_TEXT_FRAMES
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.tooltips.common import BlocksTooltipData
from gui.shared.tooltips import ToolTipDataField, ToolTipAttrField, ToolTipData, TOOLTIP_TYPE, formatters
from gui.shared.formatters import text_styles, moneyWithIcon
from gui.shared.gui_items.Tankman import Tankman
from gui.shared.gui_items.Vehicle import Vehicle
from helpers import dependency
from helpers import i18n
from helpers import time_utils
from helpers.i18n import makeString
from items.components.component_constants import EMPTY_STRING
from items.tankmen import SKILLS_BY_ROLES, getSkillsConfig, compareMastery
from shared_utils import findFirst
from skeletons.gui.shared import IItemsCache
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.game_control import IBattleRoyaleController
TANKMAN_DISMISSED = 'dismissed'
_TIME_FORMAT_UNITS = [('days', time_utils.ONE_DAY), ('hours', time_utils.ONE_HOUR), ('minutes', time_utils.ONE_MINUTE)]

class TankmanRoleLevelField(ToolTipDataField):

    def _getValue(self):
        tankman = self._tooltip.item
        return tankman.realRoleLevel.lvl if tankman else 0


class TankmanRoleBonusesField(ToolTipDataField):

    class BONUSES(object):
        COMMANDER = 0
        BROTHERHOOD = 1
        EQUIPMENTS = 2
        DEVICES = 3
        PENALTY = 4

    def __init__(self, context, name, ids):
        super(TankmanRoleBonusesField, self).__init__(context, name)
        self.__ids = ids

    def _getValue(self):
        tankman = self._tooltip.item
        result = 0
        if tankman:
            bonuses = tankman.realRoleLevel.bonuses
            for idx in self.__ids:
                result += int(math.ceil(float(bonuses[idx])))

        return result


class TankmanCurrentVehicleAttrField(ToolTipAttrField):
    itemsCache = dependency.descriptor(IItemsCache)

    def _getItem(self):
        tankman = self._tooltip.item
        return self.itemsCache.items.getVehicle(tankman.vehicleInvID) if tankman and tankman.isInTank else None


class TankmanNativeVehicleAttrField(ToolTipAttrField):
    itemsCache = dependency.descriptor(IItemsCache)

    def _getItem(self):
        tankman = self._tooltip.item
        return self.itemsCache.items.getItemByCD(tankman.vehicleNativeDescr.type.compactDescr)


class TankmanSkillListField(ToolTipDataField):

    def _getValue(self):
        tankman = self._tooltip.item
        skillsList = self._getBaseSkills(tankman)
        self._addNewSkills(tankman, skillsList)
        return skillsList

    @staticmethod
    def _getBaseSkills(tankman):
        skillsList = []
        for idx, skill in enumerate(tankman.skills):
            skillsList.append({'id': str(idx),
             'label': skill.userName,
             'level': skill.level,
             'enabled': tankman.isInTank or skill.isEnable})

        return skillsList

    def _addNewSkills(self, tankman, skillsList):
        newSkillsCount, newSkillLevel = tankman.newSkillCount
        if newSkillsCount > 0:
            if newSkillsCount > 2:
                newSkills = [str(newSkillsCount - 1) + 'x100']
            elif newSkillsCount == 2:
                newSkills = [100]
            else:
                newSkills = []
            if newSkillLevel > 0:
                newSkills.append(newSkillLevel)
            newSkillStr = makeString(TOOLTIPS.BARRACKS_TANKMEN_RECOVERY_NEWSKILL)
            for idx, skillLevel in enumerate(newSkills, start=len(skillsList)):
                skillsList.append({'id': str(idx),
                 'label': newSkillStr,
                 'level': skillLevel,
                 'enabled': False})


class BattleRoyaleTankmanSkillListField(TankmanSkillListField):
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)

    def _getValue(self):
        skills = self.__battleRoyaleController.getBrCommanderSkills()
        skillsList = []
        for idx, skill in enumerate(skills):
            skillsList.append({'id': str(idx),
             'label': skill.userName,
             'level': skill.level,
             'enabled': skill.isEnable})

        return skillsList

    def _addNewSkills(self, tankman, skillsList):
        pass


class TankmanNewFreeSkillCountField(ToolTipDataField):

    def _getValue(self):
        tankman = self._tooltip.item
        return tankman.newFreeSkillsCount if not tankman.isDismissed else 0


class TankmanNewSkillCountField(ToolTipDataField):

    def _getValue(self):
        tankman = self._tooltip.item
        return tankman.newSkillCount[0] if not tankman.isDismissed else 0


def formatRecoveryLeftValue(secondsLeft):
    closestUnit = findFirst(lambda (k, v): v < secondsLeft, _TIME_FORMAT_UNITS)
    if closestUnit is not None:
        name, factor = closestUnit
        timeLeft = int(math.ceil(float(secondsLeft) / factor))
        return makeString(TOOLTIPS.template_all_short(name), value=timeLeft)
    else:
        return makeString(TOOLTIPS.TEMPLATE_TIME_LESSTHENMINUTE)


def getRecoveryStatusText(restoreInfo):
    price, timeLeft = restoreInfo
    if not price:
        itemsCache = dependency.instance(IItemsCache)
        restoreConfig = itemsCache.items.shop.tankmenRestoreConfig
        duration = restoreConfig.billableDuration - restoreConfig.freeDuration
        text = makeString(TOOLTIPS.BARRACKS_TANKMEN_RECOVERY_FREE_BODY, totalLeftValue=formatRecoveryLeftValue(timeLeft), freeLeftValue=formatRecoveryLeftValue(timeLeft - duration), price=moneyWithIcon(restoreConfig.cost), withMoneyLeftValue=formatRecoveryLeftValue(duration))
    else:
        text = makeString(TOOLTIPS.BARRACKS_TANKMEN_RECOVERY_GOLD_BODY, totalLeftValue=formatRecoveryLeftValue(timeLeft), price=moneyWithIcon(price))
    return text_styles.main(text)


class TankmanStatusField(ToolTipDataField):
    itemsCache = dependency.descriptor(IItemsCache)

    def _getValue(self):
        header = ''
        text = ''
        statusTemplate = '#tooltips:tankman/status/%s'
        tankman = self._tooltip.item
        vehicle = None
        if tankman.isInTank:
            vehicle = self.itemsCache.items.getVehicle(tankman.vehicleInvID)
        nativeVehicle = self.itemsCache.items.getItemByCD(tankman.vehicleNativeDescr.type.compactDescr)
        if tankman.isDismissed:
            return {'header': text_styles.warning(TOOLTIPS.BARRACKS_TANKMEN_RECOVERY_HEADER),
             'text': getRecoveryStatusText(getTankmenRestoreInfo(tankman)),
             'level': TANKMAN_DISMISSED}
        else:
            inactiveRoles = []
            if tankman.isInTank:
                for skill in tankman.skills:
                    if not skill.isEnable:
                        role = self.__getRoleBySkill(skill)
                        if role not in inactiveRoles:
                            inactiveRoles.append(role)

            if vehicle is not None and nativeVehicle.innationID != vehicle.innationID and not vehicle.isWotPlus:
                if (vehicle.isPremium or vehicle.isPremiumIGR) and vehicle.type in nativeVehicle.tags:
                    header = makeString(statusTemplate % 'wrongPremiumVehicle/header')
                    text = makeString(statusTemplate % 'wrongPremiumVehicle/text') % {'vehicle': vehicle.shortUserName}
                else:
                    header = makeString(statusTemplate % 'wrongVehicle/header') % {'vehicle': vehicle.shortUserName}
                    text = makeString(statusTemplate % 'wrongVehicle/text')
            elif inactiveRoles:

                def roleFormat(role):
                    return makeString(statusTemplate % 'inactiveSkillsRoleFormat') % makeString(getSkillsConfig().getSkill(role).userString)

                header = makeString(statusTemplate % 'inactiveSkills/header')
                text = makeString(statusTemplate % 'inactiveSkills/text') % {'skills': ', '.join([ roleFormat(role) for role in inactiveRoles ])}
            return {'header': header,
             'text': text,
             'level': Vehicle.VEHICLE_STATE_LEVEL.WARNING}
            return

    def __getRoleBySkill(self, skill):
        for role, skills in SKILLS_BY_ROLES.iteritems():
            if skill.name in skills:
                return role


class NotRecruitedTooltipData(BlocksTooltipData):

    def __init__(self, ctx):
        super(NotRecruitedTooltipData, self).__init__(ctx, TOOLTIP_TYPE.NOT_RECRUITED_TANKMAN)
        self._setWidth(350)
        self.item = None
        return

    def _packBlocks(self, *args, **kwargs):
        items = super(NotRecruitedTooltipData, self)._packBlocks()
        item = self.context.buildItem(*args)
        self.item = item
        blocks = list()
        blocks.append(formatters.packImageTextBlockData(title=text_styles.highTitle(item.getFullUserName()), desc=text_styles.main(item.getLabel())))
        specialIcon = item.getSpecialIcon()
        blocks.append(formatters.packImageBlockData(img=specialIcon if specialIcon is not None else item.getBigIcon(), align=BLOCKS_TOOLTIP_TYPES.ALIGN_CENTER, width=350 if specialIcon is not None else -1, height=238 if specialIcon is not None else -1))
        blocks.append(formatters.packSeparatorBlockData(paddings=formatters.packPadding(top=-40)))
        descrStr = i18n.makeString(item.getDescription())
        hasDescr = descrStr != EMPTY_STRING
        if hasDescr:
            blocks.append(formatters.packTextBlockData(text_styles.main(descrStr), useHtml=True, padding=formatters.packPadding(top=18)))
        howToGetStr = i18n.makeString(item.getHowToGetInfo())
        hasHowToGetStr = howToGetStr != EMPTY_STRING
        if hasHowToGetStr:
            blocks.append(formatters.packTextBlockData(text_styles.middleTitle(backport.text(R.strings.tooltips.notrecruitedtankman.howToGet())), useHtml=True, padding=formatters.packPadding(top=17 if hasDescr else 18, bottom=5)))
            blocks.append(formatters.packTextBlockData(text_styles.main(howToGetStr), useHtml=True, padding=formatters.packPadding()))
        freeSkills = item.getFreeSkills()
        if freeSkills:
            tankmanSkill = item.getTankmanSkill()
            blocks.append(formatters.packTextBlockData(text_styles.middleTitle(TOOLTIPS.NOTRECRUITEDTANKMAN_FREESKILLSTITLE), useHtml=True, padding=formatters.packPadding(top=17 if hasDescr else 18, bottom=10)))
            blocks.append(formatters.packImageListParameterBlockData(listIconSrc=[ formatters.packImageListIconData(tankmanSkill(skillName=skillName).bigIconPath) for skillName in freeSkills ], columnWidth=52, rowHeight=52, verticalGap=10, horizontalGap=10))
        skills = item.getEarnedSkills(multiplyNew=True)
        if skills:
            tankmanSkill = item.getTankmanSkill()
            blocks.append(formatters.packTextBlockData(text_styles.middleTitle(TOOLTIPS.NOTRECRUITEDTANKMAN_SKILLSTITLE), useHtml=True, padding=formatters.packPadding(top=17 if hasDescr else 18, bottom=10)))
            blocks.append(formatters.packImageListParameterBlockData(listIconSrc=[ formatters.packImageListIconData(tankmanSkill(skillName=skillName).bigIconPath) for skillName in skills ], columnWidth=52, rowHeight=52, verticalGap=10, horizontalGap=10))
        expiryTime = item.getExpiryTime()
        if expiryTime:
            blocks.append(formatters.packTextBlockData(text_styles.middleTitle(TOOLTIPS.NOTRECRUITEDTANKMAN_EXPIRETITLE), useHtml=True, padding=formatters.packPadding(top=20 if skills else (17 if hasDescr else 16), bottom=2)))
            expireDateStr = makeString(TOOLTIPS.NOTRECRUITEDTANKMAN_USEBEFORE, date=expiryTime)
            blocks.append(formatters.packTextParameterWithIconBlockData(name=text_styles.premiumVehicleName(expireDateStr), value='', icon=ICON_TEXT_FRAMES.RENTALS, padding=formatters.packPadding(left=-60, bottom=-18), iconYOffset=3))
        items.append(formatters.packBuildUpBlockData(blocks, padding=formatters.packPadding(bottom=-5)))
        return items


class BattleRoyaleTankmanTooltipDataBlock(BlocksTooltipData):
    _itemsCache = dependency.descriptor(IItemsCache)
    _lobbyContext = dependency.descriptor(ILobbyContext)
    _skillIconNamePadding = {'padding': formatters.packPadding(left=65),
     'titlePadding': formatters.packPadding(left=6),
     'iconPadding': formatters.packPadding(top=-1)}

    def __init__(self, context):
        super(BattleRoyaleTankmanTooltipDataBlock, self).__init__(context, TOOLTIP_TYPE.SKILL)
        self._setWidth(320)
        self.item = None
        return

    def _packBlocks(self, *args, **kwargs):
        items = super(BattleRoyaleTankmanTooltipDataBlock, self)._packBlocks()
        item = self.context.buildItem(*args, **kwargs)
        if item is None:
            return items
        else:
            self.item = item
            vehicle = None
            if item.isInTank:
                vehicle = self._itemsCache.items.getVehicle(item.vehicleInvID)
            fullUserName = self._getFullUserName(item)
            titleBlock = []
            titleBlock.append(formatters.packTitleDescBlock(title=text_styles.highTitle(fullUserName), desc=text_styles.main(self._getTankmanDescription(item))))
            if vehicle and vehicle.isXPToTman:
                isLessMastered = True
                for slotIdx, tman in vehicle.crew:
                    if tman is not None:
                        res = compareMastery(tman.descriptor, self.item.descriptor)
                        if res < 0 or res == 0 and slotIdx < self.item.vehicleSlotIdx:
                            isLessMastered = False
                            break

                if isLessMastered:
                    titleBlock.append(self._makeXpToTankmanCaption())
            items.append(formatters.packBuildUpBlockData(titleBlock))
            innerBlock = []
            if vehicle:
                self._createLabel(innerBlock)
                self._createVehicleBlock(innerBlock, vehicle)
            if innerBlock:
                items.append(formatters.packBuildUpBlockData(innerBlock, padding=formatters.packPadding(left=0, right=50, top=-5, bottom=0), linkage=BLOCKS_TOOLTIP_TYPES.TOOLTIP_BUILDUP_BLOCK_WHITE_BG_LINKAGE))
            commonStatsBlock = []
            self._createFreeSkillsBlock(commonStatsBlock)
            self._createEarnedSkillsBlock(commonStatsBlock)
            if commonStatsBlock:
                items.append(formatters.packBuildUpBlockData(commonStatsBlock, gap=5))
            return items

    def _makeXpToTankmanCaption(self):
        return formatters.packImageTextBlockData(img=backport.image(R.images.gui.maps.icons.library.tman_acc_training_24x24()), padding=formatters.packPadding(bottom=0, top=16, left=0), imgPadding=formatters.packPadding(top=-2, right=6), desc=text_styles.main(backport.text(R.strings.tooltips.hangar.crew.xpToTmen())))

    def _getSign(self, val):
        return '' if val < 0 else '+'

    def _getBonusValue(self, tankman, ids):
        result = 0
        if tankman:
            bonuses = tankman.realRoleLevel.bonuses
            for idx in ids:
                result += bonuses[idx]

        return int(result)

    def _getVehicleName(self, vehicle=None, nativeVehicle=None):
        return text_styles.main(nativeVehicle.shortUserName) if not vehicle or nativeVehicle.shortUserName == vehicle.shortUserName else text_styles.critical(nativeVehicle.shortUserName)

    def _createLabel(self, innerBlock):
        innerBlock.append(formatters.packTextBlockData(text=makeHtmlString('html_templates:lobby/textStyle', 'grayTitle', {'message': backport.text(R.strings.tooltips.hangar.crew.assignedTo())})))

    def _createFreeSkillsBlock(self, commonStatsBlock):
        freeSkills = self.item.freeSkills
        if not freeSkills:
            return
        commonStatsBlock.append(formatters.packTextBlockData(text=makeHtmlString('html_templates:lobby/textStyle', 'grayTitle', {'message': makeString(TOOLTIPS.HANGAR_CREW_FREESKILLS)})))
        for freeSkill in freeSkills:
            commonStatsBlock.append(formatters.packTitleDescParameterWithIconBlockData(title=text_styles.main(freeSkill.userName), value='', icon=backport.image(R.images.gui.maps.icons.tankmen.skills.medium.dyn(freeSkill.extensionLessIconName)()), **self._skillIconNamePadding))

    def _createEarnedSkillsBlock(self, commonStatsBlock):
        field = self._getSkillList()
        _, value = field.buildData()
        skills = value[self.item.chosenFreeSkillsCount:]
        if not skills:
            return
        commonStatsBlock.append(formatters.packTextBlockData(text=makeHtmlString('html_templates:lobby/textStyle', 'grayTitle', {'message': makeString(TOOLTIPS.HANGAR_CREW_SPECIALTY_SKILLS)})))
        maxPopUpBlocks = 14
        for skill in skills[:maxPopUpBlocks]:
            commonStatsBlock.append(formatters.packTextParameterBlockData(text_styles.main(skill['label']), text_styles.stats(str(skill['level']) + '%'), valueWidth=90))

        if len(skills) > maxPopUpBlocks:
            diff = str(len(skills) - maxPopUpBlocks)
            commonStatsBlock.append(formatters.packAlignedTextBlockData(text=text_styles.middleTitle(makeString(TOOLTIPS.HANGAR_CREW_MORESKILLS, skill_cnt=diff)), align=BLOCKS_TOOLTIP_TYPES.ALIGN_CENTER))

    @classmethod
    def _getNewSkillsBlock(cls, isFree):
        if isFree:
            titleR = R.strings.tooltips.hangar.crew.new_free_skill_available.header()
        else:
            titleR = R.strings.tooltips.hangar.crew.new_skill_available.header()
        return formatters.packImageTextBlockData(img='../maps/icons/tankmen/skills/small/new_skill.png', txtOffset=20, padding=formatters.packPadding(bottom=0, top=5, left=0), imgPadding=formatters.packPadding(left=0, top=3), title=makeHtmlString('html_templates:lobby/textStyle', 'goldTextTitle', {'message': backport.text(titleR)}), desc=makeHtmlString('html_templates:lobby/textStyle', 'goldTextField', {'message': backport.text(R.strings.tooltips.hangar.crew.new_skill_available.text())}))

    def _getFullUserName(self, item):
        nationName = nations.NAMES[item.nationID]
        nationResId = R.strings.battle_royale.commanderInfo.fullName.dyn(nationName)()
        result = backport.text(nationResId)
        return result

    def _getTankmanDescription(self, _):
        return backport.text(R.strings.battle_royale.commanderInfo.commonRank())

    def _getSkillList(self):
        return BattleRoyaleTankmanSkillListField(self, 'skills')

    def _createVehicleBlock(self, innerBlock, vehicle):
        vehName = vehicle.shortUserName
        innerBlock.append(formatters.packTextBlockData(text=text_styles.stats(backport.text(R.strings.battle_royale.commanderTooltip.vehicleDescription(), vehicle=vehName)), padding=formatters.packPadding(top=10, right=-50)))


class TankmanTooltipData(ToolTipData):

    def __init__(self, context):
        super(TankmanTooltipData, self).__init__(context, TOOLTIP_TYPE.TANKMAN)
        self.fields = (ToolTipAttrField(self, 'name', 'fullUserName'),
         ToolTipAttrField(self, 'rank', 'rankUserName'),
         ToolTipAttrField(self, 'role', 'roleUserName'),
         ToolTipAttrField(self, 'roleLevel'),
         ToolTipAttrField(self, 'isInTank'),
         ToolTipAttrField(self, 'iconRole'),
         ToolTipAttrField(self, 'nation', 'nationID'),
         TankmanRoleLevelField(self, 'efficiencyRoleLevel'),
         TankmanRoleBonusesField(self, 'addition', [TankmanRoleBonusesField.BONUSES.COMMANDER,
          TankmanRoleBonusesField.BONUSES.EQUIPMENTS,
          TankmanRoleBonusesField.BONUSES.DEVICES,
          TankmanRoleBonusesField.BONUSES.BROTHERHOOD]),
         TankmanRoleBonusesField(self, 'penalty', [TankmanRoleBonusesField.BONUSES.PENALTY]),
         TankmanNativeVehicleAttrField(self, 'vehicleType', 'type'),
         TankmanNativeVehicleAttrField(self, 'vehicleName', 'shortUserName'),
         TankmanCurrentVehicleAttrField(self, 'currentVehicleType', 'type'),
         TankmanCurrentVehicleAttrField(self, 'currentVehicleName', 'shortUserName'),
         TankmanSkillListField(self, 'skills'),
         TankmanNewSkillCountField(self, 'newSkillsCount'),
         TankmanCurrentVehicleAttrField(self, 'vehicleContour', 'iconContour'),
         TankmanCurrentVehicleAttrField(self, 'isCurrentVehiclePremium', 'isPremium'),
         TankmanStatusField(self, 'status'))
