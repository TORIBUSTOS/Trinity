# UI/UX MAP: TAUROS v2 (PRIME)

## 1. Filosofía de Diseño: "Imperial Tech"
TAUROS v2 adopta una estética que combina la brutalidad y el orden romano con la tecnología avanzada ("The Roman Imperial meeting Gemini Dark").

- **Lógica Visual**: Bento Grids, jerarquía clara, tipografía técnica moderna.
- **Micro-interacciones**: Transiciones suaves, estados de carga elegantes (skeletons), y feedback proactivo vía Toasts.

## 2. Design System (Tokens de Marca)

### Paleta de Colores
- **Base (Background)**: `#131314` (Pure Graphite / Deep Dark).
- **Primary (Gold)**: `#C09891` (Imperial Gold). Utilizado en bordes, acentos y hover states.
- **Secondary (Bronze)**: `#775144` (Roman Bronze). Utilizado en componentes secundarios y sombras.
- **Text (Main)**: `#F4DBD8` (Off-White Rose). Alta legibilidad sobre fondo oscuro.
- **Success/Danger**: Verdes esmeralda y rojos carmesí silenciados para mantener la sobriedad.

### Tipografía
- **Fonts**: Inter (UI), Outfit (Headers).
- **Hierarchy**: Títulos en mayúsculas (Small Caps) para un aire de autoridad técnica.

## 3. Inventario de Pantallas (Vistas)

### A. Dashboard Central (Ejecutivo)
- **Cortex Search**: Barra de búsqueda central con inteligencia (IA).
- **Stats Row**: Tarjetas con KPIs (Ingresos, Gastos, Balance, Runway).
- **Bento Grid**: Gráficos incrustados (PieChart de gastos, FlowChart de ingresos).
- **Recent Insights**: Feed lateral con los últimos patrones detectados.

### B. Reportes (P&L Hierarchical)
- **Vista**: Tabla jerárquica colapsable.
- **Interacción**: Drill-down desde Categoría hasta nivel de subcategoría y movimientos individuales.
- **Filtros**: Selector de período global (Context-based).

### C. Analytics (Deep Dive)
- **Visuales**: Recharts integrados.
- **Gráficos**: Forecast (proyección a 3 meses), Hormone Analysis (distribución metabólica de fondos).
- **Insights Tab**: Listado detallado de anomalías y recomendaciones.

### D. Movimientos (Control de Datos)
- **Tabla Master**: Listado completo con búsqueda global y filtrado por categoría/banco.
- **Acciones**: Edición rápida de categorías, confirmación de confianza (confidence score).

## 4. Flujos de Usuario Críticos

### Flujo de Ingesta (Happy Path)
1. `User` sube archivo CSV al Dropzone en el Sidebar.
2. `Frontend` muestra progreso de subida.
3. `Backend` procesa, categoriza y devuelve el `ImportBatch`.
4. `User` recibe un Toast de éxito y el Dashboard se actualiza automáticamente.

### Flujo de Categorización Manual
1. `User` identifica movimiento con bajo `confidence_score` en la tabla.
2. `User` cambia la categoría.
3. El sistema pregunta si se desea crear una `CascadaRule` para automatizarlo a futuro.

## 5. Componentes UI Reutilizables
- **Sidebar**: Colapsable, con gradientes imperialrs y acceso rápido a módulos.
- **StatCard**: Tarjeta Bento con mini-gráfico de tendencia.
- **ImperialToast**: Notificaciones persistentes con estilo premium.
- **PeriodSelector**: Singleton global para sincronizar todas las vistas.
