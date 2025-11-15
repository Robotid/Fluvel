from typing import Dict, Any, TypedDict, Unpack, List, Callable, Pattern
import re

# PySide6
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal

# Exceptions
from fluvel.core.exceptions.state_manager import SilkBindingError, SilkStateError

class CreateStateKwargs(TypedDict):
    group           : str
    alias           : str
    description     : str

class StateGroup(QObject):
    """
    Represents a reactive state container (store) in the MVVM pattern.

    Inherits from :py:class:`PySide6.QtCore.QObject` to leverage the signal system
    and enable communication between the data model (state) and the view (widgets).

    It manages three types of data:
    1. **Definitions (:py:attr:`_definitions`):** The base state (mutable values).
    2. **Computed Properties (:py:attr:`_computed_funcs`):** Values derived from definitions, which are updated automatically.
    3. **Subscriptions (:py:attr:`_subscriptions`):** Callback functions that are executed when a state changes.

    :ivar state_changed: Signal emitted with the key of the state that has changed.
    :vartype state_changed: :py:class:`PySide6.QtCore.Signal`
    """

    state_changed   : Signal = Signal(str)

    def __init__(self, group_name: str, alias: str, description: str):
        """
        Initializes a new instance of StateGroup.

        :param group_name: Full name of the state group (e.g., 'HomeState').
        :type group_name: str
        :param alias: Unique, short alias to reference the group in bindings (e.g., “vm”).
        :type alias: str
        :param description: Brief description of the purpose of the state group.
        :type description: str
        """

        super().__init__()
        
        # StateGroup Data
        self.group_name = group_name
        self.alias = alias
        self.description = description

        # State Maps
        self._definitions       : Dict[str, Any] = {}
        self._computed_funcs    : Dict[str, Dict[str, List, Any]] = {} # Se almacena la lógica (dependencias y funciones)
        self._computed_cache    : Dict[str, Any] = {} # Se guardan los valores computados/calculados
        self._subscriptions     : Dict[str, Any] = {}

    def get(self, key: str) -> Any:
        """
        Gets the value of a state key.

        Prioritizes returning the cached value of a computed property
        over the base value of a definition.

        :param key: The key of the state to get.
        :type key: str
        :returns: The current value of the state or computed property.
        :rtype: Any
        """

        if key in self._computed_cache:
            return self._computed_cache[key]

        return self._definitions.get(key)

    def set(self, name: str, value: any) -> None:
        """
        Sets a new value for a defined state and notifies subscribers.

        If the value is different from the current value, it updates the definition,
        emits the :py:attr:`state_changed` signal (which triggers the recalculation
        of computed properties), and executes all subscribed *callbacks*.

        :param name: The name of the state key to modify.
        :type name: str
        :param value: The new value to assign to the key.
        :type value: any
        :rtype: None
        """

        old_value = self._definitions.get(name)

        if old_value != value:
            
            # Actualizando la definición
            self._definitions[name] = value

            # Luego emitir la señal para que las
            # propiedades computadas puedan actualizarse
            self.state_changed.emit(name)

            # Finalmente, Ejecutar cada callback suscrito
            # Esto debe ejecutarse después de que el estado ha cambiado.
            if name in self._subscriptions:

                # Obteniendo el nuevo valor del estado (ya cambiado)
                new_value = value
                
                # Ejecutar cada callback suscrito
                for callback in self._subscriptions[name]:
                    
                    # La callback recibe la nueva y antigua clave como argumentos
                    callback(new_value, old_value)

    def define(self, **definitions):
        """
        Defines the initial and base state of the group.

        This method is typically used only once during the configuration of the
        state group to set the initial mutable values.

        :param definitions: A dictionary of keyword arguments where the key is the
                            name of the state and the value is its initial value.
        :type definitions: Any
        :rtype: None
        """
        
        # Mapeamos las Definiciones (ej. username="")
        self._definitions = definitions

    def computed(self, key: str, dependencies: List[str], func: Callable):
        """
        Defines a computed property whose value is derived from other defined states.

        The *func* function is automatically executed when any of its
        :py:attr:`dependencies` change. The result is stored in the cache
        and the key is emitted as a state change if the computed value differs
        from the previous one.

        :param key: The name of the computed property (cannot be a defined state).
        :type key: str

        :param dependencies: A list of state keys on which this property depends.
                            The values of these keys are passed as positional arguments to *func*.
        :type dependencies: List[str]
        
        :param func: The function that computes the value of the property. It must accept as many
                    arguments as it has dependencies.
        :type func: :py:class:`~typing.Callable`

        :raises SilkStateError: If the key is already defined in the base state (:py:meth:`define`).
        :rtype: None
        """

        # The key is already in use,
        # so a SilkStateError is thrown
        if key in self._definitions:
            raise SilkStateError(f"Computed key '{key}' cannot be defined because it already exists in _definitions.")
        
        # Guardar la función y dependencias
        self._computed_funcs[key] = {
            'deps': dependencies,
            'func': func 
        }
        
        def recalculate_and_emit(changed_attr: str) -> None:
            """Recalculate the property if the attribute that changed is in its dependencies.”"""
            
            # Solo recalcular si la clave que cambió es una dependencia
            if changed_attr in dependencies:
                
                # Obtener los valores actuales de las dependencias
                dep_values = [self.get(dep_key) for dep_key in dependencies]
                
                # Ejecutar la función de cálculo
                # Pasándole como argumentos los valores de las dependencias
                new_value = func(*dep_values)
                
                # Si el valor ha cambiado, actualizar el caché y emitir la señal
                if self._computed_cache.get(key) != new_value:
                    
                    # Actualizar el caché con el nuevo valor
                    self._computed_cache[key] = new_value
                    
                    # Emitir la señal para que los componentes dependientes
                    # se actualicen
                    self.state_changed.emit(key)
        
        # Conectando la función a state_changed
        self.state_changed.connect(recalculate_and_emit)
        
        # Establecer el valor inicial (ejecutar la función por primera vez)
        recalculate_and_emit(dependencies[0])

    def subscribe(self, key: str, callback: Callable):
        """
        Subscribe a callback function to be executed when a state changes.

        The callback must accept two arguments: the new value and the old value.

        :param key: The state or computed property key to subscribe to.
        :type key: str
        :param callback: The function to execute. Receives (new_value, old_value).
        :type callback: :py:class:`~typing.Callable`

        :raises SilkStateError: If the key is not defined in :py:meth:`define` or :py:meth:`computed`.
        :rtype: None
        """

        if key not in self._definitions and key not in self._computed_funcs:
            raise SilkStateError(f"Cannot subscribe to key '{key}'. Key must be defined with st.define() or st.computed().")
        
        if key not in self._subscriptions:
            self._subscriptions[key] = []
        
        # Guardamos la función callback
        self._subscriptions[key].append(callback)

    def has_key(self, key: str) -> bool:
        """
        Checks whether a key exists as a definition, computed property, or subscription.

        :param key: The key to search for.
        :type key: str
        :returns: :py:obj:`True` if the key is registered in any of the state structures, otherwise :py:obj:`False`.
        :rtype: bool
        """

        hasKey: bool = True if key in self._definitions \
                                or key in self._computed_funcs \
                                or key in self._subscriptions \
                                else False
        
        return hasKey

