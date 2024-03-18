# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/carousel_event_entry_widget.py

import itertools
import typing

from gui.Scaleform.daapi.view.meta.CarouselEventEntryMeta import CarouselEventEntryMeta
from gui.impl.gen import R
from gui.prb_control.dispatcher import g_prbLoader
from gui.prb_control.entities.base.listener import IPrbListener
from gui.shared.system_factory import collectCarouselEventEntryPoints

# Dict to store CarouselEventEntry instances
_VIEWS = {}

