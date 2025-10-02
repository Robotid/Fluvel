COMPACT_BOOTSTRAP = """
/*
 * bootstrap_modern_theme.qss
 *
 * Un tema QSS inspirado en Bootstrap, mejorado con una estética moderna y limpia.
 * Paleta de colores principal:
 * - Azul Primario: #0078D4
 * - Fondo Principal: #FFFFFF
 * - Fondo de Widgets: #f1f3f5
 * - Texto Principal: #212529
 * - Bordes: #dee2e6
 */

/* ==================== Estilos Generales / Root ==================== */
* {
    font-family: "Segoe UI", "Helvetica Neue", "Arial", sans-serif;
    font-size: 14px;
    color: #212529;
}

QMainWindow {
    background-color: #FFFFFF;
}

/* ==================== Inputs (QLineEdit, QTextEdit) ==================== */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #FFFFFF;
    border: 1px solid #dee2e6;
    border-radius: 5px;
    padding: 8px 12px;
    selection-background-color: #0078D4;
    selection-color: #FFFFFF;
}

QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border-color: #0078D4;
    outline: 0;
}

/* ==================== ComboBox (Menú desplegable) ==================== */
QComboBox {
    background-color: #FFFFFF;
    border: 1px solid #dee2e6;
    border-radius: 5px;
    padding: 7px 12px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 25px;
    border-left: 1px solid #dee2e6;
}

QComboBox::down-arrow {
    image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgZmlsbD0iIzIxMjUyOSIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xLjY0NiA0LjY0NmEuNS41IDAgMCAxIC43MDggMGw1LjY0NiA1LjY0N2w1LjY0Ny01LjY0N2EuNS41IDAgMCAxIC43MDguNzA4bC02IDZhLjUuNSAwIDAgMS0uNzA4IDBsLTYtNmEuNS41IDAgMCAxIDAtLjcwOHoiLz48L3N2Zz4=);
    width: 12px;
    height: 12px;
}

QComboBox QAbstractItemView {
    border: 1px solid #dee2e6;
    background-color: #FFFFFF;
    selection-background-color: #0078D4;
    selection-color: #FFFFFF;
    outline: 0;
}

/* ==================== CheckBox y RadioButton ==================== */
QCheckBox, QRadioButton {
    spacing: 8px;
}

QCheckBox::indicator, QRadioButton::indicator {
    width: 18px;
    height: 18px;
    background-color: #FFFFFF;
    border: 1px solid #adb5bd;
}
QCheckBox::indicator { border-radius: 4px; }
QRadioButton::indicator { border-radius: 9px; }

QCheckBox::indicator:hover, QRadioButton::indicator:hover {
    border-color: #0078D4;
}

QCheckBox::indicator:checked, QRadioButton::indicator:checked {
    background-color: #0078D4;
    border-color: #0078D4;
}

QCheckBox::indicator:checked {
    image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMiIgaGVpZ2h0PSIxMiIgZmlsbD0id2hpdGUiIHZpZXdCb3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTEzLjg1NCAzLjY0NmEuNS41IDAgMCAxIDAgLjcwOGwtNyA3YS41LjUgMCAwIDEtLjcwOCAwbC0zLjUtMy41YS41LjUgMCAxIDEgLjcwOC0uNzA4TDYuNSA MTAuMjkybDYuNjQ2LTYuNjQ3YS41LjUgMCAwIDEgLjcwOCAweiIvPjwvc3ZnPg==);
}

QRadioButton::indicator:checked {
    image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4IgaGVpZ2h0PSI4IiBmaWxsPSJ3aGl0ZSIgdmlld0JveD0iMCAwIDE2IDE2Ij48Y2lyY2xlIGN4PSI4IiBjeT0iOCIgcj0iOCIvPjwvc3ZnPg==);
}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled {
    background-color: #e9ecef;
    border-color: #dee2e6;
}

/* ==================== Botones (QPushButton) ==================== */

QPushButton {
    /* Estilos base del Label */
    background-color: #007bff;
    color: #fff;
    font-size: 14px;
    font-weight: 700; 
    text-align: center; 
    border: 1px solid #007bff;
    border-radius: 4px;
    padding: 8px 16px; 
    outline: none;
}

QPushButton:hover {
    background-color: #0071eb;
    border-color: #0071eb;
}

QPushButton:pressed {
    padding-bottom: 6px;
    background-color: #0068d6;
    border-color: #0068d6;
}

QPushButton:disabled {
    /* Estilos para el botón deshabilitado */
    background-color: #e9ecef; 
    color: #6c757d;
    border: 1px solid #ced4da; 
}


/* Estilo para un primary Button */

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
    
/* Estilo para un secondary Button */

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
    
/* Estilo para un info Button */

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
    
/* Estilo para un success Button */

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
    
/* Estilo para un warning Button */

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
    
/* Estilo para un danger Button */

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
    
/* Estilo para un dark Button */

QPushButton[class~="dark"] {
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
    
/* Estilo para un light Button */

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
}

/* ==================== Pestañas (QTabWidget) ==================== */
QTabWidget::pane {
    border: 1px solid #dee2e6;
    border-radius: 5px;
}
QTabBar::tab {
    background: transparent;
    color: #6c757d;
    border: none;
    padding: 10px 15px;
    border-bottom: 2px solid transparent;
}
QTabBar::tab:hover {
    color: #212529;
}
QTabBar::tab:selected {
    color: #0078D4;
    font-weight: 600;
    border-bottom: 2px solid #0078D4;
}

/* ==================== Barras de Herramientas, Menús y Tooltips ==================== */
QMenuBar, QToolBar {
    background-color: #f1f3f5;
    padding: 6px;
    border-bottom: 1px solid #dee2e6;
}
QMenuBar::item {
    padding: 6px 12px;
    background-color: transparent;
    border-radius: 4px;
}
QMenuBar::item:selected {
    background-color: #0078D4;
    color: #FFFFFF;
}
QMenu {
    background-color: #FFFFFF;
    border: 1px solid #dee2e6;
    border-radius: 5px;
    padding: 5px;
}
QMenu::item {
    padding: 8px 20px;
    border-radius: 4px;
}
QMenu::item:selected {
    background-color: #0078D4;
    color: #FFFFFF;
}
QMenu::separator {
    height: 1px;
    background: #f1f3f5;
    margin: 5px;
}
QToolButton {
    background-color: transparent;
    border: 1px solid transparent;
    border-radius: 5px;
    padding: 6px;
}
QToolButton:hover {
    background-color: #e2e6ea;
    border: 1px solid #dee2e6;
}
QToolButton:checked {
    background-color: #dbeafe;
    border: 1px solid #0078D4;
    color: #0078D4;
}
QToolTip {
    background-color: #212529;
    color: #FFFFFF;
    border: none;
    border-radius: 4px;
    padding: 5px 8px;
}

/* ==================== Sliders, Barras de Progreso y ScrollBars ==================== */
QSlider::groove:horizontal {
    height: 6px; background: #e9ecef; border-radius: 3px;
}
QSlider::handle:horizontal {
    background: #0078D4; width: 18px; margin: -6px 0; border-radius: 9px;
}
QProgressBar {
    border: none; border-radius: 5px; text-align: center; background-color: #e9ecef; color: #212529; height: 20px;
}
QProgressBar::chunk {
    background-color: #0078D4; border-radius: 5px;
}
QScrollBar:vertical, QScrollBar:horizontal {
    border: none; background: #f1f3f5; width: 10px; margin: 0;
}
QScrollBar::handle {
    background: #ced4da; border-radius: 5px;
}
QScrollBar::handle:hover {
    background: #adb5bd;
}
QScrollBar::add-line, QScrollBar::sub-line, QScrollBar::add-page, QScrollBar::sub-page {
    height: 0; width: 0; background: none;
}

/* ==================== Alertas y Tarjetas ==================== */
QLabel[class~="info"], QLabel[class~="success"], QLabel[class~="warning"], QLabel[class~="danger"] {
    padding: 10px 15px;
    border-radius: 5px;
    border-left: 4px solid;
}
QLabel[class~="info"] {
    background-color: #dbeafe; border-color: #60a5fa; color: #3b82f6;
}
QLabel[class~="success"] {
    background-color: #dcfce7; border-color: #4ade80; color: #16a34a;
}
QLabel[class~="warning"] {
    background-color: #fef3c7; border-color: #facc15; color: #ca8a04;
}
QLabel[class~="danger"] {
    background-color: #fee2e2; border-color: #f87171; color: #dc2626;
}

/* --- Estilos para tarjetas de alerta --- */
*[type="card-container"] {
    border-radius: 5px;
    border-bottom: 4px solid;
}
*[type="card-description"] {
    color: #FFFFFF;
    background: none;
    border: none;
    font-weight: 500;
}
QFrame#InfoCard { background-color: #3b82f6; border-color: #2563eb; }
QFrame#WarningCard { background-color: #f59e0b; border-color: #d97706; }
QFrame#DangerCard { background-color: #ef4444; border-color: #dc2626; }
QFrame#SuccessCard { background-color: #22c55e; border-color: #16a34a; }

/* ==================== Clases de Utilidad ==================== */
/* Size */
*[class~="h1"] { font-size: 24pt; }
*[class~="h2"] { font-size: 18pt; }
*[class~="h3"] { font-size: 13.5pt; }
*[class~="h4"] { font-size: 12pt; }
*[class~="h5"] { font-size: 10.5pt; }
*[class~="h6"] { font-size: 9pt; }
*[class~="h7"] { font-size: 7.5pt; }
*[class~="bold"] { font-weight: bold; }
*[class~="italic"] { font-style: italic; }
/* Weight */
*[class~="w-100"] { font-weight: 100; }
*[class~="w-200"] { font-weight: 200; }
*[class~="w-300"] { font-weight: 300; }
*[class~="w-400"] { font-weight: 400; }
*[class~="w-500"] { font-weight: 500; }
*[class~="w-600"] { font-weight: 600; }
*[class~="w-700"] { font-weight: 600; }
*[class~="bold"]{ font-weight: bold; }
*[class~="italic"]{ font-style: italic; }
"""