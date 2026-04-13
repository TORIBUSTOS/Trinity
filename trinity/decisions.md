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
