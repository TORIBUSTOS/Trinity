# SYSTEM BLUEPRINT: TAUROS v2 (PRIME)

## 1. Identidad del Proyecto
**TAUROS v2** es el cerebro financiero del ecosistema TORO. Su propósito es la **Captura, Inteligencia y Proyección** de flujos de capital, transformando datos bancarios crudos en insights estratégicos para la toma de decisiones.

- **Mantra**: "Intelligence over Operation". Solo procesa información, no ejecuta pagos ni almacena credenciales bancarias.
- **Estado**: Production-Ready Beta.
- **Ruta Local**: `C:\Users\mauri\OneDrive\Escritorio\TORO\_TORO _HOLDING_\55 - Proyectos-TORO v2\2_TAUROS_v2`

## 2. Mapa Funcional (Árbol de Capacidades)

### A. Ingesta & Normalización (BN-001/002)
- **Multi-Source Parser**: Procesamiento de CSVs bancarios (Galicia, ICBC, Santander, etc.).
- **Batch Management**: Control de lotes de importación para evitar duplicados.
- **Normalización**: Estandarización de fechas, montos y descripciones.

### B. Motor de Categorización (Cascada) (BN-003)
- **Regex Engine**: Clasificación automática basada en patrones.
- **Jerarquía**: Sistema de Categoría > Subcategoría.
- **Confidence Scoring**: Evaluación de la precisión de la auto-categorización.

### C. Reportes & Analytics (BN-006/007)
- **Hierarchical P&L**: Reporte de Pérdidas y Ganancias dinámico.
- **Bento Dashboard**: Vista ejecutiva con KPIs principales (Caja, Burn Rate, Runway).
- **Hormone Analysis**: Desglose visual de flujos por categorías críticas.

### D. Inteligencia Predictiva (Cortex) (BN-008)
- **Forecast Engine**: Proyección de saldos basada en histórico.
- **Insight Feed**: Alertas proactivas sobre fugas de capital o patrones de gasto.

## 3. Modelo de Dominio (Entidades Clave)
- **Movimiento**: La unidad atómica de información. Atributos: `fecha`, `descripcion`, `monto`, `categoria`, `subcategoria`.
- **ImportBatch**: Tracking de cada subida de archivos para auditoría.
- **CascadaRule**: Reglas de negocio que definen cómo el sistema "aprende" a categorizar.

## 4. Arquitectura Técnica (Blueprint Axial)

### Stack Tecnológico
- **Backend**: FastAPI (Python 3.11+).
- **Frontend**: Next.js 14+ (App Router).
- **Database**: SQLite vía SQLAlchemy (Local-First).
- **Processing**: Pandas para análisis de datos masivos.

### Flujo de Datos
1. `User` -> `Next.js (Upload)` -> `FastAPI (Parser)`
2. `FastAPI` -> `SQLAlchemy` -> `SQLite (Persistence)`
3. `FastAPI (Categorizer/Insights)` -> `Recharts (Frontend Visualization)`

## 5. Glosario Imperial
- **Cortex**: El motor de IA/Heurística que genera insights.
- **Cascada**: El sistema jerárquico de reglas de categorización.
- **Hormonas**: Indicadores metabólicos de la salud financiera del holding.
- **Bento**: Estilo de diseño de dashboard en celdas integradas.
