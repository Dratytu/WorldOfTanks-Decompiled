# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/impl/lobby/feature/tooltips/entry_point_before_progression_tooltip_view.py
from frameworks.wulf import ViewSettings
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.tooltips.entry_point_before_progression_tooltip_view_model import EntryPointBeforeProgressionTooltipViewModel
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IArmoryYardController

class EntryPointBeforeProgressionTooltipView(ViewImpl):
    """
    View for displaying tooltip information about an entry point before progression.
    """
    __slots__ = ()

    def __init__(self):
        """
        Initialize the view with settings and a view model.
        """
        settings = ViewSettings(R.views.armory_yard.lobby.feature.tooltips.EntryPointBeforeProgressionTooltipView())
        settings.model = EntryPointBeforeProgressionTooltipViewModel()
        super(EntryPointBeforeProgressionTooltipView, self).__init__(settings)

    @property
    def view_model(self):
        """
        Property for getting the view model.
        """
        return super(EntryPointBeforeProgressionTooltipView, self).get_view_model()

    def _on_loading(self, *args, **kwargs):
        """
        Called when the view is loaded.
        """
        super(EntryPointBeforeProgressionTooltipView, self)._on_loading(*args, **kwargs)
        if not self.__armory_yard_ctrl.is_enabled():
            return
        with self.view_model.transaction() as tx:
            start_progression_time, _ = self.__armory_yard_ctrl.get_progression_times()
            tx.set_start_timestamp(start_progression_time)

    @property
    def __armory_yard_ctrl(self):
        """
        Property for getting the armory yard controller.
        """
        return dependency.descriptor(IArmoryYardController)  # type: IArmoryYardController

