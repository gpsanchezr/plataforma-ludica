# Plan técnico

## Arquitectura

Capas: rutas, servicios, modelos y plantillas.

## Modelo de datos

```mermaid
erDiagram
    CLASE ||--o{ NINO : contiene
    ACTIVIDAD ||--o{ PREGUNTA : incluye
    NINO ||--o{ INTENTO : realiza
    ACTIVIDAD ||--o{ INTENTO : registra

    CLASE {
        int id PK
        string nombre
        string codigo UK
    }
    NINO {
        int id PK
        string alias
        string avatar
        int clase_id FK
    }
    ACTIVIDAD {
        int id PK
        string titulo
        string descripcion
        int orden
    }
    PREGUNTA {
        int id PK
        string enunciado
        JSON opciones
        string respuesta_correcta
        int actividad_id FK
    }
    INTENTO {
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
