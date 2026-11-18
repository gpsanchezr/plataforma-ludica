# Registro de Prompts - Semana 2 (Mini-App: Registro de Gastos)

## Versión A (Prompt de una línea)
- **Herramienta y modelo:** Copilot en VS Code (GPT-6 Luna, modo Interactive).
- **Prompt exacto:** `Haz una app web para registrar gastos con FastAPI.`
- **Resultado:** Creó una app en `main.py` con base de datos SQLite y rutas en inglés (`/expenses`), cumpliendo solo 1 de 5 requisitos del Anexo E y fallando las pruebas de aceptación.

## Versión B (Prompt estructurado de 7 partes)
- **Herramienta y modelo:** Copilot en VS Code (GPT-6 Luna, modo Interactive + `AGENTS.md`).
- **Prompt exacto (7 partes):**
  - **Rol:** Actúa como desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con pytest.
  - **Objetivo:** Construir la mini-aplicación web Registro de gastos con los 5 requisitos del Anexo E (`GET /`, `POST /api/gastos`, categorías `comida`, `transporte`, `estudio`, `otros`, `GET /api/gastos`, `GET /api/gastos/resumen`).
  - **Contexto:** Lee `AGENTS.md`. El contrato de la API está en `tests/test_aceptacion.py`.
  - **Restricciones:** Usa solo dependencias de `requirements.txt`, define rutas en `app/main.py` y lógica en `app/servicios.py`, guarda datos en memoria y no modifiques `tests/test_aceptacion.py`.
  - **Formato de salida:** Antes de escribir código, muestra el plan con las rutas completas y espera mi aprobación.
  - **Ejemplo:** `POST /api/gastos` con `{"descripcion": "Almuerzo", "valor": 15000, "categoria": "comida"}` responde 201.
  - **Criterio de éxito:** `python -m pytest -v` pasa todas las pruebas y `ruff check .` no reporta errores.
- **Resultado:** El agente presentó el plan, respetó el contrato y aprobó las 7 pruebas de aceptación y Ruff sin errores.

## Mejora (Eliminar gasto - DELETE /api/gastos/{id})
- **Herramienta y modelo:** Copilot en VS Code (GPT-6 Luna, modo Interactive).
- **Prompt exacto (7 partes):**
  - **Rol:** Desarrollador backend con experiencia en FastAPI, Jinja2 y pruebas con pytest.
  - **Objetivo:** Crear `DELETE /api/gastos/{id}` (204 si elimina, 404 si no existe), actualizar resumen, añadir botón en la interfaz y crear `tests/test_mejora.py`.
  - **Contexto:** Lee `AGENTS.md`, `app/main.py` y `app/servicios.py` sin tocar `tests/test_aceptacion.py`.
  - **Restricciones:** No modificar `tests/test_aceptacion.py`, mantener arquitectura modular y dependencias actuales.
  - **Formato de salida:** Mostrar el plan con rutas completas (incluyendo `tests/test_mejora.py`) y esperar aprobación.
  - **Ejemplo:** `DELETE /api/gastos/1` responde 204; `DELETE /api/gastos/9999` responde 404.
  - **Criterio de éxito:** `pytest` pasa las 9 pruebas (aceptación + mejora) y `ruff check .` limpio.
- **Resultado:** Funcionalidad implementada y verificada con 9/9 pruebas pasando en verde.