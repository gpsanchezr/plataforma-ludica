# STATE.md

Estado del proyecto. Léalo al iniciar cada sesión de trabajo y actualícelo al cerrarla.

## Estado actual

Repositorio publicado en GitHub con el CI en verde. Página de inicio, `/salud`, `/docs` y `/api/version` funcionando en https://plataforma-ludica-r0im.onrender.com.

## Decisiones

| Fecha      | Decisión                                            | Motivo                                                                |
| ---------- | --------------------------------------------------- | --------------------------------------------------------------------- |
| 2026-11-13 | Usar la plantilla del curso con FastAPI y SQLModel  | Es el stack definido para la plataforma lúdica de cursos para niños   |
| 2026-11-13 | Implementar endpoint `/api/version` con `VERSION`   | Consultar la versión centralizada del proyecto de forma automatizada  |

## Siguiente paso

Desarrollar la lógica de negocio de la mecánica Memoria de parejas para el curso Geografía de Colombia en `app/servicios/`.