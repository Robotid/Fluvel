![Fluvel's Logo](assets/logo.svg)
# Fluvel
Fluvel es un framework de Python diseñado para simplificar y acelerar la creación de interfaces gráficas de usuario (GUI) elegantes y complejas. Se basa en PySide6 y propone una arquitectura de diseño MVC, por lo que aprovecha las robustas capacidades del framework Qt y la consistencia del patrón MVC para ofrecer una experiencia de desarrollo más intuitiva y declarativa.
También cuenta con DSLs (Domain Specific Languages) propios creados para centralizar, agilizar y simplificar la gestión de Menús y contenido estático de la aplicación.

## Toolkit And Patterns

## Diseño Reactivo Basado en Señales de PySide6

## Diseña las **Vistas** a través de la `clase` `ViewBuilder` 

## Fluvel In Action. Demostrations
### Cómo crear menús a través de archivos `.fluml`
Pequeña demostración construyendo los típicos menús de las aplicaciones usando el lenguaje `fluml`. 
<br>
```
[File]:

    new_text_file = "New Text File"
    new_file = "New File..."

    @SaveAndExportSection
    save = "Save"
    save_as = "Save As..."
    [Export]:
        export = "Export"
        export_as = "Export As..."
    
    @QuitSection
    quit = "Quit"

[Help]:

    about = "About"
    licence = "Licence"

    @MoreSection
    [More]:
        author = "Author"
        version = "Version"
...
```
<!-- ## Reglas sintácticas
| Action | Syntax | Example | Representation |
| --- | --- | --- | --- |
| Inline Comments | `#` | ` # inline-comment` | *an inline comment* |
| Menu or Submenu | `[ ]:` | `[File]:` | ** -->

## Reglas de estilo y funcionalidad
| Style | Syntax | Example | Result | Comments
| --- | --- | --- | --- | --- |
| Italic | `* *` | `*This text is italicized*` | ![style-1](assets/images/lbl-italic.png) | --- |
| Bold | `** **` | `**This is bold text**` | ![style-2](assets/images/lbl-bold.png)| --- |
| Bold and Italic | `*** ***` | `****This text is in bold and italics****` | ![style-3](assets/images/lbl-bold-and-italic.png)| --- |
| Underline | `__ __` | `__This text is underlined__` | ![style-4](assets/images/lbl-underline.png) | --- |
| Line Through | `-- --` | `--This was mistaken text--` | ![style-5](assets/images/lbl-line-through.png) | --- |
| Subscript | `<sub> </sub>` | `This is a <sub>subscript</sub> text` | ![style-6](assets/images/lbl-sub.png) | --- |
| Superscript | `<sup> </sup>` | `This is a <sup>superscript</sup> text` | ![style-7](assets/images/lbl-sup.png) | --- |
| Link | `{ text \| url }` | `Check our {GitHub \| https://www.github.com} page.` | ![style-8](assets/images/lbl-link.png) | --- |
| Placeholders | `$0, $1, etc..` | `Hello! my name is $0.` | ![style-9](assets/images/lbl-placeholder.gif) | *The marker `$0` can be replaced with an instance of `str` or `StringVar`*. |

## Hot-Reloading