# Fluvel 🚀

**Fluvel is a Python framework designed to simplify and accelerate the creation of elegant Graphical User Interfaces (GUIs). It's built on top of PySide6, leveraging the robust capabilities of the Qt framework to provide a more intuitive and declarative development experience.**

![Fluvel Demo - Placeholder Image](assets/fluvel_demo.png)
*(Reemplaza esta imagen con una captura de pantalla o GIF de tu aplicación de ejemplo o de un menú generado por Fluvel)*

## ✨ Características Principales

Fluvel se enfoca en hacer el desarrollo de GUIs en PySide6 más eficiente y disfrutable, ofreciendo:

* **Menús Dinámicos con FLUML:** Define la estructura de tus menús de forma declarativa y legible usando un Lenguaje de Dominio Específico (DSL) llamado FLUML. Olvídate del código repetitivo para construir menús complejos.
* **Temas Personalizables al Instante:** Cambia la apariencia completa de tu aplicación en tiempo real con solo unas líneas de código, utilizando Hojas de Estilo Qt (QSS) que puedes definir y cargar dinámicamente.
* **Arquitectura Modular (MVC Inspirada):** Fomenta una clara separación de responsabilidades para un código más limpio, mantenible y escalable, inspirado en los principios del patrón Modelo-Vista-Controlador.
* **Preparado para la Escalabilidad:** Diseñado desde cero para manejar proyectos desde pequeñas utilidades hasta aplicaciones complejas, facilitando la adición de nuevas funcionalidades sin romper la estructura.
* **Productividad Mejorada:** Reduce la cantidad de código boilerplate que necesitas escribir, permitiéndote centrarte en la lógica de tu aplicación.

## 🚀 Empezando

### Requisitos

* Python 3.9+
* PySide6

### Instalación

Dado que Fluvel es tu proyecto, puedes explicar cómo otros podrían instalarlo si lo haces público. Por ahora, asumiendo que es un desarrollo local:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/fluvel.git](https://github.com/tu-usuario/fluvel.git)
    cd fluvel
    ```
2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate # En Linux/macOS
    # venv\Scripts\activate # En Windows
    ```
3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Asegúrate de tener un archivo `requirements.txt` en la raíz de tu proyecto con `PySide6` y cualquier otra dependencia)*

### Uso Básico

Aquí un ejemplo de cómo crear una aplicación simple con Fluvel.

Primero, crea tu archivo de configuración de menú `views/menus/main_menu.fluml`:

```fluml
# views/menus/main_menu.fluml

# Main menu sections
[File]:
    new_file = "New File"
    save = "Save"
    ---
    quit = "Quit"

[Help]:
    about_app = "About Fluvel"