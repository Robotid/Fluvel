# Registro de Cambios

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), y este proyecto adhiere al versionado semántico.

## [0.1.0a2] - 2025-08-28

### Added

- CLI: comando `build`.
- CLI: comando `reset`.
- CLI: comando `init`.

### Changed

- Migración a la fase Beta. La API del framework ahora es más estable.

### Deprecated
- `filter_by_extension` fue reemplazada por `Path.rglob`.
- `load_app_config` fue reemplazada por `load_file`.
- Se eliminó `get_default_config` al no ser necesaria.
- `project/GlobalConfig.py` pasó a ser la clase `APP` de `fluvel._user.Config.APP`.

### Fixed

- Corrección de errores críticos en la integración de `PyInstaller`.
- Solución de errores en el manejo de archivos `.fluml`.

## [0.1.0a1] - 2025-08-25

### Added

- `GlobalContent`: Añadida la clase para gestionar el contenido estático.
- `StringVars`: Introducido el sistema de variables reactivas.
- `fluvel init`: Creado el comando para inicializar la estructura del proyecto.
- Sistema de internacionalización basado en archivos `.fluml`.

### Fixed

- Solucionado el error de importación de `fluvel.core`.