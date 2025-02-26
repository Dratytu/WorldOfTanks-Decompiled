# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: armory_yard/scripts/client/armory_yard/gui/Scaleform/daapi/view/lobby/hangar/armory_yard_entry_point.py
from armory_yard.gui.impl.lobby.feature.armory_yard_entry_point_view import ArmoryYardEntryPointView
from armory_yard.gui.impl.lobby.feature.armory_yard_hangar_widget_view import ArmoryYardWidgetEntryPointView
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from shared_utils import nextTick

class ArmoryYardEntryPoint(InjectComponentAdaptor):

    @nextTick
    def _createInjectView(self, *args):
        super(ArmoryYardEntryPoint, self)._createInjectView(*args)

    def _makeInjectView(self):
        self.__view = ArmoryYardEntryPointView()
        return self.__view


class ArmoryYardEntryPointWidget(InjectComponentAdaptor):

    def _makeInjectView(self):
        self.__view = ArmoryYardWidgetEntryPointView()
        return self.__view
