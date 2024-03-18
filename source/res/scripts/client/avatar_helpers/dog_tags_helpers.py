# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/avatar_helpers/dog_tags_helpers.py

import random
import BigWorld
from dog_tags_common.components_config import componentConfigAdapter
from dog_tags_common.components_packer import unpack_component
from dog_tags_common.config.common import ComponentViewType
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from soft_exception import SoftException

