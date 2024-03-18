# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/frameworks/wulf/__init__.py

# wulf framework initialization file
# This script imports various modules and classes that define the core functionality
# of the wulf framework, a graphical user interface (GUI) framework for a specific application.

from .gui_application import GuiApplication  # The main application class for the GUI framework

# Constants used throughout the framework to define various properties and flags
from .gui_constants import (PropertyType, PositionAnchor, ViewFlags, ViewStatus,
                            ViewEventType, WindowFlags, WindowLayer, WindowStatus,
                            NumberFormatType, RealFormatType, TimeFormatType,
                            DateFormatType, CaseType)

# Functions for working with translated text, formatting, and case mapping
from .py_object_wrappers import (isTranslatedKeyValid, isTranslatedTextExisted,
                                  getTranslatedText, getTranslatedPluralText,
                                  getImagePath, getSoundEffectId, getLayoutPath,
                                  getTranslatedTextByResId,
                                  getTranslatedPluralTextByResId, getTranslatedKey,
                                  getNumberFormat, getRealFormat, getTimeFormat,
                                  getDateFormat, caseMap)

# Various classes defining different aspects of the GUI framework
from .view.array import Array  # A class for working with arrays in views
from .view.command import Command  # A class for defining commands in views
from .view.view import ViewSettings  # Settings for configuring a view
from .view.view import View  # A base class for creating views in the framework
from .view.view_event import ViewEvent  # A class for handling events in views

from .windows_system.windows_area import WindowsArea  # A class for managing windows areas
from .windows_system.window import WindowSettings  # Settings for configuring a window
from .windows_system.window import Window  # A base class for creating windows in the framework

# A class for creating view models in the framework
from .view.view_model import ViewModel

__all__ = (    'GuiApplication', 'PropertyType', 'PositionAnchor', 'ViewFlags', 'ViewStatus', 'ViewEventType', 'WindowFlags',
