# PandaTaT API

Sistema backend para gestión de pedidos del área de ventas TaT usando FastAPI y MySQL.

## Estructura del Proyecto

- MVC con FastAPI
- Conexión MySQL (`mysql.connector`)
- Endpoints por tipo de pedido
- Control de acceso basado en roles

## Cómo iniciar

1. Clonar el repositorio
2. Crear la base de datos con el script SQL proporcionado
3. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```
4. Ejecutar el servidor:
   ```
   uvicorn app.main:app --reload
   ```
