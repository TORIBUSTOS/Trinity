# TORO PRIME: Multi-LLM Orchestration System

Refundación integrada de TORO Holdings + SANARTE sistemas.

## 📋 Documentación

- [Constitución Operativa](CONSTITUCION_OPERATIVA.md)
- [Guía Rápida](docs/QUICKSTART.md)
- [Roadmap 6 meses](docs/ROADMAP_6_MESES.md)

## 🗂️ Estructura

- `projects/` - Sistemas Prime (TAUROS, MOIRAS, ARGOS, MINOS, OIKOS)
- `skills/` - Skills de ingeniería adaptadas para Trinity ([ver pack](skills/TRINITY_SKILLS_PACK_v1.md))
- `trinity/` - Memory files + decisiones
- `integration/` - APIs + data flows
- `.github/workflows/` - CI/CD automático

## 👥 Trinity

| Rol | Agente | Responsabilidad |
|-----|--------|-----------------|
| Director | Tori (Rodrigo Bustos) | Visión estratégica |
| Product Architect | Rosario (ChatGPT) | Genera bloques negros (VISION.md) |
| CTO / Execution Engine | Claude | Arquitectura, código, decisiones técnicas, memoria Trinity |
| Heavy Execution | AG (Google Antigravity) | Implementaciones intensivas, agentes paralelos |
| Validator | Gemini | Validación cruzada |

## 🚀 Cómo empezar

**Cada agente lee SU documento de onboarding:**

| Agente | Documento | Qué encontrás |
|--------|-----------|----------------|
| Rosario | [TO_ROSARIO.md](TO_ROSARIO.md) | Tu flujo, qué skills leer, formato de VISION.md |
| Claude | [TO_CLAUDE.md](TO_CLAUDE.md) | Tu flujo, qué skills leer, qué validás, qué mantenés |
| Gemini/AG | [TO_GEMINI.md](TO_GEMINI.md) | Tu flujo, qué BN ejecutás, cómo debuggear |

Cada documento tiene pasos numerados en orden. Seguilo de arriba a abajo y al final sabés exactamente qué hacer.

## 📐 Stack Base

- **Backend:** Python 3.12+ / FastAPI
- **Frontend:** React / Next.js + TailwindCSS
- **Database:** PostgreSQL (migración desde SQL Server)
- **Infra:** GitHub Actions CI/CD
- **Deployment:** PyInstaller (desktop) / Vercel (web)
