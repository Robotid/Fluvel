La Carpeta components/ (Componentes Personalizados) 🧩

Este directorio se convierte en el hogar de tus widgets reutilizables y compuestos. Piensa en ellos como "bloques de construcción" más complejos que los widgets básicos de Qt, pero que aún no son una "vista" o "ventana" completa.

¿Qué contendría?

    Botones especializados: Un CustomSubmitButton que ya tiene un icono, un texto predefinido y un estilo particular.

    Campos de entrada con validación: Un ValidatedLineEdit que ya incorpora lógica para mostrar errores o un formato específico.

    Grupos de widgets compuestos: Un LoginFormWidget que agrupa campos de usuario, contraseña y un botón de inicio de sesión, pero que no es una ventana completa.

    Tarjetas o paneles reutilizables: Un ProductCard que muestra la imagen, nombre y precio de un producto, diseñado para ser usado en una lista.

    Barras de navegación o de estado personalizadas: Si creas una barra de herramientas con un diseño y funcionalidad específicos que se repiten.

Beneficios de components/:

    Reutilización: Define un widget una vez y úsalo en múltiples ventanas o diálogos, asegurando consistencia.

    Encapsulación: Cada componente maneja su propia lógica interna y su disposición de widgets, manteniendo el código de las vistas más limpio.

    Mantenibilidad: Si necesitas cambiar la apariencia o el comportamiento de un ProductCard, lo haces en un solo lugar.

    Claridad de la UI: La carpeta views/ se enfoca en la composición de ventanas completas, utilizando estos componentes más pequeños.