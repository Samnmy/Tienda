# Inventory Management System

Este proyecto tiene como objetivo gestionar un inventario de productos, permitiendo realizar operaciones como agregar, buscar, actualizar, eliminar productos y generar informes relacionados con el inventario. Es útil para empresas que necesiten llevar un control detallado de su inventario de productos.

## Funcionalidades

El sistema ofrece las siguientes funcionalidades clave:

1. **Agregar un producto**: Permite agregar nuevos productos al inventario, incluyendo detalles como nombre, categoría, proveedor, cantidad y precio unitario.
   
2. **Buscar un producto**: Permite buscar productos por nombre o categoría. La búsqueda es insensible a mayúsculas/minúsculas.

3. **Actualizar un producto**: Permite actualizar la cantidad o el precio unitario de un producto ya existente en el inventario.

4. **Eliminar un producto**: Elimina un producto del inventario si su cantidad es cero, después de confirmar la acción.

5. **Generar informes**: Genera un informe con el valor total por categoría y los productos cuyo stock sea inferior a un umbral (5 unidades).

6. **Menú interactivo**: Ofrece una interfaz de usuario interactiva que permite a los usuarios realizar diversas operaciones en el sistema de inventario.

## Cómo funciona

El sistema mantiene una lista de diccionarios (`inventory`), donde cada diccionario contiene los detalles de un producto. Cada producto tiene los siguientes atributos:

- **name**: Nombre del producto.
- **category**: Categoría del producto (por ejemplo, Electrónica, Ropa, Electrodomésticos).
- **supplier**: Proveedor del producto.
- **quantity**: Cantidad disponible en el inventario.
- **unit_price**: Precio unitario del producto.

Las funciones principales del sistema permiten:

- **preload_inventory**: Inicializa el inventario con algunos productos predeterminados.
  
- **add_product**: Añade un nuevo producto al inventario, validando que la cantidad y el precio sean positivos.

- **search_product**: Permite buscar productos por nombre o categoría.

- **update_product**: Permite actualizar la cantidad o el precio unitario de un producto específico.

- **delete_product**: Elimina un producto si su cantidad es cero.

- **generate_reports**: Genera un informe con el valor total de los productos por categoría y una lista de los productos con un stock inferior a 5 unidades.

- **menu**: Muestra un menú interactivo para que el usuario seleccione una acción.

## Uso

### Requisitos

Este proyecto requiere Python 3.x para ejecutarse correctamente.

### Ejecución

1. Clona o descarga este repositorio.
2. Ejecuta el archivo `inventory_management.py` en tu terminal o entorno de desarrollo Python.
3. El sistema mostrará un menú interactivo en la consola donde podrás elegir entre las diferentes opciones para gestionar el inventario.

### Ejemplo de flujo

1. **Agregar un producto**:
   - El usuario ingresa los detalles del producto (nombre, categoría, proveedor, cantidad y precio unitario) y el producto se añade al inventario.
   
2. **Buscar un producto**:
   - El usuario puede buscar productos por nombre o categoría, y se mostrarán los resultados coincidentes.
   
3. **Actualizar un producto**:
   - El usuario puede actualizar la cantidad o el precio de un producto específico en el inventario.

4. **Eliminar un producto**:
   - El usuario puede eliminar un producto si su cantidad es cero, después de confirmar la acción.

5. **Generar informes**:
   - El sistema muestra el valor total por categoría y una lista de los productos con stock inferior a 5 unidades.

## Objetivo

El objetivo de este proyecto es proporcionar una solución sencilla y eficaz para gestionar el inventario de productos. Permite a las empresas realizar un seguimiento del estado de su inventario, asegurándose de que siempre haya un control adecuado sobre los productos y los valores asociados a cada categoría.

## Contribuciones

Si deseas contribuir al proyecto, puedes hacer un fork y enviar un pull request. Las mejoras y sugerencias son siempre bienvenidas.
