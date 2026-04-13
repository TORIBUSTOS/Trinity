# TAUROS PRIME

> Sistema de control de gestión financiera para SANARTE Medicina Prepaga

## Estado: Planning

Esperando VISION.md de Rosario (Product Architect).

## Contexto

TAUROS es la evolución del sistema actual de control de gestión:
- Dashboard financiero (React/Next.js/TailwindCSS)
- Clasificación automática de transacciones bancarias (cascada Concepto → Detalle, 99%+ cobertura)
- Procesamiento mensual de cientos de transacciones
- Base actual: SQL Server (200+ tablas)

## Pipeline

- [ ] VISION.md (Rosario)
- [ ] Gate-1: Validación (Claude)
- [ ] MISSION.md (Claude)
- [ ] ARCHITECTURE.md (Rosario + Claude)
- [ ] Gate-2: Validación técnica (Gemini)
- [ ] SPECS.md (Claude)
- [ ] Gate-3: Aprobación (Tori)
- [ ] Código + Tests
- [ ] Deploy
