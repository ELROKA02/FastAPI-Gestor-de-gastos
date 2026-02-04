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

## 🎓 ¿Cómo funciona? (Guía para principiantes)

### 1️⃣ **El flujo general**

Cuando abres la aplicación en el navegador, ocurre esto:

```
Usuario abre index.html
        ↓
JavaScript carga (app.js)
        ↓
Se conecta al Backend (FastAPI) en http://127.0.0.1:8000
        ↓
Backend consulta MySQL
        ↓
Devuelve datos al navegador
        ↓
JavaScript pinta los datos en la web
```

### 2️⃣ **Backend (Python + FastAPI)**

**¿Qué es?** El "servidor" que guarda los datos y atiende peticiones.

**¿Cómo funciona?**

1. **database.py** → Se conecta a MySQL (la base de datos)
2. **models.py** → Define cómo se guardan los gastos (qué campos tiene cada gasto)
3. **crud.py** → Contiene las funciones para crear, leer, borrar gastos
4. **main.py** → Las "rutas" (endpoints) que el frontend llama

**Ejemplo práctico:**

Cuando haces clic en "Agregar gasto", ocurre:
- El JavaScript envía los datos al backend: `POST /gastos`
- FastAPI recibe la petición
- Llama a `crud.py` para guardar en MySQL
- Devuelve confirmación al navegador
- El JavaScript recarga la lista

### 3️⃣ **Frontend (HTML + JavaScript)**

**¿Qué es?** Lo que ves en pantalla y con lo que interactúas.

**¿Cómo funciona?**

1. **index.html** → La estructura de la página (formulario, tabla, gráficas)
2. **app.js** → La "inteligencia" que:
   - Escucha clics de botones
   - Envía datos al backend
   - Recibe respuestas
   - Actualiza la página

**Ejemplo práctico:**

```javascript
// Cuando haces clic en el botón "Eliminar"
btnEliminar.addEventListener("click", function(){
    // 1. Envía DELETE al backend
    fetch(URL_ELIMINAR, { method: "DELETE" })
    
    // 2. Espera respuesta
    .then(response => response.json())
    
    // 3. Si todo va bien, recarga la lista
    .then(data => cargarGastos())
})
```

### 4️⃣ **La base de datos (MySQL)**

**¿Qué es?** Un archivo especial que guarda todos los gastos.

**Tabla de ejemplo:**

| id | descripcion | monto | categoria | fecha |
|----|-------------|-------|-----------|-------|
| 1 | Café | 3.50 | Alimentación | 2026-02-04 |
| 2 | Gasolina | 45.00 | Transporte | 2026-02-04 |

### 5️⃣ **Paso a paso: Agregar un gasto**

1. **Llenas el formulario** (descripción, monto, categoría, fecha)
2. **Haces clic en "Agregar"**
3. **JavaScript captura el evento** (DOMContentLoaded)
4. **Recoge los datos** del formulario
5. **Los envía al backend** en formato JSON:
   ```json
   {
     "descripcion": "Café",
     "monto": 3.50,
     "categoria": "Alimentación",
     "fecha": "2026-02-04"
   }
   ```
6. **Backend recibe** la petición en `main.py`
7. **Guarda en MySQL** usando `crud.py`
8. **Devuelve confirmación** al navegador
9. **JavaScript limpia el formulario** y recarga la lista
10. **Ves el nuevo gasto** en la tabla

### 6️⃣ **Paso a paso: Ver estadísticas**

1. **Página carga** y ejecuta `cargarEstadisticas()`
2. **Llama** a `/gastos/estadisticas`
3. **Backend calcula:**
   - Total de gastos
   - Gastos por categoría
   - Gastos por mes
4. **Devuelve JSON** con los datos
5. **JavaScript pinta:**
   - Cards con totales
   - Tablas con categorías y meses
   - Gráficas (Chart.js)

### 7️⃣ **Archivos clave explicados**

**backend/main.py**
```python
@app.get("/gastos")
def obtener_gastos():
    # Obtiene todos los gastos de MySQL
    return crud.obtener_gastos()

@app.post("/gastos")
def crear_gasto(gasto: schemas.GastoCreate):
    # Crea un gasto nuevo
    return crud.crear_gasto(gasto)

@app.delete("/gastos/{id}")
def eliminar_gasto(id: int):
    # Borra un gasto por ID
    return crud.eliminar_gasto(id)
```

**frontend/app.js**
```javascript
// Carga los gastos cuando abre la página
document.addEventListener("DOMContentLoaded", cargarGastos)

// Cuando envías el formulario
formulario.addEventListener("submit", function(event) {
    // Recoge datos → Envía al backend → Recarga lista
})

// Cuando haces clic en Eliminar
btnEliminar.addEventListener("click", function() {
    // Envía DELETE → Recarga lista
})
```

### 8️⃣ **Resumen visual**

```
┌─────────────────────────────────────────────────────────┐
│                    NAVEGADOR (Frontend)                │
│  ┌──────────────────────────────────────────────────┐  │
│  │  index.html (lo que ves)                         │  │
│  │  + app.js (inteligencia)                         │  │
│  │                                                  │  │
│  │  [Formulario] [Tabla de gastos] [Gráficas]      │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────┬───────────────────────────────────────────┘
              │ HTTP (fetch)
              ↓
┌─────────────────────────────────────────────────────────┐
│                 SERVIDOR (Backend FastAPI)              │
│  ┌──────────────────────────────────────────────────┐  │
│  │  main.py (rutas)                                 │  │
│  │  crud.py (lógica)                                │  │
│  │  models.py (estructura)                          │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────┬───────────────────────────────────────────┘
              │ SQL (consultas)
              ↓
┌─────────────────────────────────────────────────────────┐
│              BASE DE DATOS (MySQL)                      │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Tabla: gastos                                   │  │
│  │  [id, descripcion, monto, categoria, fecha]      │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

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