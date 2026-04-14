# MISSION — TAUROS PRIME

> Qué construimos y cuál es el alcance funcional

---

## Objetivo

Construir un sistema web local-first que permita a TORO Holdings importar, categorizar, analizar y proyectar sus flujos financieros desde múltiples fuentes bancarias, con mínima intervención manual.

## Módulos del Sistema

### BN-001 / BN-002 — Ingesta & Normalización
- Parser multi-banco: procesa CSVs de Galicia, ICBC, Santander y otros
- Batch Management: control de lotes para evitar duplicados
- Normalización de fechas, montos y descripciones a formato estándar

### BN-003 — Motor de Categorización (Cascada)
- Clasificación automática por expresiones regulares y patrones
- Jerarquía Categoría > Subcategoría
- Confidence Scoring por movimiento (0.0 a 1.0)
- Permite al usuario crear reglas nuevas desde un movimiento mal categorizado

### BN-006 / BN-007 — Reportes & Analytics
- P&L Jerárquico: tabla colapsable por categoría/subcategoría con drill-down
- Dashboard Bento: KPIs principales (Caja, Burn Rate, Runway, Balance)
- Hormone Analysis: distribución visual de flujos por categorías críticas
- Filtro de período global sincronizado en todas las vistas

### BN-008 — Inteligencia Predictiva (Cortex)
- Forecast Engine: proyección de saldos a 3 meses basado en histórico
- Insight Feed: alertas automáticas sobre anomalías, fugas de capital y patrones de gasto

## Flujos de Usuario Críticos

### Ingesta (Happy Path)
1. Usuario sube CSV al Dropzone en el Sidebar
2. Frontend muestra progreso de subida
3. Backend parsea, normaliza, categoriza y devuelve el ImportBatch
4. Toast de éxito + Dashboard se actualiza automáticamente

### Categorización Manual
1. Usuario identifica movimiento con confidence_score bajo en la tabla
2. Cambia la categoría manualmente
3. Sistema ofrece crear una CascadaRule para automatizarlo a futuro

## Alcance MVP

**Incluye:**
- Importación de CSVs bancarios (Galicia, ICBC, Santander mínimo)
- Categorización automática via Cascada
- Dashboard ejecutivo con KPIs básicos
- P&L Jerárquico
- Gestión de movimientos (edición de categorías)

**Fuera de alcance MVP:**
- Cortex / Forecast (post-MVP)
- Conexión directa a APIs bancarias
- Multi-usuario / autenticación
- Deploy en cloud (local-first primero)

---

*Versión 1.0 — Extraída del Blueprint AG — Abril 2026*
