# INTEGRACIÓN: DATA FLOWS

> Cómo fluye la data entre sistemas Prime.

---

## Flujo Principal (Planificado)

```
Bancos (extractos)
  → TAUROS (clasificación automática)
    → MOIRAS (obligaciones detectadas)
    → MINOS (cobranzas pendientes)
    → ARGOS (oportunidades de inversión)
  → OIKOS (vista operativa consolidada)
```

## Fuentes de Datos Actuales

- **SQL Server** — 200+ tablas (SANARTE operativo)
- **Extractos bancarios** — PDF/CSV procesados mensualmente
- **Sistema de clasificación** — Cascada Concepto → Detalle (99%+ cobertura)

## Migración Planificada

- SQL Server → PostgreSQL (schemas separados por sistema)
- Procesamiento batch → API real-time donde aplique
- Excel manual → Dashboards automatizados

---
