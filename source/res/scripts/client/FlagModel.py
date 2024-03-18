# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/FlagModel.py

# Import necessary modules
from collections import namedtuple
from Math import Matrix
import BigWorld
import AnimationSequence

# Define a named tuple for FlagSettings
FlagSettings = namedtuple('FlagSettings', ['flagCompounModel',  # The compound model for the flag
                                            'flagAlias',          # The alias for the flag
                                            'flagAnim',           # The animation for the flag
                                            'flagBackgroundTex',  # The background texture for the flag
                                            'flagEmblemTex',      # The emblem texture for the flag
                                            'flagEmblemTexCoords', # The emblem texture coordinates for the flag
                                            'spaceID'])            # The space ID for the flag

# Define the FlagModel class
class FlagModel(object):
    # Define a property for the model
    @property
    def model(self):
        return self.__flagCompoundModel

    # Initialize the FlagModel class
    def __init__(self):
        # Initialize instance variables
        self.__flagCompoundModel = None
        self.__flagStaffFashion = None
        self.__flagFashion = None
        self.__flagAnimator = None
        self.__spaceID = None
        return

    # Define a method to set up the flag
    def setupFlag(self, position, flagSettings, color):
        # Set the space ID and flag compound model
        self.__spaceID = flagSettings.spaceID
        self.__flagCompoundModel = flagSettings.flagCompounModel
        self.__flagCompoundModel.position = position

        # Create a WGAlphaFadeCompoundFashion for the flag staff
        self.__flagStaffFashion = BigWorld.WGAlphaFadeCompoundFashion()

        # Create a WGFlagAlphaFadeFashion for the flag
        self.__flagFashion = BigWorld.WGFlagAlphaFadeFashion()

        # Set the color, background texture, and emblem texture for the flag
        self.__flagFashion.setColor(color)
        self.__flagFashion.setFlagBackgroundTexture(flagSettings.flagBackgroundTex)
        self.__flagFashion.setEmblemTexture(flagSettings.flagEmblemTex, flagSettings.flagEmblemTexCoords)

        # Create a translation matrix and override the position for the flag
        translationMatrix = Matrix()
        translationMatrix.setTranslate(position)
        self.__flagFashion.overridePosition(translationMatrix)

        # Set up the fashions for the flag compound model
        self.__flagCompoundModel.setupFashions((self.__flagStaffFashion, self.__flagFashion))

        # Set the flag animator
        self.__flagAnimator = flagSettings.flagAnim

        # If the flag animator is not None, bind it to the flag compound model
        if self.__flagAnimator is not None:
            self.__flagAnimator.bindTo(AnimationSequence.PartWrapperContainer(self.__flagCompoundModel, self.__spaceID, flagSettings.flagAlias))

        return

    # Define a method to change the flag color
    def changeFlagColor(self, color):
        # If the flag fashion exists, set its color
        if self.__flagFashion:
            self
