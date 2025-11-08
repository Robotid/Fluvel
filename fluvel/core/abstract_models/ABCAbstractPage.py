"""
This module contains the fundamental logic for creating declarative layouts in Fluvel.

It defines the core abstract class for all views and the context manager 
responsible for building nested PySide6 layouts.
"""

from abc import ABC, abstractmethod, ABCMeta

# Fluvel
from fluvel.components.widgets.FContainer import FContainer
from fluvel.core.AppWindow import AppWindow
from fluvel.core.abstract_models.Builder import Builder

# PySide6
from PySide6.QtCore import QObject

class VBMeta(type(QObject), ABCMeta):
    """
    Unified Metaclass that resolves conflicts when combining 
    :py:class:`PySide6.QtCore.QObject` and :py:class:`abc.ABCMeta`.

    All :py:class:`~fluvel.core.abstract_models.ABCAbstractPage.AbstractPage` subclasses inherit from this metaclass to ensure 
    compatibility with both PySide6's signal/slot system and Python's abstract base classes.
    """
    pass

class AbstractPage(FContainer, ABC, metaclass=VBMeta):
    """
    Abstract base class for creating Views (pages) in Fluvel.

    This class provides the core declarative helper methods (context managers) 
    for UI construction, such as :py:meth:`Vertical`, :py:meth:`Horizontal`, etc.

    All application views must inherit from :py:class:`~fluvel.core.abstract_models.ABCAbstractPage.AbstractPage` and implement
    the :py:meth:`build_ui` method.

    :cvar app_root: The instance of the main application class (:py:class:`~fluvel.core.FluvelApp.FluvelApp`).
    :cvar main_window: The instance of the main window container (:py:class:`~fluvel.core.AppWindow.AppWindow`).
    """

    def __init__(self) -> None:
        """
        Initializes an instance of :py:class:`~fluvel.core.abstract_models.ABCAbstractPage.AbstractPage`.
        """
        super().__init__()
        

    @classmethod
    def _set_globals(cls, app_root, main_window: AppWindow):
        """
        Sets global references to the application root and main window.

        This is called internally by :py:class:`~fluvel.core.Router.Router.init`.

        :param app_root: The root application instance.
        :type app_root: :py:class:`~fluvel.core.App.FluvelApp`
        :param main_window: The main application window instance.
        :type main_window: :py:class:`~fluvel.core.AppWindow.AppWindow`
        :rtype: None
        """
        # The FluvelApp instance
        cls.app_root = app_root

        # The MainWindow instance
        cls.main_window = main_window

    @abstractmethod
    def build_ui(self) -> None:
        """
        Abstract method for building the user interface.
        
        This method **must** be implemented by all classes inheriting from 
        :py:class:`~fluvel.core.abstract_models.ABCAbstractPage.AbstractPage` and is where the entire UI construction logic resides.
        :rtype: None
        """
        pass


class Page(AbstractPage, Builder):
    """
    Concrete class that inherits from :py:class:`~fluvel.core.abstract_models.ABCAbstractPage.AbstractPage`
    used for user interface composition via context handlers.   
    """
    pass