# Gestor de Gastos - FastAPI

Aplicación web para gestionar y analizar gastos personales. Proyecto desarrollado como prueba técnica para estudios de grado.

## 📋 Descripción

Sistema completo de gestión de gastos con:
- **Backend**: API REST con FastAPI y MySQL
- **Frontend**: Interfaz web con JavaScript vanilla
- Visualización de gastos por categoría y mes
- Gráficas interactivas (Chart.js)
- CRUD completo: crear, leer, actualizar y eliminar gastos

## 🛠️ Tecnologías

**Backend:**
- FastAPI
- SQLAlchemy (ORM)
- MySQL
- Uvicorn

**Frontend:**
- HTML5 / CSS (Bootstrap)
- JavaScript vanilla
- Chart.js (gráficas)

## 📦 Instalación

### 1. Clonar el repositorio
```bash
git clone <tu-repo>
cd Proyecto_Fastapi
```

### 2. Configurar variables de entorno
```bash
cp .env.example .env
```
Edita `.env` con tus credenciales MySQL:
```
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=3306
DB_NAME=tu_base_datos
```

### 3. Instalar dependencias Python
```bash
pip install -r requirements.txt
```

### 4. Crear base de datos
```bash
mysql -u tu_usuario -p < database.sql
```
*(Crea el archivo `database.sql` con tus tablas)*

## 🚀 Ejecutar

### Backend
```bash
cd backend
uvicorn main:app --reload
```
La API estará en: `http://127.0.0.1:8000`

### Frontend
Abre `frontend/index.html` en tu navegador (o usa un servidor local).

## 📂 Estructura del Proyecto

```
Proyecto_Fastapi/
├── backend/
│   ├── main.py           # Rutas API
│   ├── models.py         # Modelos SQLAlchemy
│   ├── schemas.py        # Esquemas Pydantic
│   ├── crud.py           # Lógica de datos
│   └── database.py       # Conexión MySQL
├── frontend/
│   ├── index.html        # Interfaz
│   └── js/
│       └── app.js        # Lógica JavaScript
├── requirements.txt
├── .env.example
└── README.md
```

## 🔌 Endpoints API

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/gastos` | Obtener todos los gastos |
| POST | `/gastos` | Crear nuevo gasto |
| DELETE | `/gastos/{id}` | Eliminar gasto |
| GET | `/gastos/estadisticas` | Obtener estadísticas |

## 📊 Características

- ✅ Registrar gastos con descripción, monto, categoría y fecha
- ✅ Visualizar lista completa de gastos
- ✅ Eliminar gastos
- ✅ Estadísticas totales y por categoría
- ✅ Gráficas de gastos por mes y categoría
- ✅ Gestión de errores

## ⚙️ Requisitos

- Python 3.9+
- MySQL 5.7+
- Navegador moderno

## 📝 Notas

Este proyecto fue desarrollado como prueba técnica educativa para demonstrar:
- Desarrollo de APIs REST
- Gestión de bases de datos
- Integración frontend-backend
- Visualización de datos

## 👤 Autor

Samuel - Proyecto de grado

---

**Última actualización:** 4 de febrero de 2026