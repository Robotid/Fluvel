COMPACT_BOOTSTRAP = """
QCheckBox {
    spacing: 5px; /* Space between the indicator and the text */
    color: #212529; /* Bootstrap's default text color */
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border: 1px solid #ced4da; /* Bootstrap's default border color for inputs */
    border-radius: 3px; /* Slightly rounded corners */
    background-color: #fff; /* White background */
}

QCheckBox::indicator:unchecked {
    /* No specific icon for unchecked state, just the border */
    border: 1px solid #ced4d1;
}

QCheckBox::indicator:checked {
    background-color: #0d6efd; /* Bootstrap primary blue */
    border-color: #0d6efd;
    image: url(check_icon.png); /* Path to your checkmark icon */
    /* You'll need a small white checkmark icon. */
    /* Alternatively, you can try to draw it with gradients, but an image is easier. */
}

QCheckBox::indicator:hover {
    border-color: #86b7fe; /* Lighter blue for hover */
}

QCheckBox::indicator:checked:hover {
    background-color: #0a58ca; /* Darker blue on hover when checked */
    border-color: #0a58ca;
}

QCheckBox::indicator:pressed {
    background-color: #0a58ca; /* Darker blue on press */
    border-color: #0a58ca;
}

QCheckBox:focus {
    outline: none; /* Remove default focus outline */
    /* The box-shadow on :hover should handle visual focus indication */
}/* Info Alert */

*[type="card-container"] {
    border-radius: 5px;
    padding-top: 3px;
    border-bottom: 4px solid;
}

*[type="card-description"] {
    color: #fff;
    background: none;
    border: none;
    font-family: Montserrat, "Segoe UI", "Helvetica Neue", sans-serif;
    font-size: 14px;
    font-weight: 500;
    margin: 0px;
    padding-top: 2px;
    padding-bottom: 0px;
}

QPushButton[type="card-description"] {
    background-color: #ffffff;
    margin-right: 10px;
}

QPushButton[type="card-description"]:hover {
    background: #fff;
}

QFrame#InfoCard {
    background-color: #3a7bde;
    border-color: #244c94;
}

QFrame#WarningCard {
    background-color: #f5cc63;
    border-color: #c3a214;
}

QFrame#DangerCard {
    background-color: #b03b22;
    border-color: #722413;
}

QFrame#SuccessCard {
    background-color: #007b66;
    border-color: #025244;
}QLabel {
    /* Estilos base del Label */
    color: #343a40;
    background-color: transparent;
    font-size: 14px; 
    font-weight: 400;
    margin: 5px;
}


/* ==================== Alertas y Tarjetas ==================== */

QLabel[class~="info"], QLabel[class~="success"], QLabel[class~="warning"], QLabel[class~="danger"] {
    padding: 10px 15px;
    border-radius: 5px;
    border-left: 4px solid;
    color: #f0f0f0;
}

QLabel[class~="info"] {
    background-color: #dbeafe;
    border-color: #60a5fa;
    color: #508ef7
}

QLabel[class~="success"] {
    background-color: #DCFCE7;
    border-color: 3px solid #62ca89;
    color: #34bd66;
}

QLabel[class~="warning"] {
    background-color: #faecdb;
    border-left: 3px solid #ff9800;
    color: #f18d54;
}

QLabel[class~="danger"] {
    background-color: #fdecea;
    border-left: 3px solid #f44336;
    color: #f44358;
}/* styles_minimal.qss */

/* * Colores base inspirados en Bootstrap
 * Es importante que reemplaces manualmente `var(--nombre-variable)` con los valores hexadecimales.
 */
/* Puedes ajustarlos a tu paleta de colores específica. */
/* --primary: #007bff; */         /* Azul */
/* --dark: #343a40; */           /* Gris oscuro para el menubar */
/* --light: #f8f9fa; */          /* Gris muy claro para el resaltado del menú */
/* --body-bg: #fff; */           /* Fondo principal */
/* --text-color: #212529; */     /* Color de texto oscuro */
/* --border-radius: 0.25rem; */  /* Radio de borde pequeño */

/* * Estilo general de la MainWindow
 */
QMainWindow {
    background-color: #fff; /* Simula el --body-bg */
    color: #212529;         /* Simula el --text-color */
    font-family: "Segoe UI", "Helvetica Neue", sans-serif;
    font-size: 14px; /* Tamaño de fuente base */
}
/* QWidget#central-wd {
    background-color: #7136e0;
} */
/* ==================== QMenu, QMenuBar ==================== */
QMenuBar {
    background-color: #e9ecef; /* Un gris claro para la barra de menú */
    color: #212529; /* Texto oscuro */
    padding: 4px;
}

QMenuBar::item {
    padding: 5px 10px;
    background-color: transparent;
}

QMenuBar::item:selected {
    background-color: #007bff; /* Fondo azul al seleccionar */
    color: #ffffff; /* Texto blanco */
    border-radius: 3px;
}

QMenu {
    background-color: #ffffff; /* Fondo blanco para los menús desplegables */
    border: 1px solid #dee2e6;
    border-radius: 4px;
    padding: 5px 0;
}

QMenu::item {
    padding: 6px 20px;
    color: #212529;
}

QMenu::item:selected {
    background-color: #007bff;
    color: #ffffff;
    border-radius: 3px; /* Bordes redondeados para los ítems del menú */
}

QMenu::separator {
    height: 1px;
    background: #ced4da;
    margin: 5px 0px;
}

/* ==================== ToolTips (QToolTip) ==================== */
QToolTip {
    background-color: #212529; /* Fondo oscuro */
    color: #ffffff; /* Texto blanco */
    border: 1px solid #212529;
    border-radius: 4px;
    padding: 5px 8px;
    opacity: 200; /* Completamente opaco */
}
QPushButton {
    /* Estilos base del PushButton */
    color: #fff;
    font-size: 14px;
    font-weight: 700; 
    text-align: center; 
    border: 1px solid;
    border-radius: 5px;
    padding: 8px 16px; 
    outline: none;
}

QPushButton:pressed {
    padding-bottom: 6px;
}

QPushButton:disabled {
    /* Estilos para el botón deshabilitado */
    background-color: #e9ecef; 
    color: #6c757d;
    border: 1px solid #ced4da; 
}


/* Estilo para un Primary Button */

QPushButton[class~="primary"] {
    background-color: #007bff;
    border-color: #007bff;
}
QPushButton[class~="primary"]:hover {
    background-color: #0071eb;
    border-color: #0071eb;
}
QPushButton[class~="primary"]:pressed {
    background-color: #0068d6;
    border-color: #0068d6;
}
QPushButton[class~="primary-outlined"] {
    color: #007bff;
    background-color: transparent;
    border-color: #007bff;
}
QPushButton[class~="primary-outlined"]:hover {
    color: #0071eb;
    background-color: transparent;
    border-color: #0071eb;
}
QPushButton[class~="primary-outlined"]:pressed {
    color: #0068d6;
    background-color: transparent;
    border-color: #0068d6;
}
    
/* Estilo para un Secondary Button */

QPushButton[class~="secondary"] {
    background-color: #858e96;
    border-color: #858e96;
}
QPushButton[class~="secondary"]:hover {
    background-color: #7f848a;
    border-color: #7f848a;
}
QPushButton[class~="secondary"]:pressed {
    background-color: #767a80;
    border-color: #767a80;
}
QPushButton[class~="secondary-outlined"] {
    color: #858e96;
    background-color: transparent;
    border-color: #858e96;
}
QPushButton[class~="secondary-outlined"]:hover {
    color: #7f848a;
    background-color: transparent;
    border-color: #7f848a;
}
QPushButton[class~="secondary-outlined"]:pressed {
    color: #767a80;
    background-color: transparent;
    border-color: #767a80;
}
    
/* Estilo para un Info Button */

QPushButton[class~="info"] {
    background-color: #17a2b8;
    border-color: #17a2b8;
}
QPushButton[class~="info"]:hover {
    background-color: #1c98ac;
    border-color: #1c98ac;
}
QPushButton[class~="info"]:pressed {
    background-color: #1490a3;
    border-color: #1490a3;
}
QPushButton[class~="info-outlined"] {
    color: #17a2b8;
    background-color: transparent;
    border-color: #17a2b8;
}
QPushButton[class~="info-outlined"]:hover {
    color: #1497ac;
    background-color: transparent;
    border-color: #1497ac;
}
QPushButton[class~="info-outlined"]:pressed {
    color: #138a9c;
    background-color: transparent;
    border-color: #138a9c;
}
    
/* Estilo para un Success Button */

QPushButton[class~="success"] {
    background-color: #00a441;
    border-color: #00a441;
}
QPushButton[class~="success"]:hover {
    background-color: #009b3e;
    border-color: #009b3e;
}
QPushButton[class~="success"]:pressed {
    background-color: #008d38;
    border-color: #008d38;
}
QPushButton[class~="success-outlined"] {
    color: #00a441;
    background-color: transparent;
    border-color: #00a441;
}
QPushButton[class~="success-outlined"]:hover {
    color: #009b3e;
    background-color: transparent;
    border-color: #009b3e;
}
QPushButton[class~="success-outlined"]:pressed {
    color: #008d38;
    background-color: transparent;
    border-color: #008d38;
}
    
/* Estilo para un Warning Button */

QPushButton[class~="warning"] {
    background-color: #ffbe00;
    border-color: #ffbe00;
}
QPushButton[class~="warning"]:hover {
    background-color: #eeb200;
    border-color: #eeb200;
}
QPushButton[class~="warning"]:pressed {
    background-color: #e6ac00;
    border-color: #e6ac00;
}
QPushButton[class~="warning-outlined"] {
    color: #ffbe00;
    background-color: transparent;
    border-color: #ffbe00;
}
QPushButton[class~="warning-outlined"]:hover {
    color: #eeb200;
    background-color: transparent;
    border-color: #eeb200;
}
QPushButton[class~="warning-outlined"]:pressed {
    color: #e6ac00;
    background-color: transparent;
    border-color: #e6ac00;
}
    
/* Estilo para un Danger Button */

QPushButton[class~="danger"] {
    background-color: #e63a40;
    border-color: #e63a40;
}
QPushButton[class~="danger"]:hover {
    background-color: #d43439;
    border-color: #d43439;
}
QPushButton[class~="danger"]:pressed {
    background-color: #c93237;
    border-color: #c93237;
}
QPushButton[class~="danger-outlined"] {
    color: #e63a40;
    background-color: transparent;
    border-color: #e63a40;
}
QPushButton[class~="danger-outlined"]:hover {
    color: #d43439;
    background-color: transparent;
    border-color: #d43439;
}
QPushButton[class~="danger-outlined"]:pressed {
    color: #c93237;
    background-color: transparent;
    border-color: #c93237;
}
    
/* Estilo para un Dark Button */

QPushButton[class~="dark"] {
    color: #fff;
    background-color: #272923;
    border-color: #232629;
}
QPushButton[class~="dark"]:hover {
    background-color: #333a40;
    border-color: #333a40;
}
QPushButton[class~="dark"]:pressed {
    background-color: #25292c;
    border-color: #25292c;
}
QPushButton[class~="dark-outlined"] {
    color: #232629;
    background-color: transparent;
    border-color: #232629;
}
QPushButton[class~="dark-outlined"]:hover {
    color: #333a40;
    background-color: transparent;
    border-color: #333a40;
}
QPushButton[class~="dark-outlined"]:pressed {
    color: #25292c;
    background-color: transparent;
    border-color: #25292c;
}
    
/* Estilo para un Light Button */

QPushButton[class~="light"] {
    color: #25292c;
    background-color: #f6f8fa;
    border-color: #b9b9b9;
}
QPushButton[class~="light"]:hover {
    background-color: #e8eaec;
    border-color: #b9b9b9;
}
QPushButton[class~="light"]:pressed {
    background-color: #e3e5e7;
    border-color: #b9b9b9;
}
QPushButton[class~="light-outlined"] {
    color: #25292c;
    background-color: transparent;
    border-color: #b9b9b9;
}
QPushButton[class~="light-outlined"]:hover {
    background-color: transparent;
    border-color: #b9b9b9;
}
QPushButton[class~="light-outlined"]:pressed {
    background-color: transparent;
    border-color: #b9b9b9;
}/* QToolBar estilo Bootstrap */
QToolBar {
    background-color: #f8f9fa;  /* bg-light */
    border: 1px solid #dee2e6;  /* border */
    padding: 6px;               /* espacio interno */
    spacing: 4px;               /* espacio entre íconos */
}

/* Botones dentro del ToolBar */
QToolButton {
    background-color: #ffffff;        /* fondo blanco */
    border: 1px solid #ced4da;        /* border-secondary */
    border-radius: 4px;
    padding: 4px 8px;
    margin: 2px;
    color: #212529;                   /* texto oscuro */
    font-weight: 500;
    min-width: 100px; /* Establece el mismo valor para min-width y max-width */
    max-width: 100px; /* Esto efectivamente fija el ancho */
    text-align: center; /* Alinea el contenido al centro */
}

QToolButton:hover {
    background-color: #e2e6ea;        /* hover-light */
    border-color: #adb5bd;
}

QToolButton:pressed {
    background-color: #dae0e5;        /* active-light */
    border-color: #adb5bd;
}

QToolButton:checked {
    background-color: #0d6efd;        /* primary */
    border-color: #0d6efd;
    color: #fff;
}

/* Íconos de ToolButton */
QToolButton::menu-indicator {
    image: none;  /* ocultar el indicador del menú desplegable */
}

/* Separadores */
QToolBar::separator {
    background-color: #dee2e6;
    width: 1px;
    margin: 4px;
}

/* Espaciadores personalizados */
QWidget#ToolBarSpacer {
    background-color: transparent;
}/*
 * bootstrap_style.qss
 * Estilos globales inspirados en Bootstrap para PySide6
 */

/* ==================== Estilos Generales / Root ==================== */
* {
    /* Fuente base */
    font-family: "Segoe UI", "Helvetica Neue", "Arial", sans-serif;
    font-size: 14px;
    color: #343a40; 
    
    /* Colores de fondo */
    background-color: #f8f9fa;
}

QWidget {
    background-color: transparent;
}

/* ==================== QLineEdit, QTextEdit, QPlainTextEdit ==================== */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #ffffff;
    border: 1px solid #ced4da; /* Borde de Bootstrap input-border-color */
    border-radius: 4px;
    padding: 6px 12px;
    selection-background-color: #80bdff; /* Color de selección azul de Bootstrap */
    selection-color: #ffffff; /* Texto blanco en la selección */
}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border-color: #80bdff; /* Borde azul al enfocar */
    outline: 0;

}

/* ==================== QComboBox ==================== */
QComboBox {
    background-color: #ffffff;
    border: 1px solid #ced4da;
    border-radius: 4px;
    padding: 5px 10px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 1px;
    border-left-color: #ced4da;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iY3VycmVudENvbG9yIiBjbGFzcz0iYmkgYmktY2hldnJvbi1leHBhbmQtbXYiIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNNi40NjQgMi44OTZjLjE1OS0uMTg4LjM2LS4zMDUuNTctLjM4N2wuNzg0LS4zNTJjLjIwNC0uMDkyLjQxLS4xNDkuNjEzLS4xNjYuMjAyLS4wMTcuMzk0LS4wMTMuNTgzLjAxMmwuODc4LjIwMWMuMTkuMDQ2LjM3MS4xNDIuNTI4LjI4M0wxNS4yNSA5LjIzNGExIDEgMCAwIDEtMS41MDIgMS4zMTZMMjU2Ljc1IDYuNDQ3bC05LjUyOSA5LjUyOXMtMi40NzcgNS41MTYtNS40NDItMy44NTMtMS42MDktMi45NDMtLjcxOS0yLjM2YzEuNzA2IDEuMTU0IDIuNjA1IDEuMTc0IDIuODIgMS4yOTcuMjQ2LjE0OS42ODguMTU0Ljg3LjAyNi4yMjUtLjE2Mi43MzctLjUwNC44MDMtLjUyLjI4LS4wNjYuNTI5LS4xNjQuNzU5LS4yODZjLjIzLS4xMjIuNDQ0LS4yNTguNjQ3LS4zNDkuMjA0LS4wOTMuMzk1LS4xNjYuNTc2LS4yMjcuMTgyLS4wNjIuMzU2LS4xMDUuNTIyLS4xMjUuMzIyLS4wNDYuNjU1LS4wOTUuOTc3LS4xMjIuMzIyLS4wMjcuNjQ1LS4wMjcuOTU5LjAxMi4zMTQuMDQuNjE4LjEwNy45MDkuMjA0bDEuMDA1LjMxYzEuMS4zNC4xMzcgNS41MTYtLjUwMyA5LjUzMSAxLjEyNS0uNzAyIDcuMzcxIDUuMzE1LTkuNjQzLS41MjYtLjEzMi0uMjEzLS4zNDMtLjUxMy0uNDIxLS43NjItLjEyNy0uMTctLjE0OS0uMjg1LS4xNTUtLjMxNC0uMDE4LS4xNTMtLjA0LS4zMDktLjA0OC0uNDY1bC0uMDA4LS41MDhjLjAwMy0uMTU2LjAxNS0uMjkxLjAyMy0uNDEzbC4wMTktLjI1Yy4wMDgtLjExOC4wMzYtLjI0NC4wNzQtLjM3LjA1LS4xOTEuMTItLjM4Ny4yMDgtLjU5NGwuMDgzLS4yMDQuMTczLS40MzYuMjY0LS42NzQuMTYtLjQzOC4yNTgtLjY3Ny4zMzUtLjg2Mi4xNTMtLjM1Ny4zMDktLjczOC40NzYtMS4xNjMuMjItLjU1NC4zNjMtMS4xOTEuNDMtMS44OTFsLjAyLS43MWMuMDEzLS41NzctLjA1NS0xLjIyNy0uMTI3LTEuODYyLS4wNzEtLjYzNS0uMTY0LTEuMjU0LS4yNy0xLjg0NS0uMTA3LS41OTUtLjIzNS0xLjE3Ni0uMzg3LTEuNzQyLS4xNTItLjU2Ny0uMzIyLTEuMTA0LS40ODgtMS42My0uMTY3LS41MjYtLjM1LTEuMDMzLS41NS0xLjUzNS0uMi0uNTAyLS40MTctLjk4LS42NDYtMS40MzItLjIyOS0uNDUxLS40NzYtLjg4Mi0uNzMyLTEuMjkuMjI2LS4xODkuNDU0LS4zNjYuNjk2LS41MjcuMjQzLS4xNjEuNDk4LS4zMDYuNzU4LS40MjkuMjYtLjEyMy41MjctLjIxOS43OTctLjI4Ny4yNy0uMDY4LjU0Ny0uMTExLjgyOC0uMTE2LjI4MS0uMDA1LjU2MS4wMTcuODM3LjA2Ny4yNzUuMDUtLjU4My4wNjEtMS4wMjMuMDc1bC0uOTEuMDY5Yy0uMTgxLjAxMy0uMzczLjAyMi0uNTYyLjAyNi0uMTg4LjAwMy0uMzc5LjAwNy0uNTcxLjAxMWwtLjYwOC4wMTFjLS4yMy4wMDItLjQ2LjAxLS42ODguMDI0LS4yMjguMDEzLS40NTUuMDMxLS42NzguMDYyLS4yMjQuMDMxLS40NDUuMDY5LS42NjIuMTE4LS4yMTcuMDQ5LS40MjkuMTEyLS42MzQuMTgyLS4yMDYuMDctLjQwNS4xNDYtLjU5OC4yMzQtLjE5NC4wODgtLjM3OC4xODQtLjU1NS4yODktLjE3Ni4xMDYtLjM0Mi4yMjQtLjQ5NC4zNDYtLjE1My4xMjMtLjI5Mi4yNTUtLjQxMy4zOTYtLjEyMi4xNDEtLjIyNi4yOTItLjMyLjQ0OS0uMDk1LjE1Ny0uMTc0LjMyMi0uMjM4LjQ4OS0uMDY1LjE2Ny0uMTE2LjMzOC0uMTU2LjUxLS4wNC4xNzMtLjA2Mi4zNDYtLjA2Ni41MTgtLjAwNS4xNzIuMDA1LjM0My4wMy41MDkuMDI0LjE2Ni4wNi4zMjYuMTEuNDgyLjA1LjE1Ni4xMTUuMzA1LjE5LjQ0Mi4wNzYuMTM3LjE2LjI2Ny4yNDguMzg3bC4zNTguNTA2LjQzOS41OTEuNTMuNzE4LjY0NC43OTQuNjU0Ljc4MS43MjMuODQ4IDEuMDQ2IDEuMTM1eiIvPjwvc3ZnPg==); /* Imagen SVG de una flecha hacia abajo */
    width: 16px;
    height: 16px;
}

QComboBox QAbstractItemView {
    border: 1px solid #ced4da; /* Borde para el menú desplegable */
    border-radius: 4px;
    selection-background-color: #007bff;
    selection-color: #ffffff;
    background-color: #ffffff;
}

/* ==================== QCheckBox y QRadioButton ==================== */
QCheckBox::indicator {
    width: 16px;
    height: 16px;
    background-color: #ffffff;
    border: 1px solid #ced4da;
    border-radius: 3px; /* Más cuadrado para checkbox */
}

QCheckBox::indicator:checked {
    background-color: #007bff;
    border: 1px solid #007bff;
    image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iI2ZmZmZmZiIgY2xhc3M9ImJpIGJpLWNoZWNrIiB2aWV3Qm94PSIwIDAgMTYgMTYiPjxwYXRoIGQ9Ik0xMy44NTQgMy42NDZhLjUuNSAwIDAgMSAwIC43MDhsLTcgN2EuNS41IDAgMCAxLS43MDggMEwxLjc5MyA5LjQxN2EuNS41IDAgMCAxIC43MDgtLjcwOEw2LjUgMTAuMjkybDYuNjQ2LTYuNjQ3YS41LjUgMCAwIDEgLjcwOCAweiIvPjwvc3ZnPg==); /* Icono de check blanco SVG */
}

QCheckBox::indicator:disabled {
    background-color: #e9ecef;
    border-color: #ced4da;
}

QRadioButton::indicator {
    width: 16px;
    height: 16px;
    background-color: #ffffff;
    border: 1px solid #ced4da;
    border-radius: 8px; /* Redondo para radio button */
}

QRadioButton::indicator:checked {
    background-color: #007bff;
    border: 1px solid #007bff;
    image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iI2ZmZmZmZiIgY2xhc3M9ImJpIGJpLWRvdCIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBkPSJBNi41IDhhMS41IDEuNSAwIDEgMC0zIDAgMS41IDEuNSAwIDAgMCAzIDBaIi8+PC9zdmc+); /* Icono de punto blanco SVG */
}

QRadioButton::indicator:disabled {
    background-color: #e9ecef;
    border-color: #ced4da;
}

/* ==================== QSlider ==================== */
QSlider::groove:horizontal {
    border: 1px solid #ced4da;
    height: 8px;
    background: #e9ecef;
    margin: 2px 0;
    border-radius: 4px;
}

QSlider::handle:horizontal {
    background: #007bff;
    border: 1px solid #007bff;
    width: 18px;
    margin: -5px 0; /* Centra el handle en el groove */
    border-radius: 9px;
}

QSlider::sub-page:horizontal {
    background: #007bff;
    border-radius: 4px;
}

/* ==================== QProgressBar ==================== */
QProgressBar {
    border: 1px solid #ced4da;
    border-radius: 5px;
    text-align: center;
    background-color: #e9ecef;
    color: #343a40;
}

QProgressBar::chunk {
    background-color: #007bff;
    border-radius: 4px;
}

/* ==================== QScrollBar (vertical y horizontal) ==================== */
QScrollBar:vertical {
    border: 1px solid #ced4da;
    background: #f8f9fa;
    width: 12px;
    margin: 0px 0px 0px 0px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: #6c757d;
    min-height: 20px;
    border-radius: 5px;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px; /* Eliminar flechas */
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QScrollBar:horizontal {
    border: 1px solid #ced4da;
    background: #f8f9fa;
    height: 12px;
    margin: 0px 0px 0px 0px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background: #6c757d;
    min-width: 20px;
    border-radius: 5px;
}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px; /* Eliminar flechas */
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

/* ==================== QTabWidget ==================== */
QTabWidget::pane { /* El marco donde residen las páginas */
    border: 1px solid #dee2e6; /* Borde de Bootstrap nav-tabs-border-color */
    background-color: #ffffff;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
}

QTabBar::tab {
    background: #e9ecef; /* Fondo de las pestañas inactivas */
    border: 1px solid #dee2e6;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    padding: 8px 15px;
    margin-right: 2px;
    color: #495057; /* Texto de pestañas inactivas */
}

QTabBar::tab:selected {
    background: #ffffff; /* Fondo de la pestaña activa */
    border-bottom-color: #ffffff; /* Para que parezca unida al panel */
    color: #007bff; /* Texto azul para la pestaña activa */
    font-weight: bold;
}

QTabBar::tab:hover {
    background-color: #e2e6ea; /* Fondo al pasar el ratón */
    color: #007bff;
}

/* ==================== QGroupBox ==================== */
QGroupBox {
    background-color: #ffffff;
    border: 1px solid #dee2e6;
    border-radius: 5px;
    margin-top: 1em; /* Espacio para el título */
    padding: 10px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 3px;
    left: 10px;
    top: -8px; /* Mueve el título ligeramente fuera del borde */
    color: #343a40;
    font-weight: bold;
    background-color: #ffffff; /* Fondo para que el texto del título no se mezcle con el borde */
}

/* ==================== QMenu, QMenuBar ==================== */
QMenuBar {
    background-color: #e9ecef; /* Un gris claro para la barra de menú */
    color: #212529; /* Texto oscuro */
    padding: 4px;
}

QMenuBar::item {
    padding: 5px 10px;
    background-color: transparent;
}

QMenuBar::item:selected {
    background-color: #007bff; /* Fondo azul al seleccionar */
    color: #ffffff; /* Texto blanco */
    border-radius: 3px;
}

QMenu {
    background-color: #ffffff; /* Fondo blanco para los menús desplegables */
    border: 1px solid #dee2e6;
    border-radius: 4px;
    padding: 5px 0;
}

QMenu::item {
    padding: 6px 20px;
    color: #212529;
}

QMenu::item:selected {
    background-color: #007bff;
    color: #ffffff;
    border-radius: 3px; /* Bordes redondeados para los ítems del menú */
}

QMenu::separator {
    height: 1px;
    background: #ced4da;
    margin: 5px 0px;
}

/* ==================== ToolTips (QToolTip) ==================== */
QToolTip {
    background-color: #212529; /* Fondo oscuro */
    color: #ffffff; /* Texto blanco */
    border: 1px solid #212529;
    border-radius: 4px;
    padding: 5px 8px;
    opacity: 200; /* Completamente opaco */
}

*{
    border-color: #9c9c9c;
}

/* BORDER RADIUS - Mapped to fixed pixel values */


/* BORDER RADIUS ALL (rounded-*) */
*[class~="rounded-none"] { border-radius: 0; }
*[class~="rounded-xs"] { border-radius: 2px; }
*[class~="rounded-sm"] { border-radius: 4px; }
*[class~="rounded-md"] { border-radius: 6px; }
*[class~="rounded-lg"] { border-radius: 8px; }
*[class~="rounded-xl"] { border-radius: 12px; }
*[class~="rounded-2xl"] { border-radius: 16px; }
*[class~="rounded-3xl"] { border-radius: 24px; }
*[class~="rounded-4xl"] { border-radius: 32px; }
*[class~="rounded-full"] { border-radius: 50%; }

/* BORDER RADIUS SIDES (rounded-t, rounded-r, rounded-b, rounded-l) */

*[class~="rounded-t-md"] { 
    border-top-left-radius: 6px; 
    border-top-right-radius: 6px; 
}
*[class~="rounded-t-2xl"] { 
    border-top-left-radius: 16px; 
    border-top-right-radius: 16px; 
}


*[class~="rounded-r-md"] { 
    border-top-right-radius: 6px; 
    border-bottom-right-radius: 6px; 
}
*[class~="rounded-b-md"] { 
    border-bottom-right-radius: 6px; 
    border-bottom-left-radius: 6px; 
}
*[class~="rounded-b-2xl"] { 
    border-bottom-right-radius: 16px; 
    border-bottom-left-radius: 16px; 
}
*[class~="rounded-l-md"] { 
    border-top-left-radius: 6px; 
    border-bottom-left-radius: 6px; 
}

/* BORDER RADIUS CORNERS (rounded-tl, rounded-tr, rounded-br, rounded-bl) */

*[class~="rounded-tl-md"] { border-top-left-radius: 6px; }
*[class~="rounded-tr-md"] { border-top-right-radius: 6px; }
*[class~="rounded-br-md"] { border-bottom-right-radius: 6px; }
*[class~="rounded-bl-md"] { border-bottom-left-radius: 6px; }


/* rounded-ss-* (Start-Start -> Top-Left) */
*[class~="rounded-ss-md"] { border-top-left-radius: 6px; }

/* rounded-se-* (Start-End -> Top-Right) */
*[class~="rounded-se-md"] { border-top-right-radius: 6px; }

/* rounded-ee-* (End-End -> Bottom-Right) */
*[class~="rounded-ee-md"] { border-bottom-right-radius: 6px; }

/* rounded-es-* (End-Start -> Bottom-Left) */
*[class~="rounded-es-md"] { border-bottom-left-radius: 6px; }


/* rounded-s-* (Start Side -> Top-Left and Bottom-Left) */
*[class~="rounded-s-md"] { 
    border-top-left-radius: 6px; 
    border-bottom-left-radius: 6px;
}

/* rounded-e-* (End Side -> Top-Right and Bottom-Right) */
*[class~="rounded-e-md"] { 
    border-top-right-radius: 6px; 
    border-bottom-right-radius: 6px;
}

/* ========================================================================= */
/* 7. BORDERS (border-*, border-t-*, border-style)                           */
/* ========================================================================= */

*[class~="border-basic"] {
    border: 1px solid #adabab;
    border-radius: 6px;
}

/* BORDER WIDTH ALL (border-*) */
*[class~="border-0"] { border-width: 0px; }
*[class~="border"] { border-width: 1px; }
*[class~="border-px"] { border-width: 1px; }
*[class~="border-2"] { border-width: 2px; }
*[class~="border-4"] { border-width: 4px; }
*[class~="border-8"] { border-width: 8px; }

/* BORDER STYLE (border-*) */
*[class~="border-solid"] { border-style: solid; }
*[class~="border-dashed"] { border-style: dashed; }
*[class~="border-dotted"] { border-style: dotted; }
*[class~="border-none"] { border-style: none; }

/* BORDER WIDTH INDIVIDUAL SIDES */
/* border-x/y-* (Horizontal/Vertical) */
*[class~="border-x"] { border-left-width: 1px; border-right-width: 1px; }
*[class~="border-x-2"] { border-left-width: 2px; border-right-width: 2px; }
*[class~="border-x-4"] { border-left-width: 4px; border-right-width: 4px; }

*[class~="border-y"] { border-top-width: 1px; border-bottom-width: 1px; }
*[class~="border-y-2"] { border-top-width: 2px; border-bottom-width: 2px; }
*[class~="border-y-4"] { border-top-width: 4px; border-bottom-width: 4px; }

/* Top (T) */
*[class~="border-t"] { border-top-width: 1px; }
*[class~="border-t-2"] { border-top-width: 2px; }
*[class~="border-t-4"] { border-top-width: 4px; }
*[class~="border-t-0"] { border-top-width: 0px; }

/* Bottom (B) */
*[class~="border-b"] { border-bottom-width: 1px; }
*[class~="border-b-2"] { border-bottom-width: 2px; }
*[class~="border-b-4"] { border-bottom-width: 4px; }

/* Left (L) - Physical mapping for start/L/S */
*[class~="border-l"] { border-left-width: 1px; }
*[class~="border-l-2"] { border-left-width: 2px; }
*[class~="border-l-4"] { border-left-width: 4px; }

/* Right (R) - Physical mapping for end/R/E */
*[class~="border-r"] { border-right-width: 1px; }
*[class~="border-r-2"] { border-right-width: 2px; }
*[class~="border-r-4"] { border-right-width: 4px; }


/* BORDER STYLE (border-*) */
*[class~="border-solid"] { border-style: solid; }
*[class~="border-dashed"] { border-style: dashed; }
*[class~="border-dotted"] { border-style: dotted; }
*[class~="border-none"] { border-style: none; }



*[class~="bcolor-warning"] { border-color: #9a6700; }
*[class~="alert-warning"] { color: #cd9533; }/* Font Size */
*[class~="text-xs"] { font-size: 12px; }
*[class~="text-sm"] { font-size: 14px; }
*[class~="text-base"] { font-size: 16px; }
*[class~="text-lg"] { font-size: 18px; }
*[class~="text-xl"] { font-size: 20px; }
*[class~="text-2xl"] { font-size: 24px; }
*[class~="text-3xl"] { font-size: 28px; }
*[class~="text-4xl"] { font-size: 32px; }

/* Font Weight */
*[class~="font-extralight"] { font-weight: 200; }
*[class~="font-light"] { font-weight: 300; }
*[class~="font-normal"] { font-weight: 400; }
*[class~="font-medium"] { font-weight: 500; }
*[class~="font-semibold"] { font-weight: 600; }
*[class~="font-bold"] { font-weight: 700; }

/* Text Alignment */
*[class~="text-left"] { text-align: left; }
*[class~="text-center"] { text-align: center; }
*[class~="text-right"] { text-align: right; }
/* Background base */
*[class~="bg-transparent"] { background-color: transparent; }

/* --- Paleta de Colores --- */
*[class~="bg-black"] { background-color: rgb(0, 0, 0); }
*[class~="bg-white"] { background-color: rgb(255, 255, 255); }

/* Slate */
*[class~="bg-slate-50"] { background-color: rgb(248, 250, 252); }
*[class~="bg-slate-100"] { background-color: rgb(241, 245, 249); }
*[class~="bg-slate-200"] { background-color: rgb(226, 232, 240); }
*[class~="bg-slate-300"] { background-color: rgb(203, 213, 225); }
*[class~="bg-slate-400"] { background-color: rgb(148, 163, 184); }
*[class~="bg-slate-500"] { background-color: rgb(100, 116, 139); }
*[class~="bg-slate-600"] { background-color: rgb(71, 85, 105); }
*[class~="bg-slate-700"] { background-color: rgb(51, 65, 85); }
*[class~="bg-slate-800"] { background-color: rgb(30, 41, 59); }
*[class~="bg-slate-900"] { background-color: rgb(15, 23, 42); }
*[class~="bg-slate-1000"] { background-color: rgb(2, 6, 23); }

/* Gray */
*[class~="bg-gray-50"] { background-color: rgb(249, 250, 251); }
*[class~="bg-gray-100"] { background-color: rgb(243, 244, 246); }
*[class~="bg-gray-200"] { background-color: rgb(229, 231, 235); }
*[class~="bg-gray-300"] { background-color: rgb(209, 213, 219); }
*[class~="bg-gray-400"] { background-color: rgb(156, 163, 175); }
*[class~="bg-gray-500"] { background-color: rgb(107, 114, 128); }
*[class~="bg-gray-600"] { background-color: rgb(75, 85, 99); }
*[class~="bg-gray-700"] { background-color: rgb(55, 65, 81); }
*[class~="bg-gray-800"] { background-color: rgb(31, 41, 55); }
*[class~="bg-gray-900"] { background-color: rgb(17, 24, 39); }
*[class~="bg-gray-1000"] { background-color: rgb(3, 7, 18); }

/* Zinc */
*[class~="bg-zinc-50"] { background-color: rgb(250, 250, 250); }
*[class~="bg-zinc-100"] { background-color: rgb(244, 244, 245); }
*[class~="bg-zinc-200"] { background-color: rgb(228, 228, 231); }
*[class~="bg-zinc-300"] { background-color: rgb(212, 212, 216); }
*[class~="bg-zinc-400"] { background-color: rgb(161, 161, 170); }
*[class~="bg-zinc-500"] { background-color: rgb(113, 113, 122); }
*[class~="bg-zinc-600"] { background-color: rgb(82, 82, 91); }
*[class~="bg-zinc-700"] { background-color: rgb(63, 63, 70); }
*[class~="bg-zinc-800"] { background-color: rgb(39, 39, 42); }
*[class~="bg-zinc-900"] { background-color: rgb(24, 24, 27); }
*[class~="bg-zinc-1000"] { background-color: rgb(9, 9, 11); }

/* Neutral */
*[class~="bg-neutral-50"] { background-color: rgb(250, 250, 250); }
*[class~="bg-neutral-100"] { background-color: rgb(245, 245, 245); }
*[class~="bg-neutral-200"] { background-color: rgb(229, 229, 229); }
*[class~="bg-neutral-300"] { background-color: rgb(212, 212, 212); }
*[class~="bg-neutral-400"] { background-color: rgb(163, 163, 163); }
*[class~="bg-neutral-500"] { background-color: rgb(115, 115, 115); }
*[class~="bg-neutral-600"] { background-color: rgb(82, 82, 82); }
*[class~="bg-neutral-700"] { background-color: rgb(64, 64, 64); }
*[class~="bg-neutral-800"] { background-color: rgb(38, 38, 38); }
*[class~="bg-neutral-900"] { background-color: rgb(23, 23, 23); }
*[class~="bg-neutral-1000"] { background-color: rgb(10, 10, 10); }

/* Stone */
*[class~="bg-stone-50"] { background-color: rgb(250, 250, 249); }
*[class~="bg-stone-100"] { background-color: rgb(245, 245, 244); }
*[class~="bg-stone-200"] { background-color: rgb(231, 229, 228); }
*[class~="bg-stone-300"] { background-color: rgb(214, 211, 209); }
*[class~="bg-stone-400"] { background-color: rgb(168, 162, 158); }
*[class~="bg-stone-500"] { background-color: rgb(120, 113, 108); }
*[class~="bg-stone-600"] { background-color: rgb(87, 83, 78); }
*[class~="bg-stone-700"] { background-color: rgb(68, 64, 60); }
*[class~="bg-stone-800"] { background-color: rgb(41, 37, 36); }
*[class~="bg-stone-900"] { background-color: rgb(28, 25, 23); }
*[class~="bg-stone-1000"] { background-color: rgb(12, 10, 9); }

/* Red */
*[class~="bg-red-50"] { background-color: rgb(254, 242, 242); }
*[class~="bg-red-100"] { background-color: rgb(254, 226, 226); }
*[class~="bg-red-200"] { background-color: rgb(254, 202, 202); }
*[class~="bg-red-300"] { background-color: rgb(252, 165, 165); }
*[class~="bg-red-400"] { background-color: rgb(248, 113, 113); }
*[class~="bg-red-500"] { background-color: rgb(239, 68, 68); }
*[class~="bg-red-600"] { background-color: rgb(220, 38, 38); }
*[class~="bg-red-700"] { background-color: rgb(185, 28, 28); }
*[class~="bg-red-800"] { background-color: rgb(153, 27, 27); }
*[class~="bg-red-900"] { background-color: rgb(127, 29, 29); }
*[class~="bg-red-1000"] { background-color: rgb(69, 10, 10); }

/* Orange */
*[class~="bg-orange-50"] { background-color: rgb(255, 247, 237); }
*[class~="bg-orange-100"] { background-color: rgb(255, 237, 213); }
*[class~="bg-orange-200"] { background-color: rgb(254, 215, 170); }
*[class~="bg-orange-300"] { background-color: rgb(253, 186, 116); }
*[class~="bg-orange-400"] { background-color: rgb(251, 146, 60); }
*[class~="bg-orange-500"] { background-color: rgb(249, 115, 22); }
*[class~="bg-orange-600"] { background-color: rgb(234, 88, 12); }
*[class~="bg-orange-700"] { background-color: rgb(194, 65, 12); }
*[class~="bg-orange-800"] { background-color: rgb(154, 52, 18); }
*[class~="bg-orange-900"] { background-color: rgb(124, 45, 18); }
*[class~="bg-orange-1000"] { background-color: rgb(67, 20, 7); }

/* Amber */
*[class~="bg-amber-50"] { background-color: rgb(255, 251, 235); }
*[class~="bg-amber-100"] { background-color: rgb(254, 243, 199); }
*[class~="bg-amber-200"] { background-color: rgb(253, 230, 138); }
*[class~="bg-amber-300"] { background-color: rgb(252, 211, 77); }
*[class~="bg-amber-400"] { background-color: rgb(251, 191, 36); }
*[class~="bg-amber-500"] { background-color: rgb(245, 158, 11); }
*[class~="bg-amber-600"] { background-color: rgb(217, 119, 6); }
*[class~="bg-amber-700"] { background-color: rgb(180, 83, 9); }
*[class~="bg-amber-800"] { background-color: rgb(146, 64, 14); }
*[class~="bg-amber-900"] { background-color: rgb(120, 53, 15); }
*[class~="bg-amber-1000"] { background-color: rgb(69, 26, 3); }

/* Yellow */
*[class~="bg-yellow-50"] { background-color: rgb(254, 252, 232); }
*[class~="bg-yellow-100"] { background-color: rgb(254, 249, 195); }
*[class~="bg-yellow-200"] { background-color: rgb(254, 240, 138); }
*[class~="bg-yellow-300"] { background-color: rgb(253, 224, 71); }
*[class~="bg-yellow-400"] { background-color: rgb(250, 204, 21); }
*[class~="bg-yellow-500"] { background-color: rgb(234, 179, 8); }
*[class~="bg-yellow-600"] { background-color: rgb(202, 138, 4); }
*[class~="bg-yellow-700"] { background-color: rgb(161, 98, 7); }
*[class~="bg-yellow-800"] { background-color: rgb(133, 77, 14); }
*[class~="bg-yellow-900"] { background-color: rgb(113, 63, 18); }
*[class~="bg-yellow-1000"] { background-color: rgb(66, 32, 6); }

/* Lime */
*[class~="bg-lime-50"] { background-color: rgb(247, 254, 231); }
*[class~="bg-lime-100"] { background-color: rgb(236, 252, 203); }
*[class~="bg-lime-200"] { background-color: rgb(217, 249, 157); }
*[class~="bg-lime-300"] { background-color: rgb(190, 242, 100); }
*[class~="bg-lime-400"] { background-color: rgb(163, 230, 53); }
*[class~="bg-lime-500"] { background-color: rgb(132, 204, 22); }
*[class~="bg-lime-600"] { background-color: rgb(101, 163, 13); }
*[class~="bg-lime-700"] { background-color: rgb(77, 124, 15); }
*[class~="bg-lime-800"] { background-color: rgb(63, 98, 18); }
*[class~="bg-lime-900"] { background-color: rgb(54, 83, 20); }
*[class~="bg-lime-1000"] { background-color: rgb(26, 46, 5); }

/* Green */
*[class~="bg-green-50"] { background-color: rgb(240, 253, 244); }
*[class~="bg-green-100"] { background-color: rgb(220, 252, 231); }
*[class~="bg-green-200"] { background-color: rgb(187, 247, 208); }
*[class~="bg-green-300"] { background-color: rgb(134, 239, 172); }
*[class~="bg-green-400"] { background-color: rgb(74, 222, 128); }
*[class~="bg-green-500"] { background-color: rgb(34, 197, 94); }
*[class~="bg-green-600"] { background-color: rgb(22, 163, 74); }
*[class~="bg-green-700"] { background-color: rgb(21, 128, 61); }
*[class~="bg-green-800"] { background-color: rgb(22, 101, 52); }
*[class~="bg-green-900"] { background-color: rgb(20, 83, 45); }
*[class~="bg-green-1000"] { background-color: rgb(5, 46, 22); }

/* Emerald */
*[class~="bg-emerald-50"] { background-color: rgb(236, 253, 245); }
*[class~="bg-emerald-100"] { background-color: rgb(209, 250, 229); }
*[class~="bg-emerald-200"] { background-color: rgb(167, 243, 208); }
*[class~="bg-emerald-300"] { background-color: rgb(110, 231, 183); }
*[class~="bg-emerald-400"] { background-color: rgb(52, 211, 153); }
*[class~="bg-emerald-500"] { background-color: rgb(16, 185, 129); }
*[class~="bg-emerald-600"] { background-color: rgb(5, 150, 105); }
*[class~="bg-emerald-700"] { background-color: rgb(4, 120, 87); }
*[class~="bg-emerald-800"] { background-color: rgb(6, 95, 70); }
*[class~="bg-emerald-900"] { background-color: rgb(6, 78, 59); }
*[class~="bg-emerald-1000"] { background-color: rgb(2, 44, 34); }

/* Teal */
*[class~="bg-teal-50"] { background-color: rgb(240, 253, 250); }
*[class~="bg-teal-100"] { background-color: rgb(204, 251, 241); }
*[class~="bg-teal-200"] { background-color: rgb(153, 246, 228); }
*[class~="bg-teal-300"] { background-color: rgb(94, 234, 212); }
*[class~="bg-teal-400"] { background-color: rgb(45, 212, 191); }
*[class~="bg-teal-500"] { background-color: rgb(20, 184, 166); }
*[class~="bg-teal-600"] { background-color: rgb(13, 148, 136); }
*[class~="bg-teal-700"] { background-color: rgb(15, 118, 110); }
*[class~="bg-teal-800"] { background-color: rgb(17, 94, 89); }
*[class~="bg-teal-900"] { background-color: rgb(19, 78, 74); }
*[class~="bg-teal-1000"] { background-color: rgb(4, 47, 46); }

/* Cyan */
*[class~="bg-cyan-50"] { background-color: rgb(236, 254, 255); }
*[class~="bg-cyan-100"] { background-color: rgb(207, 250, 254); }
*[class~="bg-cyan-200"] { background-color: rgb(165, 243, 252); }
*[class~="bg-cyan-300"] { background-color: rgb(103, 232, 249); }
*[class~="bg-cyan-400"] { background-color: rgb(34, 211, 238); }
*[class~="bg-cyan-500"] { background-color: rgb(6, 182, 212); }
*[class~="bg-cyan-600"] { background-color: rgb(8, 145, 178); }
*[class~="bg-cyan-700"] { background-color: rgb(14, 116, 144); }
*[class~="bg-cyan-800"] { background-color: rgb(21, 94, 117); }
*[class~="bg-cyan-900"] { background-color: rgb(22, 78, 99); }
*[class~="bg-cyan-1000"] { background-color: rgb(8, 51, 68); }

/* Sky */
*[class~="bg-sky-50"] { background-color: rgb(240, 249, 255); }
*[class~="bg-sky-100"] { background-color: rgb(224, 242, 254); }
*[class~="bg-sky-200"] { background-color: rgb(186, 230, 253); }
*[class~="bg-sky-300"] { background-color: rgb(125, 211, 252); }
*[class~="bg-sky-400"] { background-color: rgb(56, 189, 248); }
*[class~="bg-sky-500"] { background-color: rgb(14, 165, 233); }
*[class~="bg-sky-600"] { background-color: rgb(2, 132, 199); }
*[class~="bg-sky-700"] { background-color: rgb(3, 105, 161); }
*[class~="bg-sky-800"] { background-color: rgb(7, 89, 133); }
*[class~="bg-sky-900"] { background-color: rgb(12, 74, 110); }
*[class~="bg-sky-1000"] { background-color: rgb(8, 47, 73); }

/* Blue */
*[class~="bg-blue-50"] { background-color: rgb(239, 246, 255); }
*[class~="bg-blue-100"] { background-color: rgb(219, 234, 254); }
*[class~="bg-blue-200"] { background-color: rgb(191, 219, 254); }
*[class~="bg-blue-300"] { background-color: rgb(147, 197, 253); }
*[class~="bg-blue-400"] { background-color: rgb(96, 165, 250); }
*[class~="bg-blue-500"] { background-color: rgb(59, 130, 246); }
*[class~="bg-blue-600"] { background-color: rgb(37, 99, 235); }
*[class~="bg-blue-700"] { background-color: rgb(29, 78, 216); }
*[class~="bg-blue-800"] { background-color: rgb(30, 64, 175); }
*[class~="bg-blue-900"] { background-color: rgb(30, 58, 138); }
*[class~="bg-blue-1000"] { background-color: rgb(23, 37, 84); }

/* Indigo */
*[class~="bg-indigo-50"] { background-color: rgb(238, 242, 255); }
*[class~="bg-indigo-100"] { background-color: rgb(224, 231, 255); }
*[class~="bg-indigo-200"] { background-color: rgb(199, 210, 254); }
*[class~="bg-indigo-300"] { background-color: rgb(165, 180, 252); }
*[class~="bg-indigo-400"] { background-color: rgb(129, 140, 248); }
*[class~="bg-indigo-500"] { background-color: rgb(99, 102, 241); }
*[class~="bg-indigo-600"] { background-color: rgb(79, 70, 229); }
*[class~="bg-indigo-700"] { background-color: rgb(67, 56, 202); }
*[class~="bg-indigo-800"] { background-color: rgb(55, 48, 163); }
*[class~="bg-indigo-900"] { background-color: rgb(49, 46, 129); }
*[class~="bg-indigo-1000"] { background-color: rgb(30, 27, 75); }

/* Violet */
*[class~="bg-violet-50"] { background-color: rgb(245, 243, 255); }
*[class~="bg-violet-100"] { background-color: rgb(237, 233, 254); }
*[class~="bg-violet-200"] { background-color: rgb(221, 214, 254); }
*[class~="bg-violet-300"] { background-color: rgb(196, 181, 253); }
*[class~="bg-violet-400"] { background-color: rgb(167, 139, 250); }
*[class~="bg-violet-500"] { background-color: rgb(139, 92, 246); }
*[class~="bg-violet-600"] { background-color: rgb(124, 58, 237); }
*[class~="bg-violet-700"] { background-color: rgb(109, 40, 217); }
*[class~="bg-violet-800"] { background-color: rgb(91, 33, 182); }
*[class~="bg-violet-900"] { background-color: rgb(76, 29, 149); }
*[class~="bg-violet-1000"] { background-color: rgb(46, 16, 101); }

/* Purple */
*[class~="bg-purple-50"] { background-color: rgb(250, 245, 255); }
*[class~="bg-purple-100"] { background-color: rgb(243, 232, 255); }
*[class~="bg-purple-200"] { background-color: rgb(233, 213, 255); }
*[class~="bg-purple-300"] { background-color: rgb(216, 180, 254); }
*[class~="bg-purple-400"] { background-color: rgb(192, 132, 252); }
*[class~="bg-purple-500"] { background-color: rgb(168, 85, 247); }
*[class~="bg-purple-600"] { background-color: rgb(147, 51, 234); }
*[class~="bg-purple-700"] { background-color: rgb(126, 34, 206); }
*[class~="bg-purple-800"] { background-color: rgb(107, 33, 168); }
*[class~="bg-purple-900"] { background-color: rgb(88, 28, 135); }
*[class~="bg-purple-1000"] { background-color: rgb(59, 7, 100); }

/* Fuchsia */
*[class~="bg-fuchsia-50"] { background-color: rgb(253, 244, 255); }
*[class~="bg-fuchsia-100"] { background-color: rgb(250, 232, 255); }
*[class~="bg-fuchsia-200"] { background-color: rgb(245, 208, 254); }
*[class~="bg-fuchsia-300"] { background-color: rgb(240, 171, 252); }
*[class~="bg-fuchsia-400"] { background-color: rgb(232, 121, 249); }
*[class~="bg-fuchsia-500"] { background-color: rgb(217, 70, 239); }
*[class~="bg-fuchsia-600"] { background-color: rgb(192, 38, 211); }
*[class~="bg-fuchsia-700"] { background-color: rgb(162, 28, 175); }
*[class~="bg-fuchsia-800"] { background-color: rgb(134, 25, 143); }
*[class~="bg-fuchsia-900"] { background-color: rgb(112, 26, 117); }
*[class~="bg-fuchsia-1000"] { background-color: rgb(74, 4, 78); }

/* Pink */
*[class~="bg-pink-50"] { background-color: rgb(253, 242, 248); }
*[class~="bg-pink-100"] { background-color: rgb(252, 231, 243); }
*[class~="bg-pink-200"] { background-color: rgb(251, 207, 232); }
*[class~="bg-pink-300"] { background-color: rgb(249, 168, 212); }
*[class~="bg-pink-400"] { background-color: rgb(244, 114, 182); }
*[class~="bg-pink-500"] { background-color: rgb(236, 72, 153); }
*[class~="bg-pink-600"] { background-color: rgb(219, 39, 119); }
*[class~="bg-pink-700"] { background-color: rgb(190, 24, 93); }
*[class~="bg-pink-800"] { background-color: rgb(157, 23, 77); }
*[class~="bg-pink-900"] { background-color: rgb(131, 24, 67); }
*[class~="bg-pink-1000"] { background-color: rgb(80, 7, 36); }

*[class~="fg-white"] { color: white; }
*[class~="fg-gray"] { color: grey; }/* Width */
*[class~="w-full"] { width: 100%; }
*[class~="w-1/2"] { width: 50%; }
*[class~="w-1/4"] { width: 25%; }
*[class~="w-0"] { width: 0px; }
*[class~="w-4"] { width: 16px; }
*[class~="w-8"] { width: 32px; }
*[class~="w-16"] { width: 64px; }
*[class~="w-32"] { width: 128px; }

/* Height */
*[class~="h-full"] { height: 100%; }
*[class~="h-0"] { height: 0px; }
*[class~="h-4"] { height: 16px; }
*[class~="h-8"] { height: 32px; }
*[class~="h-16"] { height: 64px; }
*[class~="h-32"] { height: 128px; }/* PADDING ALL (p-*) */
*[class~="p-px"] { padding: 1px; }
*[class~="p-0_5"] { padding: 2px; }
*[class~="p-1"] { padding: 4px; }
*[class~="p-2"] { padding: 8px; }
*[class~="p-3"] { padding: 12px; }
*[class~="p-4"] { padding: 16px; }
*[class~="p-5"] { padding: 20px; }
*[class~="p-6"] { padding: 24px; }
*[class~="p-8"] { padding: 32px; }
*[class~="p-10"] { padding: 40px; }
*[class~="p-12"] { padding: 48px; }
*[class~="p-16"] { padding: 64px; }

/* PADDING HORIZONTAL (px-*) -> Maps to padding-left and padding-right */
*[class~="px-px"] { padding-left: 1px; padding-right: 1px; }
*[class~="px-0_5"] { padding-left: 2px; padding-right: 2px; }
*[class~="px-1"] { padding-left: 4px; padding-right: 4px; }
*[class~="px-2"] { padding-left: 8px; padding-right: 8px; }
*[class~="px-3"] { padding-left: 12px; padding-right: 12px; }
*[class~="px-4"] { padding-left: 16px; padding-right: 16px; }
*[class~="px-5"] { padding-left: 20px; padding-right: 20px; }
*[class~="px-6"] { padding-left: 24px; padding-right: 24px; }

/* PADDING VERTICAL (py-*) -> Maps to padding-top and padding-bottom */
*[class~="py-px"] { padding-top: 1px; padding-bottom: 1px; }
*[class~="py-0_5"] { padding-top: 2px; padding-bottom: 2px; }
*[class~="py-1"] { padding-top: 4px; padding-bottom: 4px; }
*[class~="py-2"] { padding-top: 8px; padding-bottom: 8px; }
*[class~="py-3"] { padding-top: 12px; padding-bottom: 12px; }
*[class~="py-4"] { padding-top: 16px; padding-bottom: 16px; }
*[class~="py-5"] { padding-top: 20px; padding-bottom: 20px; }
*[class~="py-6"] { padding-top: 24px; padding-bottom: 24px; }

/* PADDING START/END (ps-*, pe-*) -> Mapped physically assuming LTR */
*[class~="ps-1"] { padding-left: 4px; }   
*[class~="pe-1"] { padding-right: 4px; }   
*[class~="ps-4"] { padding-left: 16px; }
*[class~="pe-4"] { padding-right: 16px; }


/* PADDING TOP/RIGHT/BOTTOM/LEFT (pt-*, pr-*, pb-*, pl-*) */
*[class~="pt-4"] { padding-top: 16px; }
*[class~="pr-4"] { padding-right: 16px; }
*[class~="pb-4"] { padding-bottom: 16px; }
*[class~="pl-4"] { padding-left: 16px; }


/* MARGIN ALL (m-*) */
*[class~="m-auto"] { margin: auto; }
*[class~="m-0"] { margin: 0; }
*[class~="m-px"] { margin: 1px; }
*[class~="-m-px"] { margin: -1px; }
*[class~="m-1"] { margin: 4px; }
*[class~="-m-1"] { margin: -4px; }
*[class~="m-2"] { margin: 8px; }
*[class~="-m-2"] { margin: -8px; }
*[class~="m-4"] { margin: 16px; }
*[class~="-m-4"] { margin: -16px; }
*[class~="m-8"] { margin: 32px; }
*[class~="-m-8"] { margin: -32px; }
*[class~="m-10"] { margin: 64px; }
*[class~="-m-10"] { margin: -64px; }

/* MARGIN HORIZONTAL (mx-*) -> Maps to margin-left and margin-right (margin-inline) */
*[class~="mx-auto"] { margin-left: auto; margin-right: auto; }
*[class~="mx-0"] { margin-left: 0; margin-right: 0; }
*[class~="mx-px"] { margin-left: 1px; margin-right: 1px; }
*[class~="mx-1"] { margin-left: 4px; margin-right: 4px; }
*[class~="-mx-1"] { margin-left: -4px; margin-right: -4px; }
*[class~="mx-4"] { margin-left: 16px; margin-right: 16px; }
*[class~="-mx-4"] { margin-left: -16px; margin-right: -16px; }

/* MARGIN VERTICAL (my-*) -> Maps to margin-top and margin-bottom (margin-block) */
*[class~="my-0"] { margin-top: 0; margin-bottom: 0; }
*[class~="my-px"] { margin-top: 1px; margin-bottom: 1px; }
*[class~="my-1"] { margin-top: 4px; margin-bottom: 4px; }
*[class~="-my-1"] { margin-top: -4px; margin-bottom: -4px; }
*[class~="my-4"] { margin-top: 16px; margin-bottom: 16px; }
*[class~="-my-4"] { margin-top: -16px; margin-bottom: -16px; }

/* MARGIN START/END (ms-*, me-*) -> Mapped physically assuming LTR */
*[class~="ms-auto"] { margin-left: auto; } /* Start -> Left */
*[class~="me-auto"] { margin-right: auto; } /* End -> Right */
*[class~="ms-1"] { margin-left: 4px; }
*[class~="me-1"] { margin-right: 4px; }
*[class~="-ms-4"] { margin-left: -16px; }
*[class~="me-4"] { margin-right: 16px; }

/* MARGIN TOP/RIGHT/BOTTOM/LEFT (mt-*, mr-*, mb-*, ml-*) */
*[class~="mt-auto"] { margin-top: auto; }
*[class~="mr-auto"] { margin-right: auto; }
*[class~="mb-auto"] { margin-bottom: auto; }
*[class~="ml-auto"] { margin-left: auto; }

*[class~="mt-4"] { margin-top: 16px; }
*[class~="-mt-4"] { margin-top: -16px; }
*[class~="mr-4"] { margin-right: 16px; }
*[class~="-mr-4"] { margin-right: -16px; }
*[class~="mb-4"] { margin-bottom: 16px; }
*[class~="-mb-4"] { margin-bottom: -16px; }
*[class~="ml-4"] { margin-left: 16px; }
*[class~="-ml-4"] { margin-left: -16px; }
"""