# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AnimatedBackgroundScreenMeta.py

# Import the BaseDAAPIComponent class from the gui.Scaleform.framework.entities package
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

# Define the AnimatedBackgroundScreenMeta class, which inherits from BaseDAAPIComponent
class AnimatedBackgroundScreenMeta(BaseDAAPIComponent):

    # Define the as_setImageDataS method, which takes three parameters:
    # backgroundImgPath: A string representing the path to the background image
    # fogImgPath: A string representing the path to the fog image
    # animate: A boolean indicating whether or not to animate the background
    def as_setImageDataS(self, backgroundImgPath, fogImgPath, animate):
        # If the DAAPI is initialized, call the as_setImageData method on the flashObject with the provided parameters
        return self.flashObject.as_setImageData(backgroundImgPath, fogImgPath, animate) if self._isDAAPIInited() else None

