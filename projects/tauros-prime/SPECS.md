# SPECS — TAUROS PRIME

> Especificaciones técnicas detalladas para implementación

---

## API Endpoints (FastAPI)

### Health
```
GET /health
Response: { "status": "ok", "system": "tauros-prime" }
```

### Ingesta
```
POST /api/import
Content-Type: multipart/form-data
Body: file (CSV), bank_name (string)
Response: ImportBatchSchema
Lógica: Detectar banco, parsear CSV, normalizar, deduplicar, aplicar Cascada, persistir
```

```
GET /api/imports
Response: List[ImportBatchSchema]
```

```
DELETE /api/imports/{batch_id}
Response: { "deleted": batch_id }
Lógica: Eliminar batch y todos los movimientos asociados (soft delete opcional)
```

### Movimientos
```
GET /api/movimientos
Query params: categoria, subcategoria, banco, fecha_desde, fecha_hasta, page, page_size
Response: PaginatedMovimientosSchema

PATCH /api/movimientos/{id}
Body: { "categoria": str, "subcategoria": str }
Response: MovimientoSchema
Lógica: Actualizar categoría y recalcular confidence_score a 1.0 (manual = certeza total)
```

### Cascada Rules
```
GET /api/cascada/rules
Response: List[CascadaRuleSchema]

POST /api/cascada/rules
Body: { "pattern": str, "category": str, "subcategory": str, "weight": int }
Response: CascadaRuleSchema

PUT /api/cascada/rules/{id}
Body: CascadaRuleSchema (parcial)
Response: CascadaRuleSchema

DELETE /api/cascada/rules/{id}
Response: { "deleted": id }

POST /api/cascada/apply
Lógica: Re-aplica todas las reglas activas sobre movimientos sin categoría o con confidence < 0.5
Response: { "updated": int }
```

### Reportes
```
GET /api/reportes/pnl
Query params: fecha_desde, fecha_hasta
Response: PnLSchema (árbol jerárquico categoria > subcategoria > movimientos)

GET /api/reportes/kpis
Query params: fecha_desde, fecha_hasta
Response: { "caja": float, "burn_rate": float, "runway_meses": float, "total_ingresos": float, "total_egresos": float }
```

---

## Pydantic Schemas

```python
class MovimientoSchema(BaseModel):
    id: int
    fecha: date
    descripcion: str
    monto: float
    categoria: Optional[str]
    subcategoria: Optional[str]
    tipo: Literal["INGRESO", "EGRESO"]
    balance: Optional[float]
    batch_id: int
    confidence_score: float

class ImportBatchSchema(BaseModel):
    id: int
    filename: str
    imported_at: datetime
    count: int
    bank_name: str

class CascadaRuleSchema(BaseModel):
    id: int
    pattern: str
    category: str
    subcategory: str
    weight: int
    is_active: bool
```

---

## Lógica de Negocio Crítica

### Parser Multi-Banco
- Detectar banco por nombre de archivo o columnas presentes
- Bancos soportados MVP: Galicia, ICBC, Santander
- Normalización: fecha → YYYY-MM-DD, monto → float (negativos = egresos)
- Deduplicación: hash(fecha + descripcion + monto) por batch

### Motor Cascada
1. Cargar todas las CascadaRule activas, ordenadas por weight DESC
2. Para cada Movimiento sin categoría (o confidence < umbral):
   - Iterar reglas en orden de peso
   - Si pattern hace match en descripcion (case-insensitive): asignar categoria/subcategoria, confidence = min(1.0, weight/100)
   - Break al primer match exitoso
3. Movimientos sin ningún match: categoria = "SIN CLASIFICAR", confidence = 0.0

### Cálculo KPIs
- **Caja:** último balance disponible
- **Burn Rate:** promedio de egresos de los últimos 3 meses
- **Runway:** Caja / Burn Rate (en meses)

---

## Reglas de Validación

- monto != 0 siempre
- fecha no puede ser futura
- pattern en CascadaRule debe ser regex válido (validar antes de persistir)
- weight: integer entre 1 y 1000
- confidence_score: float entre 0.0 y 1.0

---

## Tests Requeridos (MVP)

| Test | Tipo |
|------|------|
| Parser Galicia CSV → movimientos normalizados | Unit |
| Parser ICBC CSV → movimientos normalizados | Unit |
| Cascada: regla de mayor peso gana | Unit |
| Cascada: movimiento sin match → SIN CLASIFICAR | Unit |
| POST /api/import → batch creado + movimientos | Integration |
| GET /api/reportes/kpis → valores correctos | Integration |
| Deduplicación: mismo CSV dos veces → sin duplicados | Integration |

---

*Versión 1.0 — Generada desde Blueprint AG + Data Model AG — Abril 2026*
