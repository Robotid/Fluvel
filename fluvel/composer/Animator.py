
from PySide6.QtCore import QPropertyAnimation, QObject, QEasingCurve
from PySide6.QtWidgets import QWidget, QGraphicsOpacityEffect

class Animator:
    
    # Lista para mantener las referencias a las animaciones y efectos
    _active_effects: list[QGraphicsOpacityEffect] = []
    _active_animations: list[QPropertyAnimation] = []

    @classmethod
    def animate(
        cls, 
        target: QObject, 
        property_name: bytes, 
        start_value: float, 
        end_value: float, 
        duration: int = 400, 
        easing: QEasingCurve = QEasingCurve.OutQuad
    ) -> QPropertyAnimation:
        """
        Crea, configura e inicia un QPropertyAnimation para cualquier propiedad.
        """
        animation = QPropertyAnimation(target, property_name)
        animation.setDuration(duration)
        animation.setStartValue(start_value)
        animation.setEndValue(end_value)
        animation.setEasingCurve(easing)
        
        cls._active_animations.append(animation) 
        
        animation.finished.connect(lambda: cls._active_animations.remove(animation))
        
        return animation

    @classmethod
    def fade_in(cls, widget: QWidget, duration: int = 400) -> QPropertyAnimation:
        """
        Aplica un efecto de opacidad y lo anima de 0.0 (invisible) a 1.0 (visible).
        """

        opacity_effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(opacity_effect)
        
        cls._active_effects.append(opacity_effect) 
        
        animation = cls.animate(
            target=opacity_effect, 
            property_name=b"opacity", 
            start_value=0.0, 
            end_value=1.0, 
            duration=duration
        )
    
        animation.finished.connect(lambda: widget.setGraphicsEffect(None))
        animation.finished.connect(lambda: cls._active_effects.remove(opacity_effect))
        
        return animation
    
    @classmethod
    def fade_out(cls, widget: QWidget, duration: int = 400) -> QPropertyAnimation:
        """
        Anima la opacidad de un widget de 1.0 a 0.0 (desvanecerse).
        """
        opacity_effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(opacity_effect)
        
        animation = cls.animate(
            target=opacity_effect, 
            property_name=b"opacity", 
            start_value=1.0, 
            end_value=0.0, 
            duration=duration
        )
        
        # Una vez que la animación termina, ocultamos el widget saliente
        animation.finished.connect(lambda: widget.setHidden(True))
        animation.finished.connect(lambda: widget.setGraphicsEffect(None))
        return animation