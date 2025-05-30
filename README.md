# PandaTaT API

Sistema backend para gestión de pedidos del área de ventas TaT usando FastAPI y MySQL.

## Estructura del Proyecto

- MVC con FastAPI
- Conexión MySQL (`mysql.connector`)
- Endpoints 
- Control de acceso basado en roles

## Cómo iniciar

1. Creacion del repositorio
2. Crear la base de datos 
3. Instalar las depedencias para poder ejecutar el proyecto:
   ```
   pip install -r requirements.txt
   ```
4. Ejecutar el servidor para validar la funcionalidad:
   ```
   uvicorn app.main:app --reload
   ```
