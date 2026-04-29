# TRINITY UPGRADE v1.1 — QA & Iteration Layer

## 1. Propósito

Trinity ya no debe funcionar solo como sistema de construcción. A partir de esta versión, Trinity también inspecciona, valida, corrige y aprende.

El objetivo de este upgrade es evitar que los proyectos Prime avancen con pantallas visualmente completas pero funcionalmente incompletas.

Regla central:

> Una pantalla renderizada no equivale a una funcionalidad terminada.

## 2. Problema detectado en proyectos Prime

En proyectos como MINOS, ARGOS, NEXUS y otros módulos Prime, se detectó un patrón típico de iteración rápida:

- Se generan pantallas visualmente correctas.
- Se cierran Bloques Negros por avance aparente.
- Aparecen botones sin acción real.
- Existen formularios, tabs, filtros o modales incompletos.
- Persisten datos mockeados sin declaración clara.
- El frontend puede no estar conectado al backend real.
- La revisión ocurre tarde, cuando el retrabajo ya creció.

Este upgrade convierte ese aprendizaje en una regla permanente del sistema.

## 3. Nueva regla de cierre de Bloques Negros

Ningún Bloque Negro se considera cerrado hasta pasar una revisión funcional explícita.

Todo BN debe declarar:

- Archivos modificados.
- Pantallas o flujos afectados.
- Acciones interactivas creadas o modificadas.
- Endpoints utilizados o pendientes.
- Datos reales, datos mock y placeholders.
- Prueba manual mínima.
- Riesgos detectados.
- Estado de madurez funcional.

## 4. QA Gate obligatorio

Después de cada ejecución de BN debe correrse un QA Gate antes de avanzar al siguiente bloque.

Flujo obligatorio:

```txt
Visión / PRD
↓
Bloque Negro
↓
Ejecución IA
↓
QA Gate
↓
Fixes quirúrgicos si corresponde
↓
Validación
↓
Cierre real del BN
```

El QA Gate debe revisar:

- Botones sin acción real.
- `onClick` vacío, indefinido o solo con `console.log`.
- Formularios sin `onSubmit` funcional.
- Links con `href="#"`, rutas vacías o rutas inexistentes.
- Tabs, filtros, dropdowns o modales sin cambio de estado real.
- Uso de `mockData` no declarado.
- Endpoints backend existentes pero no consumidos.
- Servicios frontend declarados pero no utilizados.
- Falta de estados `loading`, `error` y `success`.
- Funciones, imports o componentes muertos.
- Errores probables de consola.
- Inconsistencias UX/UI que impidan uso real.

## 5. Estados de madurez funcional

Cada BN, pantalla o flujo debe clasificarse con uno de estos estados:

| Estado | Significado | Criterio |
|---|---|---|
| 🟢 Cerrado funcional | Funciona de punta a punta | UI, lógica, datos y feedback validados |
| 🟡 Cerrado parcial | Útil pero incompleto | Hay partes reales, pero quedan conexiones o UX pendientes |
| 🔴 No cerrar | No debe avanzar | Rompe flujo principal o carece de lógica funcional |
| ⚫ Mock / maqueta | Visual o demostrativo | Debe declararse explícitamente como no productivo |

## 6. Componentes de adorno

Trinity debe distinguir entre:

- Funcionalidad real.
- Funcionalidad parcial.
- Mock temporal.
- Decoración intencional.
- Código muerto.
- Conexión incompleta.

Un componente decorativo no es un error si está declarado. Es un riesgo si se confunde con funcionalidad terminada.

## 7. Roles de IA dentro del flujo

| Rol | Agente sugerido | Responsabilidad |
|---|---|---|
| Dirección estratégica | Tori + Rosario | Decidir prioridad, alcance y cierre consciente |
| Arquitectura de producto | Rosario | Definir criterios de aceptación y límites del BN |
| Auditor lógico | Claude | Revisar coherencia, deuda técnica y componentes incompletos |
| Ejecución técnica | Codex / Claude Code / AG | Implementar fixes y conectar lógica real |
| QA visual / UX | MiniMax / Rosario | Detectar fricción, claridad, copy, estados y flujo visual |
| Validación cruzada | Gemini | Revisar supuestos, riesgos y alternativas |

## 8. Flujo de corrección

Si el QA Gate falla, el BN no se cierra. Se abre un fix quirúrgico.

Prioridades:

| Prioridad | Tipo | Acción |
|---|---|---|
| P0 | Rompe el uso principal | Corregir antes de avanzar |
| P1 | Funcionalidad importante incompleta | Corregir en el mismo ciclo |
| P2 | Mejora UX | Programar en el sprint actual o siguiente |
| P3 | Limpieza o deuda menor | Registrar y acumular para mantenimiento |

Regla de corrección:

> Corregir primero lo que impide usar el sistema. Después lo importante. Al final lo estético.

## 9. Registro de aprendizajes Prime

Cada proyecto Prime debe dejar aprendizajes convertibles en reglas.

Preguntas de cierre:

- ¿Qué se rompió o quedó incompleto?
- ¿Qué se repitió en más de un proyecto?
- ¿Qué debería convertirse en checklist permanente?
- ¿Qué se puede automatizar?
- ¿Qué no debería volver a hacerse manualmente?
- ¿Qué skill nueva necesita Trinity?

## 10. Prompt operativo para auditoría

```txt
Actuá como auditor técnico de UX funcional para el proyecto actual.

Objetivo:
Detectar elementos de interfaz que aparentan funcionalidad pero no están conectados a lógica real.

Revisar:
- componentes frontend
- botones
- formularios
- rutas
- hooks
- servicios API
- uso de mockData
- conexión con backend
- endpoints no consumidos
- errores potenciales de consola
- acciones placeholder

No modificar código todavía.

Entregar informe Markdown con:
1. Resumen ejecutivo.
2. Botones o acciones sin funcionalidad.
3. Componentes mockeados o decorativos.
4. Formularios, filtros, tabs y modales incompletos.
5. Endpoints backend no conectados al frontend.
6. Archivos críticos.
7. Priorización P0/P1/P2/P3.
8. Plan de corrección archivo por archivo.

Criterio:
No asumir que algo funciona.
Si no hay acción, feedback, navegación, request, estado o efecto visible, marcar como sospechoso.
```

## 11. Regla TORO final

> Ningún Bloque Negro se considera terminado hasta pasar por una revisión funcional explícita.
>
> Una entrega visual no equivale a una entrega funcional.
>
> Todo botón, formulario, ruta o componente interactivo debe tener acción real, feedback visible, conexión clara, prueba manual definida y estado de madurez declarado.
