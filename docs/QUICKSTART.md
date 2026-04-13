# QUICKSTART - TORO PRIME

## Para contribuir a un proyecto

### 1. Clonar el repo
```bash
git clone https://github.com/YOUR_USER/toro-prime.git
cd toro-prime
```

### 2. Crear rama de trabajo
```bash
# Convención: nombre/proyecto-documento
git checkout -b rosario/tauros-prime-vision
```

### 3. Escribir tu documento
```bash
# Editar el archivo correspondiente
vim projects/tauros-prime/VISION.md
```

### 4. Commit y push
```bash
git add .
git commit -m "[TAUROS-PRIME] VISION.md - descripción breve"
git push origin rosario/tauros-prime-vision
```

### 5. Abrir PR
- GitHub abrirá automáticamente la opción de PR
- Asignar al reviewer correspondiente según el gate

## Convenciones de commits

```
[SISTEMA] DOCUMENTO - descripción
[TAUROS-PRIME] VISION.md - primer draft
[TRINITY] decisions.md - agregar DEC-004
[INFRA] workflow - agregar test runner
```

## Gates de validación

| Gate | Quién entrega | Quién valida |
|------|--------------|--------------|
| Gate-1 | Rosario (VISION) | Claude |
| Gate-2 | Claude (MISSION/SPECS) | Gemini |
| Gate-3 | Todos | Tori (aprobación final) |
