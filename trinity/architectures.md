# TRINITY: ARQUITECTURA

> Decisiones arquitectónicas de alto nivel que afectan a todo el ecosistema.

---

## Principios de Diseño

1. **Modularidad:** Cada sistema Prime es independiente pero interoperable
2. **API-first:** Toda comunicación entre sistemas vía API REST (FastAPI)
3. **Data como activo:** PostgreSQL centralizado, schemas separados por sistema
4. **Iterativo:** MVP funcional antes de features avanzados

## Stack Unificado

```
Frontend:  React / Next.js + TailwindCSS
Backend:   Python 3.12+ / FastAPI
Database:  PostgreSQL (schemas por sistema)
Auth:      TBD (probablemente JWT + roles)
Deploy:    GitHub Actions → Vercel (web) / PyInstaller (desktop)
Monitoreo: TBD
```

## IDEs Agénticos

| Herramienta | Uso |
|-------------|-----|
| **Claude Code** | Ejecución primaria, memoria Trinity, specs, código incremental |
| **Google Antigravity** | Ejecución pesada, agentes paralelos, implementaciones intensivas |

Ambos operan sobre el mismo repo Git. Antigravity se activa cuando la tarea requiere múltiples agentes simultáneos o cómputo prolongado.

## Integración entre sistemas

```
TAUROS ←→ MOIRAS   (obligaciones afectan flujo financiero)
TAUROS ←→ ARGOS    (oportunidades requieren capital)
TAUROS ←→ MINOS    (cobranzas alimentan cash flow)
OIKOS  ←→ TODOS    (gestión operativa transversal)
```

---

_Actualizar cuando se tomen decisiones arquitectónicas mayores._
