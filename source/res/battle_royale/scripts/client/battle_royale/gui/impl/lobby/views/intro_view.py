# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/intro_view.py

# Import necessary modules and classes
from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.common.battle_royale.br_helpers import currentHangarIsBattleRoyale
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_pass.battle_pass_intro_view_model import BattlePassIntroViewModel
from gui.impl.gen.view_models.views.lobby.common.intro_slide_model import IntroSlideModel
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared.event_dispatcher import showBrowserOverlayView
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IBattleRoyaleController, IHangarSpaceSwitchController
from gui.shared import g_eventBus, EVENT_BUS_SCOPE

# Define the IntroView class, which inherits from ViewImpl and IGlobalListener
class IntroView(ViewImpl, IGlobalListener):
    
    # Inject required dependencies
    __settingsCore = dependency.descriptor(ISettingsCore)
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)
    __spaceSwitchController = dependency.descriptor(IHangarSpaceSwitchController)

    # Initialize the class
    def __init__(self):
        # Initialize ViewSettings with the view's attributes
        settings = ViewSettings(R.views.battle_royale.lobby.views.IntroView())
        settings.flags = ViewFlags.LOBBY_SUB_VIEW
        settings.model = BattlePassIntroViewModel()
        
        # Get the intro video URL and set a flag for page showing status
        self.__urlIntroVideo = self.__battleRoyaleController.getIntroVideoURL()
        self.__isPageWasShow = False
        
        # Initialize the superclass with the settings
        super(IntroView, self).__init__(settings)

    # Property to access the viewModel
    @property
    def viewModel(self):
        return super(IntroView, self).getViewModel()

    # Method to handle PRB entity switching
    def onPrbEntitySwitched(self):
        if not self.__battleRoyaleController.isBattleRoyaleMode():
            self.destroyWindow()

    # Override the _onLoading method
    def _onLoading(self, *args, **kwargs):
        # Call the superclass method
        super(IntroView, self)._onLoading(*args, **kwargs)
        
        # Subscribe to viewModel events
        self.viewModel.onClose += self.__onClose
        self.viewModel.onVideo += self.__onVideo
        
        # Register for the LOBBY ViewEventType
        g_eventBus.addListener(ViewEventType.LOAD_VIEW, self.__handleLoadView, scope=EVENT_BUS_SCOPE.LOBBY)
        
        # If the current hangar is Battle Royale, initialize the viewModel
        if currentHangarIsBattleRoyale():
            self.__onSpaceUpdated()
        else:
            # Otherwise, listen for space updates
            self.__spaceSwitchController.onSpaceUpdated += self.__onSpaceUpdated
        
        # Start global listening
        self.startGlobalListening()
        
        # Update the viewModel
        self.__updateViewModel()

    # Override the _finalize method
    def _finalize(self):
        # Unsubscribe from viewModel events
        self.viewModel.onClose -= self.__onClose
        self.viewModel.onVideo -= self.__onVideo
        
        # Unregister for the LOBBY ViewEventType
        g_eventBus.removeListener(ViewEventType.LOAD_VIEW, self.__handleLoadView, scope=EVENT_BUS_SCOPE.LOBBY)
        
        # Stop global listening
        self.stopGlobalListening()
        
        # Call the superclass method
        super(IntroView, self)._finalize()

    # Method to handle the LOAD_VIEW event
    def __handleLoadView(self, event):
        if event.alias == VIEW_ALIAS.LOBBY_HANGAR:
            self.__onClose()

    # Method to handle viewModel.onClose
    def __onClose(self):
        self.destroyWindow()

    # Method to handle viewModel.onVideo
    def __onVideo(self):
        # Show the intro video in a browser overlay
        showBrowserOverlayView(self.__urlIntroVideo, VIEW_ALIAS.BROWSER_OVERLAY)

    # Method to handle space updates
    def __onSpaceUpdated(self):
        if not self.__isPageWasShow:
            self.__isPageWasShow = True
            self.__onVideo()
        else:
            self.__onClose()

    # Method to update the viewModel
    def __updateViewModel(self):
        # Get texts and images from R.strings and R.images
        texts = R.strings.battle_royale.intro
        images = R.images.battle_royale.gui.maps.intro
        
        # Transact on the viewModel
        with self.viewModel.transaction() as tx:
            tx.setTitle(texts.title())
            tx.setAbout(texts.aboutButton())
            tx.setButtonLabel(texts.button())
            
            # Create and add IntroSlideModel instances to the slides list
            slides = tx.getSlides()
            slides.addViewModel(self
