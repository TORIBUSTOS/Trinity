# ARCHITECTURE — TAUROS PRIME

> Cómo está construido el sistema

---

## Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| Backend | FastAPI (Python 3.11+) |
| Frontend | Next.js 14+ (App Router) |
| Database | SQLite vía SQLAlchemy ORM |
| Processing | Pandas |
| UI Components | TailwindCSS + Recharts |

**Principio:** Local-First. Todo corre en la máquina del usuario sin necesidad de cloud.

## Flujo de Datos

```
Usuario (CSV Upload)
  → Next.js (Dropzone / Upload)
    → FastAPI (Parser + Normalizer)
      → SQLAlchemy → SQLite (Persistencia)
        ← FastAPI (Categorizer / Cascada Engine)
          ← FastAPI (Insights / Cortex)
            → Recharts (Visualización Frontend)
```

## Modelo de Datos

### Movimiento
Entidad atómica principal. Representa una transacción bancaria normalizada.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer PK | Identificador único |
| fecha | Date | Fecha de la transacción |
| descripcion | String | Descripción original del extracto |
| monto | Float | Monto (positivo = ingreso, negativo = egreso) |
| categoria | String | Categoría de alto nivel |
| subcategoria | String | Desglose específico |
| tipo | Enum | INGRESO / EGRESO |
| balance | Float | Saldo acumulado (calculado) |
| batch_id | Integer FK | Lote de importación de origen |
| confidence_score | Float | Certeza de categorización automática (0.0–1.0) |

**Restricciones:** fecha, monto, descripcion son NOT NULL. Unicidad por (fecha, descripcion, monto) dentro de un período.

### ImportBatch
Rastrea cada importación para auditoría y reversión.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer PK | Identificador del lote |
| filename | String | Nombre del archivo CSV original |
| imported_at | DateTime | Timestamp de la carga |
| count | Integer | Transacciones procesadas exitosamente |
| bank_name | String | Entidad financiera detectada |

### CascadaRule
Reglas de negocio del motor de categorización.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer PK | Identificador de la regla |
| pattern | String | Regex o cadena de coincidencia |
| category | String | Categoría a asignar |
| subcategory | String | Subcategoría a asignar |
| weight | Integer | Prioridad (mayor peso = mayor precedencia) |
| is_active | Boolean | Estado de la regla |

### Relaciones

```
ImportBatch ||--o{ Movimiento : "origina"
CascadaRule }|..|{ Movimiento : "categoriza (lógica)"
```

## Estructura de Directorios

```
tauros-prime/
├── src/
│   ├── main.py          # Entry point FastAPI
│   ├── api.py           # Routers / endpoints
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   ├── parser.py        # Multi-bank CSV parser
│   ├── cascada.py       # Motor de categorización
│   └── database.py      # DB connection & session
├── tests/
│   ├── test_parser.py
│   ├── test_cascada.py
│   └── test_api.py
├── frontend/            # Next.js app (por definir)
├── requirements.txt
└── SPECS.md
```

## Design System (UI)

**Estética:** "Imperial Tech" — Roman Imperial + Gemini Dark.

| Token | Valor |
|-------|-------|
| Background | `#131314` (Pure Graphite) |
| Primary | `#C09891` (Imperial Gold) |
| Secondary | `#775144` (Roman Bronze) |
| Text | `#F4DBD8` (Off-White Rose) |
| Fonts | Inter (UI) + Outfit (Headers) |

**Componentes clave:** StatCard (Bento), ImperialToast, PeriodSelector global, Sidebar colapsable.

---

*Versión 1.0 — Extraída del Blueprint AG + Data Model AG — Abril 2026*
