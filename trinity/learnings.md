# TRINITY: LECCIONES DE DEPRECATED

> Lo que salió mal antes. No repetir.

---

## HILE — Over-engineered

**Qué pasó:**
- Visión confusa → specs caóticas
- Código sin tests → rework infinito
- Ninguna integración → sistema aislado
- Se intentó hacer todo a la vez sin pipeline claro

**Lección para TORO Prime:**
- ✅ SIEMPRE specs antes de código
- ✅ Tests desde el inicio
- ✅ Integración en Fase 1
- ✅ Un sistema a la vez, completo, antes de pasar al siguiente
- ✅ Gates de validación obligatorios

---

## Patrón general de fracaso detectado

```
Idea ambiciosa 
  → Ejecución sin estructura 
    → Complejidad crece 
      → Abandono parcial 
        → Sistema zombie (ni vivo ni muerto)
```

**Antídoto TORO Prime:**
```
Visión clara (VISION.md)
  → Misión acotada (MISSION.md)
    → Arquitectura validada (ARCHITECTURE.md)
      → Specs ejecutables (SPECS.md)
        → Código con tests
          → Deploy incremental
```

---
