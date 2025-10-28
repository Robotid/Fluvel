from fluvel.composer import Factory
import qtawesome as qta

@Factory.compose("FButton")
def CloseIcon(color: str, on_click: callable):

    return {
        "icon": qta.icon("fa5s.times", color=f"{color}", options=[{"scale_factor": 1.0}]),
        "on_click": on_click,
        "style": "b[none]"
    }