# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/lobby/feature/tooltips/entry_point_not_active_tooltip_view.py
from frameworks.wulf import ViewFlags, ViewSettings
import armory_yard.gui.impl.gen.view_models.views.lobby.feature.tooltips.entry_point_not_active_tooltip_view_model as entry_point_not_active_tooltip_view_model
from gui.impl.pub import ViewImpl


class EntryPointNotActiveTooltipView(ViewImpl):
    __slots__ = ()

    def __init__(self, layout_id: int):
        settings = ViewSettings(layout_id)
        settings.flags = ViewFlags.LOBBY_SUB_VIEW
        settings.model = entry_point_not_active_tooltip_view_model.EntryPointNotActiveTooltipViewModel()
        super().__init__(settings)

    @property
    def view_model(self) -> entry_point_not_active_tooltip_view_model.EntryPointNotActiveTooltipViewModel:
        return super().getViewModel()

