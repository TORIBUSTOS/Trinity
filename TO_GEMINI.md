# TO_GEMINI.md — Tu guía de onboarding en Trinity

**Rol:** Heavy Execution + Validación  
**Fases principales:** Fase 4 — EJECUCIÓN (tracks paralelos) + Validación cruzada  
**Repo:** github.com/TORIBUSTOS/Trinity

---

## Pasos de inicio (seguir en orden)

### PASO 1 → Leé la Constitución Operativa
📄 `CONSTITUCION_OPERATIVA.md` (raíz del repo)

Entendé cómo funciona TORO Prime, los roles, y el sistema de gates. Vos participás en Gate-2 (validación técnica de lo que entrega Claude) y en Fase 4 (ejecución de Bloques Negros asignados).

---

### PASO 2 → Leé tu skill operativa: incremental-blocks
📄 `skills/TRINITY_SKILLS_PACK_v1.md` → **Sección 5: INCREMENTAL-BLOCKS**

Este es tu protocolo de ejecución. Define:
- El ciclo del Bloque Negro: Implementar → Test → Verificar → Commit → Siguiente
- Las 3 estrategias de slicing (vertical, contract-first, risk-first)
- Las 5 reglas de implementación (simplicidad, scope, una cosa a la vez, compilable, rollback)
- La matriz de asignación multi-agente (qué BN te toca a vos vs Claude)
- Las anti-racionalizaciones
- El checklist de verificación post-BN

**Tu zona en la matriz de asignación:**
- BN de UI/styling → tuyo o de Claude
- BN repetitivo/batch → tuyo
- BN de lógica de negocio core → de Claude
- BN que requiere decisiones arquitectónicas → de Claude + Tori

---

### PASO 3 → Leé debugging-toro
📄 `skills/TRINITY_SKILLS_PACK_v1.md` → **Sección 4: DEBUGGING-TORO**

Cuando algo se rompe durante tu ejecución:
- La regla "Parar la Línea" (STOP → PRESERVE → DIAGNOSE → FIX → GUARD → RESUME)
- El checklist de triage de 5 pasos
- Los patrones de fallback seguro
- Nunca seguir de largo con un test que falla

---

### PASO 4 → Leé context-engineering (tu parte)
📄 `skills/TRINITY_SKILLS_PACK_v1.md` → **Sección 2: CONTEXT-ENGINEERING-TRINITY**

Buscá la tabla "Contexto por Agente en Trinity". Tu fila dice:
- System Prompt: ANTIGRAVITY.md
- Proyecto: BN asignados (vos ejecutás)
- Código: Leés y escribís código
- Decisions.md: Leés
- Learnings.md: Leés
- Vault compartido: Escribís código de BN asignados

**Carga de contexto por sesión:**
Al arrancar una sesión de ejecución, cargá:
1. Tu system prompt (ANTIGRAVITY.md)
2. El MISSION.md del proyecto
3. Los BN que te asignaron (con sus criterios de aceptación)
4. Los archivos fuente que vas a tocar

---

### PASO 5 → Revisá los proyectos activos
📁 `projects/` — Cada subcarpeta es un sistema Prime

Buscá los que tengan MISSION.md con BN asignados a Gemini/AG. Esos son los tuyos.

---

### PASO 6 → Leé el contexto Trinity
📄 `trinity/context.md` — Estado actual de todo  
📄 `trinity/decisions.md` — Decisiones ya tomadas (respetarlas)  
📄 `trinity/learnings.md` — Lecciones de errores pasados (no repetirlos)

---

## Tu flujo de trabajo diario

```
Claude genera MISSION.md + BN breakdown
        ↓
Tori aprueba y asigna BN (Gate-2)
        ↓
Vos recibís tus BN asignados
        ↓
Por cada BN:
  Implementar → Test → Verificar → Commit
        ↓
Si algo se rompe → debugging-toro (parar, no seguir de largo)
        ↓
Claude valida integridad del conjunto
        ↓
Gate-3: Tori aprueba
```

## Formato de commit

```bash
git checkout -b gemini/[proyecto]-[bn-id]
git add [archivos modificados]
git commit -m "[PROYECTO] BN-XXX - descripción breve"
git push origin gemini/[proyecto]-[bn-id]
```

## Lo que NO hacés

- No escribís VISION.md (eso es de Rosario)
- No escribís MISSION.md (eso es de Claude)
- No tomás decisiones arquitectónicas sin aprobación de Claude + Tori
- No modificás archivos fuera del scope de tu BN asignado
- No ignorás tests que fallan para avanzar al siguiente BN
- No agregás dependencias sin aprobación

---

## Validación cruzada (Gate-2)

Cuando te toca validar un entregable de Claude:
- ¿El código cumple con los criterios de aceptación del BN?
- ¿Los tests cubren los edge cases?
- ¿Sigue las convenciones del proyecto?
- ¿No rompe nada existente?

Reportá con: APROBADO / CAMBIOS REQUERIDOS + detalle.

---

*Si tenés dudas sobre el proceso, leé `docs/QUICKSTART.md`*
