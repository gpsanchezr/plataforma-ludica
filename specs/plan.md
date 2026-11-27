# Plan técnico

## Arquitectura

Capas: rutas, servicios, modelos y plantillas.

## Modelo de datos

```mermaid
erDiagram
    Clase ||--o{ Nino : contiene
    Actividad ||--o{ Pregunta : incluye
    Nino ||--o{ Intento : realiza
    Actividad ||--o{ Intento : registra

    Clase {
        int id PK
        string nombre
        string codigo UK
    }
    Nino {
        int id PK
        string alias
        string avatar
        int clase_id FK
    }
    Actividad {
        int id PK
        string titulo
        string descripcion
        int orden
    }
    Pregunta {
        int id PK
        string enunciado
        JSON opciones
        string respuesta_correcta
        int actividad_id FK
    }
    Intento {
        int id PK
        int nino_id FK
        int actividad_id FK
        int aciertos
        int total
        int duracion_segundos
        datetime fecha
    }
```

## Contrato de API

| Método | Ruta | Descripción | Respuesta |
| --- | --- | --- | --- |
| GET | /salud | Estado del servicio | 200 |

## Decisiones

Cada decisión importante se registra como ADR en `specs/adr/`.
