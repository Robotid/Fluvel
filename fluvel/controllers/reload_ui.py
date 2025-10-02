from fluvel.models.GlobalContent import GlobalContent
from fluvel.controllers.ContentHandler import ContentHandler
from fluvel._user.GlobalConfig import AppConfig
from fluvel.controllers.main_controller import init_content

def reload_ui(window, router):

    # Reiniciar contenido
    GlobalContent.menu_content = {}
    GlobalContent.content_map = {}
    ContentHandler.current_lang = None
    init_content(AppConfig.ui.language)

    # Reiniciar menú y secciones principales
    if hasattr(window, "menu_bar"):
        window.menu_bar.deleteLater()
        window._set_menu_bar()
    
    # Reiniciar Router
    for route in router._routes.values():
        if route.view_instance:
            # Destruimos el widget contenedor de la vista.
            route.view_instance.container.deleteLater()
            # Reseteamos la instancia a None.
            route.view_instance = None

    router.show(router._current_route.name)

    # window.init_ui()