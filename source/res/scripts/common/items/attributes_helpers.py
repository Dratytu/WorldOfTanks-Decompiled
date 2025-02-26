# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/common/items/attributes_helpers.py
from items._xml import raiseWrongXml
from typing import Dict, Tuple, Iterable, List, TYPE_CHECKING
if TYPE_CHECKING:
    import ResMgr
STATIC_ATTR_PREFIX = 'miscAttrs/'
DYNAMIC_ATTR_PREFIX = 'dynAttrs/'
ALLOWED_STATIC_ATTRS = {'additiveShotDispersionFactor',
 'ammoBayHealthFactor',
 'ammoBayReduceFineFactor',
 'antifragmentationLiningFactor',
 'armorSpallsDamageDevicesFactor',
 'backwardMaxSpeedKMHTerm',
 'centerRotationFwdSpeedFactor',
 'chassis/shotDispersionFactors/movement',
 'chassis/shotDispersionFactors/rotation',
 'chassisHealthAfterHysteresisFactor',
 'chassisHealthFactor',
 'chassisRepairSpeedFactor',
 'circularVisionRadiusFactor',
 'circularVisionRadiusBaseFactor',
 'crewChanceToHitFactor',
 'crewLevelIncrease',
 'damageFactor',
 'deathZones/sensitivityFactor',
 'decreaseOwnSpottingTime',
 'demaskFoliageFactor',
 'demaskMovingFactor',
 'engineHealthFactor',
 'enginePowerFactor',
 'engineReduceFineFactor',
 'fireStartingChanceFactor',
 'forwardMaxSpeedKMHTerm',
 'fuelTankHealthFactor',
 'gun/shotDispersionFactors/afterShot',
 'gun/shotDispersionFactors/turretRotation',
 'gun/shotDispersionFactors/whileGunDamaged',
 'gunAimingTimeFactor',
 'gunHealthFactor',
 'gunReloadTimeFactor',
 'healthFactor',
 'increaseEnemySpottingTime',
 'invisibilityBaseAdditive',
 'invisibilityAdditiveTerm',
 'invisibilityMultFactor',
 'invisibilityFactorAtShot',
 'maxWeight',
 'multShotDispersionFactor',
 'onMoveRotationSpeedFactor',
 'onStillRotationSpeedFactor',
 'radioHealthFactor',
 'rammingFactor',
 'repairSpeedFactor',
 'repeatedStunDurationFactor',
 'rollingFrictionFactor',
 'stunResistanceDuration',
 'stunResistanceEffect',
 'surveyingDeviceHealthFactor',
 'turretRotationSpeed',
 'turretRotatorHealthFactor',
 'vehicleByChassisDamageFactor',
 'moduleDamageFactor',
 'engineAndFuelTanksDamageFactor'}
ALLOWED_DYNAMIC_ATTRS = {'additiveShotDispersionFactor',
 'chassis/shotDispersionFactors/movement',
 'chassis/shotDispersionFactors/rotation',
 'circularVisionRadius',
 'crewChanceToHitFactor',
 'crewLevelIncrease',
 'crewRolesFactor',
 'damageFactor',
 'deathZones/sensitivityFactor',
 'engine/fireStartingChance',
 'engine/power',
 'enginePowerFactor',
 'gun/aimingTime',
 'gun/changeShell/reloadFactor',
 'gun/piercing',
 'gun/reloadTime',
 'gun/rotationSpeed',
 'gun/shotDispersionFactors/turretRotation',
 'healthBurnPerSecLossFraction',
 'healthFactor',
 'radio/distance',
 'ramming',
 'repairSpeed',
 'repeatedStunDurationFactor',
 'stunResistanceDuration',
 'stunResistanceEffect',
 'turret/rotationSpeed',
 'vehicle/maxSpeed',
 'vehicle/maxSpeed/forward',
 'vehicle/maxSpeed/backward',
 'vehicle/rotationSpeed',
 'vehicle/bkMaxSpeedBonus',
 'vehicle/fwMaxSpeedBonus',
 'moduleDamageFactor',
 'engineAndFuelTanksDamageFactor'}
ALLOWED_ATTRS = {STATIC_ATTR_PREFIX: ALLOWED_STATIC_ATTRS,
 DYNAMIC_ATTR_PREFIX: ALLOWED_DYNAMIC_ATTRS}
