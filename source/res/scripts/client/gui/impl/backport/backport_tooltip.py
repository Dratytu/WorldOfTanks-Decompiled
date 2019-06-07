# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/impl/backport/backport_tooltip.py
from collections import namedtuple
from frameworks.wulf import ViewFlags, ViewModel, Window, WindowFlags
from gui.impl.pub import ViewImpl, WindowImpl
from gui.impl.pub.window_view import WindowView
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
_STATE_TYPE_INFO = 'INFO'
TooltipData = namedtuple('TooltipData', ('tooltip', 'isSpecial', 'specialAlias', 'specialArgs'))

def createTooltipData(tooltip=None, isSpecial=False, specialAlias=None, specialArgs=None):
    return TooltipData(tooltip, isSpecial, specialAlias, specialArgs)


class _BackportTooltipContent(ViewImpl):
    appLoader = dependency.descriptor(IAppLoader)
    __slots__ = ()

    def __init__(self, tooltipData):
        super(_BackportTooltipContent, self).__init__(R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent(), ViewFlags.VIEW, ViewModel, tooltipData)

    def _initialize(self, tooltipData):
        super(_BackportTooltipContent, self)._initialize()
        toolTipMgr = self.appLoader.getApp().getToolTipMgr()
        if toolTipMgr is not None:
            if tooltipData.isSpecial:
                toolTipMgr.onCreateTypedTooltip(tooltipData.specialAlias, tooltipData.specialArgs, _STATE_TYPE_INFO)
            else:
                toolTipMgr.onCreateComplexTooltip(tooltipData.tooltip, _STATE_TYPE_INFO)
        return

    def _finalize(self):
        toolTipMgr = self.appLoader.getApp().getToolTipMgr()
        if toolTipMgr is not None:
            toolTipMgr.hide()
        return


class BackportTooltipWindow(Window):
    __slots__ = ()

    def __init__(self, tooltipData, parent):
        super(BackportTooltipWindow, self).__init__(wndFlags=WindowFlags.TOOLTIP, decorator=None, content=_BackportTooltipContent(tooltipData), parent=parent)
        return


class DecoratedTooltipWindow(WindowImpl):
    __slots__ = ()

    def __init__(self, content, parent):
        super(DecoratedTooltipWindow, self).__init__(wndFlags=WindowFlags.TOOLTIP, decorator=WindowView(layoutID=R.views.common.tooltip_window.tooltip_window.TooltipWindow()), content=content, parent=parent, areaID=R.areas.specific())