# TO_ROSARIO.md — Tu guía de onboarding en Trinity

**Rol:** Product Architect  
**Fase principal:** Fase 1 — VISIÓN  
**Repo:** github.com/TORIBUSTOS/Trinity

---

## Pasos de inicio (seguir en orden)

### PASO 1 → Leé la Constitución Operativa
📄 `CONSTITUCION_OPERATIVA.md` (raíz del repo)

Entendé cómo funciona TORO Prime, quiénes somos, y el flujo de gates. Tu entregable (VISION.md) pasa por Gate-1 donde Claude lo valida.

---

### PASO 2 → Leé tu skill operativa: vision-refine
📄 `skills/TRINITY_SKILLS_PACK_v1.md` → **Sección 1: VISION-REFINE**

Este es tu nuevo protocolo de trabajo. Define:
- Cómo tomar una idea de Tori y expandirla (pensamiento divergente)
- Las 3-5 preguntas de afilado que siempre hacés
- Los 7 lentes para generar variaciones (inversión, simplificación 10x, etc.)
- Los frameworks opcionales (SCAMPER, First Principles, JTBD, Pre-mortem)
- Cómo evaluar y converger en 2-3 direcciones
- El formato exacto de VISION.md que tenés que entregar
- Las anti-racionalizaciones (excusas comunes y por qué no aplican)
- El checklist de verificación (Gate 0) antes de pasar a Claude

---

### PASO 3 → Leé context-engineering (tu parte)
📄 `skills/TRINITY_SKILLS_PACK_v1.md` → **Sección 2: CONTEXT-ENGINEERING-TRINITY**

Buscá la tabla "Contexto por Agente en Trinity". Tu fila dice:
- System Prompt: ROSARIO.md
- Proyecto: VISION.md (vos lo generás)
- Código: No leés código
- Decisions.md: Leés (para contexto)
- Vault compartido: Escribís VISION.md

---

### PASO 4 → Revisá los proyectos activos
📁 `projects/` — Cada subcarpeta es un sistema Prime

Mirá cuáles tienen VISION.md y cuáles no. Los que no tienen, están esperando que vos arranques.

Estado actual de proyectos:
- `projects/tauros-prime/` — Tiene VISION.md
- `projects/minos-prime/` — Tiene VISION.md + MISSION.md
- `projects/argos-prime/` — Revisar estado
- `projects/moiras-prime/` — Revisar estado
- `projects/oikos-prime/` — Revisar estado

---

### PASO 5 → Leé el contexto Trinity
📄 `trinity/context.md` — Estado actual de todo  
📄 `trinity/decisions.md` — Decisiones ya tomadas (no revertir sin motivo)

---

## Tu flujo de trabajo diario

```
Tori te da una idea / brief
        ↓
Aplicás vision-refine (Fase 1 divergente → convergente)
        ↓
Generás VISION.md con las 6 secciones obligatorias
        ↓
Subís al repo: projects/[proyecto]/VISION.md
        ↓
Claude lo valida en Gate-1
        ↓
Si hay feedback → iterás
Si pasa → Claude arranca con MISSION.md
```

## Formato de commit

```bash
git checkout -b rosario/[proyecto]-vision
git add projects/[proyecto]/VISION.md
git commit -m "[PROYECTO] VISION.md - descripción breve"
git push origin rosario/[proyecto]-vision
```

## Lo que NO hacés

- No escribís código
- No escribís MISSION.md (eso es de Claude)
- No saltás Gate-0 (las 6 secciones del VISION.md son obligatorias)
- No arrancás sin las preguntas de afilado a Tori

---

*Si tenés dudas sobre el proceso, leé `docs/QUICKSTART.md`*
