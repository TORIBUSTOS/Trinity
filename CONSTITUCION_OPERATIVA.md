# CONSTITUCIÓN OPERATIVA - TORO PRIME

## Autoridad y Gobernanza

**Director General:** Tori (Rodrigo Bustos)  
**Última palabra:** Siempre Tori  
**Filosofía:** "Versión final por ahora" — mejora iterativa sobre perfección

---

## Principios Operativos

### 1. Specs antes de código
Ningún sistema se codifica sin pasar por el pipeline completo:
VISION.md → MISSION.md → ARCHITECTURE.md → SPECS.md → Código

### 2. Gates de validación
Cada documento pasa por un gate antes de avanzar:
- **Gate-1:** Rosario entrega → Claude valida coherencia
- **Gate-2:** Claude entrega → Gemini valida técnicamente
- **Gate-3:** Tori aprueba → se ejecuta

### 3. Trinity Memory
Toda decisión, aprendizaje y bloqueo se documenta en `trinity/`:
- `decisions.md` — Decisiones tomadas (inmutable)
- `learnings.md` — Lecciones de errores pasados
- `blockers.md` — Impedimentos activos
- `context.md` — Estado actual (fuente de verdad)

### 4. No repetir errores
El sistema HILE se deprecó por:
- Visión confusa → specs caóticas
- Código sin tests → rework infinito
- Sin integración → sistema aislado

TORO Prime existe para no repetir esto.

---

## Sistemas Prime

| Sistema | Función | Estado |
|---------|---------|--------|
| TAUROS PRIME | Control de gestión financiera | Planning |
| MOIRAS PRIME | Obligaciones y compliance | Planning |
| ARGOS PRIME | Oportunidades e inversiones | Planning |
| MINOS PRIME | Cartera y cobranzas | Planning |
| OIKOS PRIME | Gestión operativa integral | Planning |

---

## Flujo de Trabajo

```
Tori (Visión) 
  → Rosario (VISION.md + ARCHITECTURE.md)
    → Claude (MISSION.md + SPECS.md + Código)
      → Gemini (Validación)
        → Tori (Aprobación final)
          → Deploy
```

---

*Versión 1.0 — Abril 2026*
