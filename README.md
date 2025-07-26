# Backend Gestión Educativa

Este proyecto es un backend modular para un sistema de gestión educativa, desarrollado con Django REST Framework.

## Características principales
- Arquitectura modular: apps para estudiantes, docentes, calificaciones, planes, matrículas y reportes.
- Autenticación por token (DRF Token Auth).
- Documentación Swagger disponible en `/swagger/`.
- Base de datos SQLite por defecto.
- Endpoints protegidos (excepto login y registro).
- Servicios: récord académico, comprobante de matrícula, promedio de calificaciones.

## Instalación y uso
1. Clona el repositorio y entra a la carpeta del proyecto.
2. Activa el entorno virtual:
   ```
   .\venv\Scripts\activate
   ```
3. Instala dependencias (si es necesario):
   ```
   pip install -r requirements.txt
   ```
4. Aplica migraciones:
   ```
   python manage.py migrate
   ```
5. Crea superusuarios (ya hay 3 creados: admin1, admin2, admin3).
6. Corre el servidor:
   ```
   python manage.py runserver
   ```
7. Accede a la documentación Swagger en: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

## Endpoints principales
- `/api/estudiantes/`
- `/api/docentes/`
- `/api/asignaturas/`
- `/api/planes/`
- `/api/calificaciones/`
- `/api/matriculas/`
- `/api/reportes/`

## Notas
- Todos los endpoints requieren autenticación por token.
- Puedes obtener un token usando el endpoint `/api-token-auth/` (si lo habilitas en urls).
- Incluye datos de prueba y 3 superusuarios para pruebas.

---
Entrega universitaria - Ingeniería de Software
