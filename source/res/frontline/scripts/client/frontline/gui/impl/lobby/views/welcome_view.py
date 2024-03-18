# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: frontline/scripts/client/frontline/gui/impl/lobby/views/welcome_view.py

# Import necessary modules and dependencies
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from gui.impl.pub import ViewImpl, WindowImpl
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController
from frontline.gui.impl.gen.view_models.views.lobby.views.welcome_view_model import WelcomeViewModel

# Define the WelcomeView class
class WelcomeView(ViewImpl):
    # Inject the IEpicBattleMetaGameController dependency
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)

    def __init__(self):
        # Initialize the ViewImpl class with the given settings
        settings = ViewSettings(R.views.frontline.lobby.WelcomeView(), ViewFlags.VIEW, WelcomeViewModel())
        super(WelcomeView, self).__init__(settings)

    @property
    def viewModel(self):
        # Return the viewModel instance
        return super(WelcomeView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        # Call the parent class's _onLoading method
        super(WelcomeView, self)._onLoading(*args, **kwargs)
        # Begin a transaction on the viewModel
        with self.viewModel.transaction() as vm:
            # Call the private method __updateVehiclesSlide with the vehiclesSlide viewModel as an argument
            self.__updateVehiclesSlide(vm.vehiclesSlide)

    def _getEvents(self):
        # Return a tuple of event handlers
        return ((self.viewModel.onClose, self.__onViewClose),)

    def __onViewClose(self):
        # Call the destroyWindow method
        self.destroyWindow()

    def __updateVehiclesSlide(self, vehicleSlideModel):
        # Get the valid vehicle levels from the epicController
        validVehicleLevels = self.__epicController.getValidVehicleLevels()
        # Sort the valid vehicle levels
        validVehicleLevels.sort()
        # Set the fromLevel and toLevel properties of the vehiclesSlide viewModel
        vehicleSlideModel.setFromLevel(validVehicleLevels[0])
        vehicleSlideModel.setToLevel(validVehicleLevels[-1])

# Define the WelcomeViewWindow class
class WelcomeViewWindow(WindowImpl):

    def __init__(self):
        # Initialize the WindowImpl class with the given flags, layer, and content
        super(WelcomeViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSC
