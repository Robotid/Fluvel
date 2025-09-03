
# Syntactic rules for declaring static text content application
 
* **`#`**: inline comments
* **`[text-id]:`**: dict that contains the `content_id` of the `StyledText`
* Indentation rules to define nesting **(only 1 level is allowed)**:

## Style Rules
|Style            | Syntax                | Result in RichText                                                           |
|-----------------|-----------------------|------------------------------------------------------------------------------|
| Italic          | **`* *`**             | `<span style='font-style: italic;'>`                                         | 
| Bold            | **`** **`**           | `<span style='font-weight: bold;'>`                      |
| Bold and Italic | **`*** ***`**         | `<span style='font-weight: bold; font-style: italic;'>`                      |
| Underline       | **`__ __`**           | `<span style='text-decoration: underline;'>`                                 |
| Line Through    | **`-- --`**           | `<span style='text-decoration: line-throug;'>`                               |
| Subscript       | **`<sub> </sub>`**    | `<span style='vertical-align: sub'>`                                         |
| Superscript     | **`<sup> </sup>`**    | `<span style='vertical-align: sup'>`                                         |
| Link            | **`{text \| url}`**   | `<a href='link'> value </a>`                                                 |
| Placeholders    | **`$0, $1, etc...`**  | `Placeholders that will be dynamically replaced by text in the application.` |
 
 ## Demostration
 ```
[welcome-message]:
    **Hi!** $0, this is *an* __demostration__. Check our *{Youtube | https://www.youtube.com}* channel.
 ```
