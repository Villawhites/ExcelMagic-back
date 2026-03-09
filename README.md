# ✨ ExcelMagic Backend

> **Transforma tus palabras en hojas de cálculo profesionales.**

ExcelMagic es una plataforma inteligente que utiliza **IA (Gemini 1.5 Flash)** para convertir descripciones en lenguaje natural en archivos de Excel estructurados, con fórmulas automáticas, formatos profesionales y validación de datos.

---

## 🚀 Características Principales

- 🧠 **IA-Powered**: Integración directa con Google Gemini 1.5 para entender requerimientos complejos.
- 📊 **Generación Dinámica**: Crea columnas, encabezados y estilos automáticamente usando `openpyxl`.
- 🧮 **Fórmulas Inteligentes**: Sugiere e implementa fórmulas de Excel basadas en la descripción del usuario.
- ⚡ **FastAPI High-Performance**: Backend ligero, asíncrono y extremadamente rápido.
- 📑 **Gestión de Plantillas**: Sistema de historial y guardado de estructuras para reutilización.

---

## 🛠️ Stack Tecnológico

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **IA/LLM**: [Google Gemini 1.5 Flash](https://ai.google.dev/)
- **Manipulación de Excel**: [openpyxl](https://openpyxl.readthedocs.io/) & [Pandas](https://pandas.pydata.org/)
- **Base de Datos**: PostgreSQL + SQLAlchemy
- **Validación**: Pydantic v2

---

## 📋 Flujo de Trabajo

1. **Entrada**: El usuario describe su necesidad (ej: *"Necesito un control de inventario con stock actual, precio unitario y valor total"*).
2. **Procesamiento AI**: Gemini analiza la frase y genera un esquema JSON con columnas y fórmulas.
3. **Generación**: El `ExcelService` construye un archivo `.xlsx` real aplicando estilos y las fórmulas sugeridas.
4. **Descarga**: El backend entrega un enlace seguro para descargar el archivo generado.

---

## 🔧 Instalación y configuración

### 1. Clonar y preparar entorno
```bash
git clone <repo-url>
cd ExcelMagic-back
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Variables de Entorno
Crea un archivo `.env` basado en `.env.example`:
```env
DATABASE_URL=postgresql://user:password@localhost/excelmagic
GEMINI_API_KEY=tu_api_key_aqui
```

### 3. Iniciar Servidor
```bash
python main.py
```
El servidor estará disponible en `http://localhost:8000`.

---

## 📖 Documentación API

Una vez iniciado el servidor, puedes explorar la API interactiva en:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Endpoints Principales:
- `POST /api/generate`: Recibe la descripción y devuelve el ID del archivo.
- `GET /api/download/{file_id}`: Descarga el archivo generado.
- `GET /api/health`: Estado del sistema.

---

## 🛡️ Licencia
Este proyecto es parte del ecosistema DAVO. Todos los derechos reservados.
