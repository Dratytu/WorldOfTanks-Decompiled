# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/common/items/readers/ny_readers.py
import typing
import ResMgr
import contextlib
from constants import IS_CLIENT
from soft_exception import SoftException
from items.components.ny_components import LevelDescriptor, SlotDescriptor, TalismanDescriptor, VariadicDiscountDescriptor, ToyTransformation, ToyModelOverride
from items.components.ny_constants import MAX_ATMOSPHERE_LVL, MIN_ATMOSPHERE_LVL, TOY_TYPES, YEARS_INFO, ToySettings

@contextlib.contextmanager
def openSection(path):
    try:
        yield ResMgr.openSection(path)
    finally:
        ResMgr.purge(path)


def _readLevelRewardSection(section):
    cfg = {'id': section.readString('id')}
    cfg['level'] = level = section.readInt('level')
    if not MIN_ATMOSPHERE_LVL <= level <= MAX_ATMOSPHERE_LVL:
        raise SoftException("Wrong reward level '%d'" % level)
    return cfg


def readLevelRewards(xmlPath):
    cache = {}
    with openSection(xmlPath) as section:
        if section is None:
            raise SoftException("Can't open '%s'" % xmlPath)
        for levelSec in section.values():
            cfg = _readLevelRewardSection(levelSec)
            rewardID = cfg['id']
            if rewardID in cache:
                raise SoftException("Repeated boxID '%s'" % rewardID)
            cache[rewardID] = LevelDescriptor(cfg)

    return cache


def readCollectionRewards(xmlPath):
    cache = {}
    with openSection(xmlPath) as section:
        if section is None:
            raise SoftException("Can't open '%s'" % xmlPath)
        for reward in section.values():
            rewardID = reward.readString('id')
            collName = reward.readString('collection')
            if rewardID in cache:
                raise SoftException("Repeated boxID '%s'" % rewardID)
            prefix = rewardID[:4]
            year = prefix[2:4]
            collectionStrID = YEARS_INFO.getCollectionSettingID(collName, prefix)
            cache[rewardID] = collectionStrID
            cache[collectionStrID] = rewardID
            cache[collName + year] = rewardID

    return cache


def _readSlotSection(section):
    cfg = {'id': section.readInt('id')}
    cfg['type'] = slotType = section.readString('type')
    if slotType not in TOY_TYPES:
        raise SoftException("Wrong slot type '%s'" % slotType)
    if IS_CLIENT:
        cfg['object'] = section.readString('object')
        cfg['nodes'] = section.readString('nodes')
        cfg['direction'] = section.readString('direction')
        cfg['selectable'] = section.readBool('selectable')
        cfg['defaultToy'] = section.readInt('defaultToy', -1)
        cfg['hoverEffect'] = section.readString('hoverEffect')
    return cfg


def readSlots(xmlPath):
    cache = None
    with openSection(xmlPath) as section:
        if section is None:
            raise SoftException("Can't open '%s'" % xmlPath)
        subsections = section['slots'].values()
        numSlots = len(subsections)
        cache = [None] * numSlots
        for slotSec in subsections:
            cfg = _readSlotSection(slotSec)
            slotID = cfg['id']
            if not 0 <= slotID < numSlots:
                raise SoftException("Wrong slotID '%d'" % slotID)
            if cache[slotID] is not None:
                raise SoftException("Repeated slotID '%d'" % slotID)
            cache[slotID] = SlotDescriptor(cfg)

    return cache


def _readTalismanSection(section):
    cfg = {'id': section.readInt('id')}
    cfg['setting'] = section.readString('setting')
    return cfg


def readTalisman(xmlPath):
    cache = {}
    with openSection(xmlPath) as section:
        if section is None:
            raise SoftException("Can't open '%s" % xmlPath)
        settings = []
        maxID = len(ToySettings.NEW)
        for talismanSec in section.values():
            cfg = _readTalismanSection(talismanSec)
            talismanID = cfg['id']
            setting = cfg['setting']
            if not 0 < talismanID <= maxID:
                raise SoftException('Wrong talismanID %d' % talismanID)
            if talismanID in cache:
                raise SoftException('Repeated talismanID %d' % talismanID)
            if setting not in ToySettings.NEW:
                raise SoftException('Wrong setting %s' % setting)
            if setting in settings:
                raise SoftException('Repeated setting %s' % setting)
            settings.append(setting)
            cache[talismanID] = TalismanDescriptor(cfg)

    return cache


def _readToyTransformationNode(node):
    toyTransformation = ToyTransformation(transform=node.readMatrix('transform') if node.has_key('transform') else None, modelOverride=ToyModelOverride.createModel(node))
    return (node.readString('node'), node.readString('object'), toyTransformation)


def _readToyTransformationsSection(section):
    nodes = {}
    for subSection in section.values():
        if subSection.name == 'node':
            nodeName, objectName, transformation = _readToyTransformationNode(subSection)
            nodes[intern(objectName), intern(nodeName)] = transformation

    return (section.readString('name'), nodes)


def readToysTransformations(xmlPath):
    cache = {}
    with openSection(xmlPath) as section:
        if section is None:
            raise SoftException("Can't open '%s" % xmlPath)
        for subSection in section.values():
            modelName, nodes = _readToyTransformationsSection(subSection)
            cache[modelName] = nodes

    return cache


def buildVariadicDiscountsCache(xmlPath):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        raise SoftException("Can't open '%s'" % xmlPath)
    cache = {}
    for vdSec in section.values():
        cfg = _readVariadicDiscount(vdSec)
        vdID = cfg['id']
        if vdID in cache:
            raise SoftException("Repeated variadic discount ID '%s'" % vdID)
        cache[vdID] = VariadicDiscountDescriptor(cfg['id'], cfg['firstGoodieId'], cfg['lastGoodieId'], cfg['level'])

    return cache


def _readVariadicDiscount(section):
    cfg = {}
    cfg['id'] = section.readString('id')
    cfg['firstGoodieId'] = section.readInt('firstGoodieId')
    cfg['lastGoodieId'] = section.readInt('lastGoodieId')
    cfg['level'] = section.readInt('level')
    return cfg