class State:
    """
    Static utility class that manages the creation and binding
    of all :py:class:`StateGroup` in the application.
    
    It is the entry point for Silk's reactive state system.
    """

    BIND_REGEX: Pattern[str] = re.compile(r"""
        ^                            # Starts at the beginning of the string
        (?P<property>[\w]*)          # The property name of the widget (e.g., "text", "value")
        :?                           # Optional colon separator
        (?P<signal>[\w]*)            # The signal name of the widget (e.g., "textChanged", "rangeChanged")
        :?                           # Optional colon separator
        @(?P<alias>[\w]+)            # The alias of the StateGroup (e.g., "vm", "h", "global")
        \.                           # Separator dot
        (?P<key>[\w]+)               # The key name within the StateGroup (e.g., "volume", "username")
        $                            # Ends at the end of the string
    """, re.VERBOSE)
    """
    Regular expression for analyzing Silk *binding* syntax.

    Expected format::
    
        [widget_property][:widget_signal]:@group_alias.status_key

    Examples:
    
    * ``@vm.username`` (Default unidirectional/bidirectional binding. Depends on the SKWidget)
    * ``text:@vm.username`` (Explicit unidirectional binding)
    * ``text:textChanged:@vm.username`` (Bidirectional binding)

    :type: :py:class:`~typing.Pattern`
    """

    _groups: Dict[str, StateGroup] = {}

    @classmethod
    def create(cls, **kwargs: Unpack[CreateStateKwargs]):
        """
        Class decorator used to create and register a new :py:class:`StateGroup`.

        This method should be used as a decorator for a function that, in turn, defines
        the initial states (:py:meth:`StateGroup.define`) and computed states
        (:py:meth:`StateGroup.computed`) of the group.

        :param group: The full name of the state group.
        :type group: str
        :param alias: The short, unique alias for referencing the group in the *binding*.
                      If not provided, the value of *group* is used.
        :type alias: str
        :param description: Short description of the group.
        :type description: str
        
        :returns: A decorator that accepts the state configuration function.
        :rtype: :py:class:`~typing.Callable`

        :raises AssertionError: If the ``group`` parameter is not specified.

        Example
        -------
        .. code-block:: py

            @State.create(group=“LoginViewModel”, alias="vm")
            def login_state(st: StateGroup):
            
                st.define(
                    username="user123",
                    password=""
                )

                st.computed(
                    key='isValid',
                    dependencies=['username', 'password'],
                    func=lambda user, pwd: len(user) > 3 and len(pwd) > 5 
                )
        """
        
        # StateGroup Name
        group_name: str = kwargs.get("group", None)

        # The parameter 'group' is required
        assert group_name is not None, "The 'group' parameter must be specified when creating a new StateGroup"

        # StateGroup Alias
        alias: str = kwargs.get("alias", group_name)

        # StateGroup Description
        description: str = kwargs.get("description", "No Description")

        # Create StateGroup object
        state_group_instance = StateGroup(group_name, alias, description)

        # Saving reference to the StateGroup
        cls._groups[alias] = state_group_instance

        # Decorator
        def decorator(func: Callable) -> None:
            
            # Ejecutamos la función que decora State.create
            # Para poder procesar el estado
            func(state_group_instance)

            # La función decorada es manejada por la clase State,
            # por lo que no es necesario su Retorno ni ejecución posterior a 
            # su definición
            return None
    
        return decorator
    
    @classmethod
    def show_groups(cls):
        """
        Prints a summary of all registered status groups
        and their contents (definitions, computed cache, and subscriptions) to the console.

        Main utility for debugging.
        """
        
        for i, group in enumerate(cls._groups.values()):

            print(f"Group {i}: {group.group_name}")
            print(f"Alias: {group.alias}")
            print(f"Description: {group.description}")

            print(f"\tdefinitions: {group._definitions}")
            print(f"\tcomputed: {group._computed_cache}")
            print(f"\tsubscriptions: {group._subscriptions}")

            print("-"*30)

    @classmethod
    def bind(cls, widget: QWidget, bind_string: str) -> None:
        """
        Establishes the data binding between a widget property and a state.

        This is the central method that implements two-way and one-way reactivity.
        It analyzes the binding string and configures the signal connections.

        :param widget: The PySide6 widget instance to bind.
        :type widget: :py:class:`PySide6.QtWidgets.QWidget`
        :param bind_string: The binding string with the format ``[prop][:signal]:@alias.key``.
                :type bind_string: str

        :raises SilkBindingError: If the syntax of the binding string is invalid.
        :raises SilkStateError: If the alias or state key is not found.
        :rtype: None
        """

        _match = re.match(cls.BIND_REGEX, bind_string)

        if not _match:
            raise SilkBindingError(
                f"Invalid binding syntax: '{bind_string}'. "
                "Expected format: 'property:signal:@alias.key'."
                "Ex: '@vm.volume' or 'text:@h.username' or 'value:rangeChanged:@global.theme'."
            )
        
        parsed_binding = _match.groupdict()

        alias = parsed_binding.get("alias")
        key = parsed_binding.get("key")
        
        state_group: StateGroup = cls.get_state_group(bind_string, alias, key)
        
        # Obtenendo la propiedad y señal a vincular del widget 
        prop_from_regex = parsed_binding.get("property")
        signal_from_regex = parsed_binding.get("signal")
        
        # Level 1
        if not prop_from_regex and not signal_from_regex:
            prop_name = widget._BINDABLE_PROPERTY
            signal_name = widget._BINDABLE_SIGNAL
        # Level 2
        elif prop_from_regex and not signal_from_regex:
            prop_name = prop_from_regex
            signal_name = None
        # Level 3
        else:
            prop_name = prop_from_regex
            signal_name = signal_from_regex

        # Implementando los vínculos Unidireccionales y Bidireccionales
        cls.set_unidirectional_binding(widget, state_group, key, prop_name)

        # Implementación del binding bidireccional
        # solo si signal_name es proporcionado
        if signal_name:
            cls.set_bidirectional_binding(widget, state_group, key, signal_name, prop_name)

    @classmethod
    def get_state_group(cls, bind_string: str, alias: str, key: str) -> StateGroup:
        """
        Searches for and validates the existence of the StateGroup and the state key.

        :param bind_string: The original *binding* string (for error messages).
        :type bind_string: str
        :param alias: The alias of the state group.
        :type alias: str
        :param key: The state key within the group.
        :type key: str
        :returns: The instance of :py:class:`StateGroup` found.
        :rtype: :py:class:`StateGroup`

        :raises SilkStateError: If the StateGroup alias or key does not exist.
        """

        if alias not in cls._groups:
            raise SilkStateError(    
                f"StateGroup alias '{alias}' not found for binding '{bind_string}'."
                "Make sure the StateGroup is defined with @State.create."
            )
        
        state_group_instance = cls._groups[alias]

        if not state_group_instance.has_key(key):
            raise SilkStateError(
                f"Key '{key}' not found in StateGroup '{alias}' for binding '{bind_string}'."
                "Make sure the key is defined with st.define() or st.computed()."
            )
        
        return state_group_instance

    @classmethod
    def set_unidirectional_binding(cls, widget: QWidget, state_obj: StateGroup, key: str, prop_name: str) -> None:
        """
        Configure the unidirectional link: **State -> Widget**.

        Ensures that the widget is updated whenever the state key changes
        (either a definition or a computed property).

        :param widget: The widget to update.
        :type widget: :py:class:`PySide6.QtWidgets.QWidget`
        :param state_obj: The state group instance.
        :type state_obj: :py:class:`StateGroup`
        :param key: The state key to link to.
        :type key: str
        :param prop_name: The name of the widget property to set (e.g., ``“text”``).
        :type prop_name: str
        :rtype: None
        """
        
        # El valor inicial de la propiedad se aplica por primera vez de forma inmediata
        # Esto asegura que el widget se sincronice con el estado desde el principio.
        initial_value = state_obj.get(key)
        widget.setProperty(prop_name, initial_value)
        
        # Definimos la función reactiva encargada de actualizar el widget cuando
        # el estado de las 'definitions' o 'computed properties' cambie.
        def update_widget_from_state(changed_attr: str) -> None:

            if changed_attr == key:
                
                # El Nuevo valor de la propiedad 'prop_name' del widget,
                # obtenido mediante StateGroup.get() a través de su 'key'
                new_value = state_obj.get(key)

                # Esto es un mecanismo de control
                # para evitar bucles infinitos
                if widget.property(prop_name) != new_value:

                    # Establishing the new property value
                    widget.setProperty(prop_name, new_value)
        
        # Por último, enlazamos la función reactiva definida arriba
        # a la señal 'state_changed' del StateGroup 'state_obj' para que
        # se ejecute cuando haya un cambio de estado
        state_obj.state_changed.connect(update_widget_from_state)

    @classmethod
    def set_bidirectional_binding(cls, widget: QWidget, state_obj: StateGroup, key: str, signal_name: str, prop_name: str):
        """
        Configure the bidirectional (two-way) link: **Widget -> State**.

        Connect the widget signal (e.g., ``textChanged``) to the method
        :py:meth:`StateGroup.set` so that the state is updated
        when the user interacts with the widget.

        :param widget: The widget that emits the signal.
        :type widget: :py:class:`PySide6.QtWidgets.QWidget`
        :param state_obj: The state group instance.
        :type state_obj: :py:class:`StateGroup`
        :param key: The state key to modify.
        :type key: str
        :param signal_name: The name of the widget's signal (e.g., ``“textChanged”``).
        :type signal_name: str
        :param prop_name: The name of the widget's property (used if the signal does not emit a value).
        :type prop_name: str
        :rtype: None
        """

        if signal_name:
            widget_signal = getattr(widget, signal_name) # widget.textChanged
            
            # Conecta widget.textChanged -> FState.set
            def update_state_from_widget(*args):

                if args:
                    # Si la señal emite un valor
                    widget_value = args[0] 

                else:
                    widget_value = widget.property(prop_name)

                # Lógica para evitar bucles infinitos
                if state_obj.get(key) != widget_value:
                    state_obj.set(key, widget_value)
            
            widget_signal.connect(update_state_from_widget)

    @classmethod
    def get(cls, group_alias: str, state: str) -> Any:
        """
        Convenience access method to obtain a state value
        from anywhere in the application.

        Equivalent to calling ``State.get_state_group(alias).get(state)``.

        :param group_alias: The alias of the state group.
        :type group_alias: str
        :param state: The state key to obtain.
        :type state: str
        :returns: The current value of the state or computed property.
        :rtype: Any

        :raises SilkStateError: If the StateGroup alias is not found.
        """

        group = cls._groups.get(group_alias)

        if not group:
            raise SilkStateError(f"StateGroup alias '{group_alias}' not found.")
            
        return group.get(state)