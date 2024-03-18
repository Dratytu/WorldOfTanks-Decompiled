# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: fun_random/scripts/client/fun_random/gui/feature/sub_modes/__init__.py

# Importing necessary modules and classes
import typing
from fun_random_common.fun_constants import FunSubModeImpl
from fun_random.gui.feature.sub_modes.base_sub_mode import FunBaseSubMode
from fun_random.gui.feature.sub_modes.dev_sub_mode import FunDevSubMode

# Typing imports for type checking
if typing.TYPE_CHECKING:
    from fun_random.gui.feature.sub_modes.base_sub_mode import IFunSubMode
    from fun_random.helpers.server_settings import FunSubModeConfig

# Mapping of FunSubModeImpl to corresponding sub-mode implementation classes
_SUB_MODE_IMPLS_MAP = {
    FunSubModeImpl.DEV_TEST: FunDevSubMode
}

# Function to create the appropriate sub-mode instance based on the provided settings
def createFunSubMode(subModeSettings):
    # Retrieve the sub-mode implementation class from the mapping using the client's sub-mode impl
    sub_mode_impl = _SUB_MODE_IMPLS_MAP.get(subModeSettings.client.subModeImpl, FunBaseSubMode)
    # Return an instance of the sub-mode implementation class, passing in the sub-mode settings
    return sub_mode_impl(subModeSettings)
