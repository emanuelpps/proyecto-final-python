# Plataforma de Gestión de Pedidos de Delivery

## Introducción
Esta plataforma está diseñada para la gestión eficiente de pedidos de delivery.  
Utiliza **Python** con las bibliotecas **tkinter** para la interfaz de usuario y **sqlite3** para la administración de la base de datos.

## Características principales
- **Gestor de Pedidos**: Agregar, actualizar, eliminar y visualizar pedidos.
- **Interfaz gráfica**: Diseñada con tkinter para una experiencia intuitiva.
- **Base de datos integrada**: Usa SQLite para almacenar y gestionar pedidos.
- **Validaciones**: Implementadas para los campos del formulario.

## Estructura del Código

### Declaración de colores
Definidos para una paleta consistente en la interfaz:
- `bg_color`: Fondo general.
- `title_bg_color`: Fondo del título principal.
- `button_bg_color`: Fondo de los botones.
- `button_del_bg_color`: Fondo del botón de eliminación.

### Conexión a la Base de Datos
La función `create_db` establece la conexión con SQLite y crea `orders.db`.

### Creación de la Tabla
La función `orders_table` verifica y crea la tabla `orders` si no existe.

**Estructura de la tabla:**
- `id`: Identificador único (PK).
- `nombre`: Cliente.
- `telefono`: Teléfono.
- `direccion`: Dirección de entrega.
- `total`: Monto total.
- `pedido`: Descripción.
- `fecha`: Fecha del pedido.

## Validaciones
- `validate_name`: Solo letras en el nombre.
- `validate_phone`: Hasta 10 dígitos en teléfono.
- `validate_address`: No vacío.

## Formulario de Ingreso
Incluye:
- Nombre del cliente.
- Teléfono.
- Dirección.
- Monto total.
- Pedido.
- Fecha (seleccionable con un calendario).

## Tabla de Visualización
Se usa un **Treeview** con:
- Estilos personalizados para encabezado y filas.
- Opciones para seleccionar y manipular registros.

## Botones y Funciones
- **Guardar**: Agrega un nuevo pedido (`add_order`).
- **Eliminar**: Borra el pedido seleccionado (`delete_order`).
- **Actualizar**: Modifica detalles (`update_order`).

## Uso de la Plataforma

### Ingreso de pedidos
1. Complete los campos del formulario:
   - **Nombre del cliente**  
   - **Teléfono**  
   - **Dirección**  
   - **Monto total**  
   - **Pedido**  
   - **Fecha** (seleccionable mediante el calendario)  
2. Haga clic en **Guardar** para registrar el pedido en la base de datos.

### Modificación o eliminación de pedidos
1. Seleccione un pedido en la tabla de visualización.
2. Para modificarlo, edite los datos en el formulario y presione **Actualizar**.
3. Para eliminarlo, haga clic en **Eliminar**.

---

## Mejoras Futuras

Se planean las siguientes mejoras para la plataforma:

- **Exportación de datos**: Permitir la exportación a formatos como CSV o Excel.
- **Búsqueda avanzada**: Implementar un sistema de búsqueda por cliente, pedido o fecha.
- **Sistema de autenticación**: Incluir inicio de sesión con roles y permisos diferenciados.
- **Diseño gráfico mejorado**: Optimizar la interfaz para una mejor experiencia de usuario.
- **Historial de pedidos**: Implementar una sección para ver pedidos anteriores.
- **Contador de pedidos diarios**: Agregar un indicador del número de pedidos registrados en el día.
- **Dashboard de estadísticas**: Visualización de métricas clave para los usuarios.

---

## Notas Finales

Esta plataforma está diseñada para ser **escalable y adaptable** a pequeñas empresas que gestionan pedidos de delivery.  
Con futuras actualizaciones, se mejorará la usabilidad y se agregarán nuevas funcionalidades para optimizar la gestión de pedidos.
