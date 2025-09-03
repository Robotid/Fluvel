
# Syntactic rules for creating the application's main menu

- The character **`#`** represents a line comment.
- A line **`key = "text"`** represents a **key-value** argument where the key is used to access the `"text"`.
- The combination **`[text]:`** followed by indentation represents a **dictionary**.
- The indented elements after **`[text]:`** are **key-value** arguments or other **dictionaries**.
- **`@any_text`** is conceptually a section separator, which visually represents a **separator line** in the options menu.

## Demostration
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
```