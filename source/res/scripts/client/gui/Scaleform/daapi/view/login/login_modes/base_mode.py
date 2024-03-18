# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/login/login_modes/base_mode.py

# Import necessary modules and helpers
import weakref
from helpers import dependency
from skeletons.gui.login_manager import ILoginManager

# Define a class constant for invalid fields
class INVALID_FIELDS(object):
    ALL_VALID = 0
    LOGIN_INVALID = 1
    PWD_INVALID = 2
    SERVER_INVALID = 4
    LOGIN_PWD_INVALID = LOGIN_INVALID | PWD_INVALID

