import functools
from typing import TypeVar, Callable, Any

# Fluvel
from fluvel.core.abstract_models.ABCAbstractPage import Page

TFunc = TypeVar('TFunc', bound=Callable[..., Any])

def Prefab(func: TFunc) -> TFunc:
    """
    This pattern encapsulates the design logic and composition of widgets 
    within a function to create a reusable (prefabricated) Complex Component.

    The decorated function should have the following signature:
    `def ComponentName(view: View, **kwargs) -> View:`

    :param func: The function that defines the component's layout and widgets.
    :type func: TFunc
    :returns: The decorated function (`decorator`), which, when called, executes
              the component's logic and returns a constructed `View` ready to be
              added to another layout.
    :rtype: TFunc

    Example:
    --------
    .. code-block:: python

        from fluvel import View
        from fluvel.composer import Prefab

        @Prefab
        def Note(view: View, message: str | list):

            with view.Vertical() as v:
            
                v.Label(text="Note", style="font-bold")
        
                v.Label(text=message, word_wrap=True)

            return view # ¡IMPORTANT!

        # In your views

        class ExampleView(View):

            def build_ui(self):
                
                with self.Vertical() as vbody:
                
                    vbody.Prefab(Note(message="some message"))
    """

    @functools.wraps(func)
    def decorator(*args, **kwargs):
        
        # View with blank_container
        view = Page() 
        
        return func(view, *args, **kwargs)
        
    return decorator