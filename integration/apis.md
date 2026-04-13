# INTEGRACIÓN: APIs

> Documentación de APIs públicas entre sistemas Prime.

---

## Convenciones

- Todas las APIs son REST (FastAPI)
- Formato: JSON
- Auth: TBD (JWT propuesto)
- Base URL por sistema: `/{system}/api/v1/`

## APIs Planificadas

### TAUROS PRIME
- `GET /tauros/api/v1/health` — Health check
- `GET /tauros/api/v1/transactions` — Listar transacciones
- `POST /tauros/api/v1/transactions/classify` — Clasificar transacciones
- _Más endpoints después de SPECS.md_

### Otros sistemas
_Pending VISION.md → SPECS.md pipeline_

---
