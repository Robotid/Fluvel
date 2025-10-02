"""
Este módulo contiene la lógica fundamental de Fluvel para la creación
de Layouts.
classes:
    - LayoutBuilder: es la clase usada como context manager
    - ViewBuilder: es el disparador de LayoutBuilder a través de sus
    métodos y sirve como clase abstracta para la creación de Vistas.
"""

from typing import TypeVar, Generic
from abc import ABC, abstractmethod, ABCMeta

# Fluvel
from fluvel.components.layouts import FormLayout, HBoxLayout, VBoxLayout, GridLayout

# PySide6
from PySide6.QtWidgets import QWidget, QLayout
from PySide6.QtCore import QObject

from fluvel.core.AppWindow import AppWindow

# Definir una variable de tipo para los layouts
TLayout = TypeVar("TLayout", bound=QLayout)

class LayoutBuilder(Generic[TLayout]):
    """
    Context manager para la creación declarativa de layouts de PySide6.

    Esta clase permite a los desarrolladores construir layouts de manera intuitiva
    usando la sintaxis `with`, manejando la adición de layouts a contenedores
    existentes de forma automática.

    :ivar layout: La instancia de un QLayout (e.g. 'HBoxLayout')
    :type layout: TLayout
    """

    def __init__(self, container: QLayout | QWidget, type_layout: type[TLayout]):
        """
        Inicializador de la clase `LayoutBuilder`.

        :param container: El layout o widget al que se agregará el nuevo layout.
        :type container: QLayout | QWidget
        :param type_layout: La clase del layout a instanciar (ej. `HBoxLayout`).
        :type type_layout: type[TLayout]
        """

        # an instance of HBoxLayout, VBoxLayout, GridLayout or StackedLayout
        self.layout: TLayout = type_layout()

        # the container is a layout
        if isinstance(container, QLayout):
            container.addLayout(self.layout)

        # the container is a widget
        elif isinstance(container, QWidget):
            container.setLayout(self.layout)

    def __enter__(self) -> TLayout:
        """
        Método de entrada del context manager.
        
        Devuelve la instancia del layout para que pueda ser utilizada
        dentro del bloque `with`.
        """
        return self.layout

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Método de salida del context manager.
        """
        return False

class VBMeta(type(QObject), ABCMeta):
    """
    Metaclase Unificada que resuelve los conflictos
    entre las clases base QObject y ABCMeta al combinarlas.
    """

    pass

class AbstractView(QObject, ABC, metaclass=VBMeta):
    """
    Clase base abstracta para la creación de Vistas en Fluvel.

    Esta clase proporciona los métodos de ayuda (context managers) para
    la construcción declarativa de layouts, como `Vertical`, `Horizontal`, etc.

    :cvar app_root: La instancia de la clase FluvelApp.
    :type app_root: FluvelApp
    :cvar main_window: La instancia de la clase MainWindow.
    :type main_window: MainWindow
    :ivar _container: El QWidget contenedor de la vista.
    :type _container: QWidget
    """

    _container: QWidget

    def __init__(self, container: QWidget | QLayout | None) -> None:
        """
        Inicializa una instancia de `AbstractView`.

        :param container: El contenedor principal para la vista.
        :type container: QWidget, QLayout o None
        :raises TypeError: Si el contenedor no es un QWidget o QLayout.
        """
        super().__init__()
        self.container = container

    @classmethod
    def _set_globals(cls, app_root, main_window: AppWindow):
        cls.app_root = app_root
        cls.main_window = main_window

    @property
    def container(self) -> QWidget:
        return self._container

    @container.setter
    def container(self, container: QWidget | QLayout | None) -> None:

        if isinstance(container, QWidget):
            self._container = container

        # El padre es un Layout, por lo que se crea
        # un contenedor en blanco QWidget
        elif container is None or isinstance(container, QLayout):
            blank_container = QWidget()
            self._container = blank_container

        else:
            raise TypeError("The container must be a QLayout or a QWidget.")

    def Vertical(self, container: QLayout | QWidget) -> LayoutBuilder[VBoxLayout]:
        """
        Crea un `VBoxLayout` usando un context manager.

        :param container: El contenedor para el layout.
        :type container: QLayout | QWidget
        :returns: Un `LayoutBuilder` para `VBoxLayout`.
        :rtype: LayoutBuilder[VBoxLayout]
        
        Ejemplo:
        --------
        .. code-block:: python
            ...
            with self.Vertical(container) as v:
                v.Label(text="Hello")
        """
        return LayoutBuilder(container, VBoxLayout)

    def Horizontal(self, container: QLayout | QWidget) -> LayoutBuilder[HBoxLayout]:
        """
        Crea un `HBoxLayout` usando un context manager.

        :param container: El contenedor para el layout.
        :type container: QLayout | QWidget
        :returns: Un `LayoutBuilder` para `HBoxLayout`.
        :rtype: LayoutBuilder[HBoxLayout]
        
        Ejemplo:
        --------
        .. code-block:: python
            ...
            with self.Horizontal(container) as h:
                h.Label(text="Hello")
        """
        return LayoutBuilder(container, HBoxLayout)

    def Form(self, container: QLayout | QWidget) -> LayoutBuilder[FormLayout]:
        return LayoutBuilder(container, FormLayout)

    def Grid(self, container: QLayout | QWidget) -> LayoutBuilder[GridLayout]:
        return LayoutBuilder(container, GridLayout)

    def Stacked(self, container: QLayout | QWidget): ...

    @abstractmethod
    def build_ui(self) -> None:
        """
        Método abstracto para construir la interfaz de usuario.
        
        Este método debe ser implementado por las clases que heredan de `AbstractView`
        y es donde se definirá toda la lógica de la UI.
        """
        pass

class View(AbstractView):
    pass

class Template(AbstractView):
    pass