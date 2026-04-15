## 14. Consolidación por cartera y unificación de tickers

MINOS PRIME debe permitir la coexistencia de múltiples carteras patrimoniales dentro de una misma fuente o plataforma, manteniendo separación operativa y claridad estructural.

### 14.1 Modelo de carteras

Cada fuente puede contener una o más carteras independientes.

Ejemplos:
- Balanz | Cartera 1
- Balanz | Cartera 2
- Bull Market | Cartera principal
- Binance | Cartera cripto

Cada cartera debe:
- mantener su propio conjunto de activos;
- permitir nombre editable;
- conservar su estructura de posiciones, saldos y composición;
- ser visualizada de forma independiente.

El sistema no debe asumir un único contenedor por plataforma.

---

### 14.2 Vista consolidada patrimonial

MINOS PRIME debe consolidar todas las carteras en una vista global del patrimonio, permitiendo:

- distribución total por activo;
- distribución por plataforma;
- exposición por moneda;
- lectura agregada del patrimonio.

Esta vista puede incluir sumas de valuación y exposición, pero no debe perder trazabilidad de origen por cartera.

---

### 14.3 Vista unificada de tickers

Además de la consolidación patrimonial, el sistema debe ofrecer una vista simplificada basada en activos únicos.

Esta vista no debe sumar nominales entre carteras, sino identificar la presencia de cada ticker dentro del sistema.

#### Objetivo

Permitir una lectura estratégica rápida del conjunto de activos sin duplicaciones por cartera.

#### Funcionamiento

- se identifican todos los tickers presentes en el sistema;
- se eliminan duplicados por símbolo;
- se registra en cuántas y cuáles carteras aparece cada activo;
- se asigna una señal o estado único por ticker;
- se construye una tabla unificada de activos.

#### Ejemplo

Si un activo aparece en múltiples carteras:

- Balanz Cartera 1 → MELI 10
- Balanz Cartera 2 → MELI 2

La vista unificada no mostrará "MELI 12".

Mostrará:

- Ticker: MELI
- Presencia: 2 carteras
- Estado: BUY (u otro según lógica del sistema)

---

### 14.4 Estructura sugerida

| Ticker | Presente en | Cartera(s) | Estado |
|--------|------------|-----------|--------|
| MELI   | 2          | Balanz 1, Balanz 2 | BUY |
| NVDA   | 1          | Balanz 1 | HOLD |
| TSLA   | 1          | Balanz 2 | SELL |

---

### 14.5 Separación conceptual

El sistema debe diferenciar claramente entre:

A. Datos patrimoniales por cartera:
- cantidades;
- valuación;
- moneda;
- composición específica;

B. Capa de lectura unificada por ticker:
- activo único;
- presencia transversal;
- señal simplificada;
- lectura estratégica.

---

### 14.6 Propósito

Esta funcionalidad permite:

- evitar duplicación visual de activos;
- simplificar la lectura del sistema completo;
- identificar rápidamente activos relevantes;
- facilitar la toma de decisiones a nivel patrimonial;
- separar la contabilidad de posiciones de la interpretación estratégica.

---

### 14.7 Consideraciones

- la señal por ticker debe definirse por lógica central (no por cartera individual);
- la vista unificada no reemplaza la vista patrimonial ni la vista por cartera;
- ambas deben coexistir como capas complementarias del sistema.
