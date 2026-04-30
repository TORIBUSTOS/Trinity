# TRINITY: DECISIONES TOMADAS

> Registro inmutable. Solo se agregan entradas, nunca se borran.

---

## 2026-04-13

### DEC-001: Orquestador = GitHub
- **Decidido por:** Tori + Claude
- **Elegido:** GitHub (repos + PRs + Actions)
- **Descartado:** n8n (over-engineering para esta etapa)
- **Razón:** Más simple, más confiable, sin herramientas externas adicionales
- **Trade-off:** Automatización manual inteligente vs automático puro

### DEC-002: Stack Base
- **Decidido por:** Tori + Claude
- **Python:** 3.12+
- **Backend:** FastAPI
- **Database:** PostgreSQL (migración desde SQL Server)
- **Frontend:** React / Next.js + TailwindCSS
- **Razón:** Moderno, sin EOL próximo, escalable, ecosistema maduro

### DEC-003: Pipeline de documentación
- **Decidido por:** Trinity
- **Flujo:** VISION.md → MISSION.md → ARCHITECTURE.md → SPECS.md → Código
- **Razón:** Lección directa del fracaso de HILE (código sin specs = rework infinito)

---

## 2026-04-30

### DEC-004: MINOS Broker-Grade Valuation Core
- **Decidido por:** Tori + Rosario
- **Problema:** MINOS presentaba valuaciones inconsistentes contra broker (Balanz) y mostraba menos información financiera relevante.
- **Diagnóstico:** Uso incorrecto de tickers (ADR vs BYMA), ambigüedad de instrumento, pricing no trazable y modelo financiero incompleto.
- **Decisión:** Reordenar prioridades del sistema.

Nuevo orden:

1. Verdad financiera (valuación correcta)
2. Visualización (tabla tipo broker)
3. Inteligencia (señales BUY/HOLD/SELL)

- **Arquitectura adoptada:**

```text
Position -> Instrument -> PricingEngine -> Quote -> ValuationEngine -> Portfolio
```

- **Regla crítica:** Ninguna señal es válida si `valuation_status != OK`.
- **Regla de pricing:** No usar tickers ambiguos. BYMA debe resolverse explícitamente (ej: BMA.BA, YPFD.BA).
- **Regla de fallback:** Prohibido usar `price = 0` como fallback silencioso.

- **Consecuencia:** Sprint 2 se dedica exclusivamente a lograr paridad con broker antes de cualquier mejora de inteligencia.

---
