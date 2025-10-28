from fluvel.composer import Prefab, Canvas

from ui.components.IconButton import IconButton

@Prefab
def RowOfIcons(canvas: Canvas):

    icons = [
        ("b", "google"),
        ("b", "facebook-f"),
        ("b", "github"),
        ("b", "linkedin-in"),
    ]
    
    with canvas.Horizontal() as h:
        h.adjust(alignment="center")

        for _type, name in icons:
            
            h.add_widget(IconButton(_type, name))
            
    return canvas