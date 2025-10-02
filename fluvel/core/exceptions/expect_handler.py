import sys, logging
from typing import TypedDict, Unpack

# Exceptions
from fluvel.core.exceptions.exceptions import ContentNotFoundError, ContentLoadingError

class ExpectKwargs(TypedDict, total=False):
    msg: str
    default_value: any
    stop: bool

class expect:
    """
    Clase de utilidad que agrupa decoradores para el manejo de excepciones.
    """

    @classmethod
    def Handle(
        cls,
        function: callable,
        exception: Exception,
        args: tuple,
        kwargs: dict[str, any],
        msg: str = None,
        default_value: any = None,
        stop: bool = True
    ):
        try:
            return function(*args, **kwargs)
        except exception as e:

            msg = msg.replace("$e", str(e)) if msg else f"{type(e).__name__}: {e}"

            logging.error(msg)

            if stop:
                sys.exit(1)
            
            return default_value

    @classmethod
    def _make_handler(cls, exception: Exception, **eparams):
        return lambda function: \
            lambda *args, **kwargs: \
                cls.Handle(
                    function,
                    exception,
                    args,
                    kwargs,
                    **eparams
                )

    @classmethod
    def FileNotFound(cls, **eparams: Unpack[ExpectKwargs]):

        return cls._make_handler(FileNotFoundError, **eparams)
    
    @classmethod
    def ContentNotFound(cls, **eparams: Unpack[ExpectKwargs]):

        return cls._make_handler(ContentNotFoundError, **eparams)
    
    @classmethod
    def ErrorLoadingContent(cls, **eparams: Unpack[ExpectKwargs]):

        return cls._make_handler(ContentLoadingError, **eparams)

    @classmethod
    def ErrorImportingModule(cls, **eparams: Unpack[ExpectKwargs]):

        return cls._make_handler(ImportError, **eparams)
    
    @classmethod
    def RouteNotFound(cls, **eparams: Unpack[ExpectKwargs]):

        return cls._make_handler(ValueError, **eparams)
    
    @classmethod
    def MismatchedKey(cls, **eparams: Unpack[ExpectKwargs]):

        return cls._make_handler(KeyError, **eparams)