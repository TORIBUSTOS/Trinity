# TORO PRIME: Multi-LLM Orchestration System

Refundación integrada de TORO Holdings + SANARTE sistemas.

## 📋 Documentación

- [Constitución Operativa](CONSTITUCION_OPERATIVA.md)
- [Guía Rápida](docs/QUICKSTART.md)
- [Roadmap 6 meses](docs/ROADMAP_6_MESES.md)
- [Onboarding MINI](TO_MINI.md)
- [Protocolo MINI BN TRAIN](docs/MINI_BN_TRAIN.md)

## 🗂️ Estructura

- `projects/` - Sistemas Prime (TAUROS, MOIRAS, ARGOS, MINOS, OIKOS)
- `skills/` - Skills de ingeniería adaptadas para Trinity ([ver pack](skills/TRINITY_SKILLS_PACK_v1.md))
- `trinity/` - Memory files + decisiones
- `integration/` - APIs + data flows
- `.github/workflows/` - CI/CD automático

## 👥 Trinity

| Rol | Agente | Responsabilidad |
|-----|--------|-----------------|
| Director | Tori (Rodrigo Bustos) | Visión estratégica y última palabra |
| Product Architect | Rosario (ChatGPT) | Visión, criterio, VISION.md, bloques negros y límites de producto |
| CTO / Execution Engine | Claude | Arquitectura, código core, decisiones técnicas, memoria Trinity |
| Heavy Execution | AG (Google Antigravity) | Implementaciones intensivas en IDE, agentes paralelos, tareas largas sobre repo |
| Heavy Code Worker | MINI (MiniMax) | Generación intensiva de código, refactors, scaffolding, tests y cadenas BN TRAIN |
| Validator / Explorer | Gemini | Validación cruzada, exploración técnica y revisión independiente |

## 🚀 Cómo empezar

**Cada agente lee SU documento de onboarding:**

| Agente | Documento | Qué encontrás |
|--------|-----------|----------------|
| Rosario | [TO_ROSARIO.md](TO_ROSARIO.md) | Tu flujo, qué skills leer, formato de VISION.md |
| Claude | [TO_CLAUDE.md](TO_CLAUDE.md) | Tu flujo, qué skills leer, qué validás, qué mantenés |
| AG | [TO_GEMINI.md](TO_GEMINI.md) | Flujo actual de ejecución pesada y debugging |
| MINI | [TO_MINI.md](TO_MINI.md) | Ejecución por BN TRAIN, límites, formato de salida y reglas de STOP |
| Gemini | [TO_GEMINI.md](TO_GEMINI.md) | Validación cruzada y revisión técnica |

Cada documento tiene pasos numerados en orden. Seguilo de arriba a abajo y al final sabés exactamente qué hacer.

## ⚙️ Regla MINI

MINI puede ejecutar cadenas amplias de Bloques Negros solo cuando cada BN está cerrado y tiene objetivo, archivos permitidos, archivos prohibidos, criterios de aceptación, verificación y condición de STOP.

Si un BN falla, MINI no continúa al siguiente. Reporta evidencia y queda bloqueado hasta decisión de Claude/Tori.

## 📐 Stack Base

- **Backend:** Python 3.12+ / FastAPI
- **Frontend:** React / Next.js + TailwindCSS
- **Database:** PostgreSQL (migración desde SQL Server)
- **Infra:** GitHub Actions CI/CD
- **Deployment:** PyInstaller (desktop) / Vercel (web)