ALLOWED_ATTR_PREFIXES = set(ALLOWED_ATTRS.keys())

class MODIFIER_TYPE:
    MUL = 'mul'
    ADD = 'add'


def _parseAttrName(complexName):
    for attrPrefix in ALLOWED_ATTR_PREFIXES:
        if complexName.startswith(attrPrefix):
            return (attrPrefix, intern(complexName[len(attrPrefix):]))

    return (None, None)


def readModifiers(xmlCtx, section):
    xmlCtx = (xmlCtx, section.name)
    modifiers = []
    for opType, data in section.items():
        name = data.readString('name')
        value = data.readFloat('value')
        modifier = createModifier(xmlCtx, opType, name, value)
        if modifier:
            modifiers.append(modifier)

    return modifiers


def createModifier(ctx, opType, name, value):
    if opType not in (MODIFIER_TYPE.MUL, MODIFIER_TYPE.ADD):
        return raiseWrongXml(ctx, opType, 'Unknown operation type')
    attrType, attrName = _parseAttrName(name)
    if attrType not in ALLOWED_ATTRS:
        return raiseWrongXml(ctx, name, 'Unknown attribute type')
    return raiseWrongXml(ctx, name, 'Unknown attribute name') if attrName not in ALLOWED_ATTRS.get(attrType) else (opType,
     attrType,
     attrName,
     value)


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


class SingleCollectorHelper(object):
    _EMPTY_CHECKER = {MODIFIER_TYPE.ADD: lambda value: isclose(value, 0.0),
     MODIFIER_TYPE.MUL: lambda value: isclose(value, 1.0)}
    _APPLIERS = {MODIFIER_TYPE.ADD: lambda currentValue, addValue: currentValue + addValue,
     MODIFIER_TYPE.MUL: lambda currentValue, addValue: currentValue * addValue}

    @staticmethod
    def isEmpty(opType, value):
        return SingleCollectorHelper._EMPTY_CHECKER[opType](value)

    @staticmethod
    def collect(total, modifiersList, attrPrefix):
        isEmpty = SingleCollectorHelper.isEmpty
        appliers = SingleCollectorHelper._APPLIERS
        for modifiers in modifiersList:
            for opType, attrType, attrName, value in modifiers:
                if attrType != attrPrefix:
                    continue
                if isEmpty(opType, value):
                    continue
                total[attrName] = appliers[opType](total[attrName], value)


class AggregatedCollectorHelper(object):
    _EMPTY_CHECKER = {MODIFIER_TYPE.ADD: lambda value: isclose(value, 0.0),
     MODIFIER_TYPE.MUL: lambda value: isclose(value, 0.0)}
    _MERGERS = {MODIFIER_TYPE.ADD: lambda currentValue, addValue: currentValue + addValue,
     MODIFIER_TYPE.MUL: lambda currentValue, addValue: currentValue + (addValue - 1)}
    _APPLIERS = {MODIFIER_TYPE.ADD: lambda currentValue, addValue: currentValue + addValue,
     MODIFIER_TYPE.MUL: lambda currentValue, addValue: currentValue * (addValue + 1)}

    @staticmethod
    def isEmpty(opType, value):
        return AggregatedCollectorHelper._EMPTY_CHECKER[opType](value)

    @staticmethod
    def collect(total, modifiersList, attrPrefix):
        uniqueAttrs = dict()
        mergers = AggregatedCollectorHelper._MERGERS
        for modifiers in modifiersList:
            for opType, attrType, attrName, value in modifiers:
                if attrType != attrPrefix:
                    continue
                key = (attrName, opType)
                uniqueAttrs[key] = mergers[opType](uniqueAttrs.get(key, 0.0), value)

        isEmpty = AggregatedCollectorHelper.isEmpty
        appliers = AggregatedCollectorHelper._APPLIERS
        for (attrName, opType), value in uniqueAttrs.iteritems():
            if isEmpty(opType, value):
                continue
            total[attrName] = appliers[opType](total[attrName], value)


def onCollectAttributes(total, modifiersList, attrPrefix, asAggregated):
    if asAggregated:
        AggregatedCollectorHelper.collect(total, modifiersList, attrPrefix)
    else:
        SingleCollectorHelper.collect(total, modifiersList, attrPrefix)
