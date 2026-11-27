# Taller 8: Actividades

## Actividad 2: Modelo de datos y conexión DB

### Objetivo
Crear el modelo de datos del MVP y la conexión con la base de datos.

### Herramienta y modelo
Copilot, modelo Auto.

### Prompt
## Rol
Actúa como desarrollador backend con experiencia en FastAPI y SQLModel.

## Objetivo
Crear el modelo de datos del MVP y la conexión con la base de datos:
1. En app/modelos/__init__.py, los modelos de tabla Clase, Nino, Actividad, Pregunta e Intento, con los campos del contrato.
2. En app/db.py, la variable motor, la función crear_tablas() y la dependencia obtener_sesion(), que entrega una sesión por petición.
3. En app/main.py, un ciclo de vida (lifespan) que llame a crear_tablas() al iniciar la aplicación.
4. En specs/plan.md, el diagrama entidad-relación en Mermaid, dentro de la sección Modelo de datos.

## Contexto
Lee AGENTS.md, specs/spec.md, specs/plan.md y app/main.py.
Contrato de datos:
- Clase: id, nombre, codigo (texto de 6 caracteres, único).
- Nino: id, alias, avatar, clase_id (clave foránea a Clase).
- Actividad: id, titulo, descripcion (texto opcional, vacío por defecto), orden (entero).
- Pregunta: id, enunciado, opciones (lista de textos), respuesta_correcta, actividad_id (clave foránea a Actividad).
- Intento: id, nino_id, actividad_id, aciertos, total, duracion_segundos, fecha (fecha y hora).

## Restricciones
- Usa exactamente los nombres de clases y campos del contrato.
- Guarda opciones en una columna JSON.
- La URL de la base de datos se lee de la variable de entorno DATABASE_URL, con el valor por defecto sqlite:///./plataforma.db.
- No agregues dependencias: sqlmodel ya está en requirements.txt.
- No crees endpoints ni modifiques las pruebas.

## Formato de salida
Antes de escribir código, muestra el plan con las rutas completas de los archivos y espera mi aprobación.

## Ejemplo
Pregunta(enunciado="¿Cuál es la capital del departamento del Atlántico?", opciones=["Barranquilla", "Cartagena", "Santa Marta"], respuesta_correcta="Barranquilla", actividad_id=1)

## Criterio de éxito
python -m pytest -v pasa todas las pruebas existentes, ruff check . no reporta errores y el comando python -c "import app.main" termina sin errores. No dejes ningún servidor en ejecución. Si después de 3 intentos no se cumple, detente y explica el problema.

### Resultado
Se definieron los cinco modelos, la conexión configurable con DATABASE_URL, la creación de tablas al iniciar la aplicación y el diagrama ER en Mermaid. Las pruebas existentes, Ruff y la importación de app.main pasaron. No se modificaron pruebas ni requirements.txt.
