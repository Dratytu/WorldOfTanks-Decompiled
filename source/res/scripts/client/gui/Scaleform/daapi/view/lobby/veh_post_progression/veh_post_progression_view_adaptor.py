# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/veh_post_progression/veh_post_progression_view_adaptor.py

from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.impl.lobby.veh_post_progression.post_progression_cfg_component import PostProgressionCfgComponentView
from gui.impl.lobby.veh_post_progression.post_progression_cmp_component import PostProgressionCmpComponentView

class VehiclePostProgressionViewAdaptor(InjectComponentAdaptor):
    """
    A view adaptor for the lobby's vehicle post progression functionality.
    """
    __slots__ = ('__ctx',)

    def __init__(self
