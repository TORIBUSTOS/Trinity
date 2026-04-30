# MINOS — Sprint 2: Broker-Grade Valuation Core

## Objetivo

Convertir MINOS en un sistema capaz de replicar, como mínimo, la información financiera base de un broker como Balanz antes de emitir señales o recomendaciones.

Sprint 1 dejó el repo funcional. Sprint 2 corrige el núcleo de producto: la valuación debe ser confiable, trazable y comparable contra broker.

## Problema detectado

MINOS muestra menos información que Balanz y algunas valuaciones no coinciden con el broker.

Caso observado:

- Balanz muestra BMA y YPFD como acciones BYMA en ARS.
- Balanz calcula:
  - V. Actual = nominales * precio actual
  - V. Inicial = nominales * PPC
  - Rendimiento = V. Actual - V. Inicial
  - Rendimiento % = Rendimiento / V. Inicial
- MINOS mostraba valores inferiores y no exponía con claridad precio, timestamp, PPC, rendimiento ni peso de cartera.

Hipótesis principal:

- Resolución incorrecta de instrumentos argentinos.
- Riesgo de usar tickers ADR/USA en lugar de tickers BYMA, por ejemplo BMA en vez de BMA.BA, YPF en vez de YPFD.BA.
- Moneda y fuente de precio no suficientemente trazables.

## Decisión estratégica

Primero verdad financiera. Después inteligencia.

Las señales BUY/HOLD/SELL quedan subordinadas al estado de valuación. Ninguna señal debe considerarse válida si `valuation_status != OK`.

## Arquitectura objetivo

```text
Position -> Instrument -> PricingEngine -> Quote -> ValuationEngine -> Portfolio
```

MINOS no debe valorar por `ticker string` aislado. Debe valorar por instrumento financiero resuelto.

Identidad mínima de instrumento:

- ticker
- mercado / exchange
- tipo de instrumento
- moneda
- fuente
- unidad de cotización
- símbolo de pricing resuelto

## Fases del sprint

### Fase 0 — Diagnóstico de pricing

Crear o adaptar script:

```text
scripts/debug_pricing.py
```

Debe imprimir para BMA, YPFD, GGAL, PAMP y SUPV:

```text
ticker_input | instrument_type | exchange | resolved_symbol | source | price | currency | quote_timestamp | fetched_at | status | error
```

Criterios:

- BMA BYMA debe resolver a BMA.BA.
- YPFD BYMA debe resolver a YPFD.BA.
- GGAL BYMA debe resolver a GGAL.BA.
- PAMP BYMA debe resolver a PAMP.BA.
- SUPV BYMA debe resolver a SUPV.BA.
- La moneda esperada para acciones BYMA es ARS.
- Nunca usar `price = 0` como fallback silencioso.
- Si faltan `instrument_type` o `exchange`, reportar bug estructural.

### Fase 1 — Modelo financiero broker-grade

Cada posición valuada debe exponer:

- ticker
- instrument_type
- exchange
- quantity / nominales
- price
- price_currency
- price_timestamp
- avg_cost / PPC
- avg_cost_currency
- market_value / V. Actual
- cost_basis / V. Inicial
- pnl_absolute / Rendimiento $
- pnl_percentage / Rendimiento %
- portfolio_weight / % de cartera
- source
- pricing_status
- valuation_status
- valuation_trace

### Fase 2 — Instrument Identity

Reglas mínimas:

- Si `exchange == BYMA` e `instrument_type == EQUITY`, `resolved_symbol = ticker + ".BA"`.
- Si `exchange == NYSE` o `exchange == NASDAQ`, `resolved_symbol = ticker`.
- Si `instrument_type == CEDEAR`, usar `pricing_symbol` explícito si existe.
- Si `instrument_type == BOND`, no usar yfinance ciegamente.
- Si falta exchange o instrument_type, marcar `AMBIGUOUS_INSTRUMENT` y no calcular valuación confiable.

Ejemplos:

- BYMA / EQUITY / BMA -> BMA.BA
- BYMA / EQUITY / YPFD -> YPFD.BA
- NYSE / EQUITY / BMA -> BMA
- NYSE / EQUITY / YPF -> YPF

### Fase 3 — Pricing Engine

El pricing engine debe devolver un objeto `Quote`, no solo un float.

Campos mínimos de `Quote`:

- input_ticker
- resolved_symbol
- source
- price
- currency
- timestamp
- fetched_at
- instrument_type
- exchange
- quote_unit
- status
- is_stale
- error

Reglas:

- Si no hay precio, no inventar.
- Si hay error, devolver status explícito.
- Si mercado cerrado, usar último cierre válido marcado como `MARKET_CLOSED` o `STALE`.
- Si currency no coincide, exigir conversión explícita.
- No convertir automáticamente sin política FX definida.

### Fase 4 — Valuation Engine

Para acciones:

```text
market_value = quantity * price
cost_basis = quantity * avg_cost
pnl_absolute = market_value - cost_basis
pnl_percentage = pnl_absolute / cost_basis * 100
portfolio_weight = market_value / total_market_value * 100
```

Reglas:

- Usar Decimal para dinero.
- No usar float para cálculos financieros.
- No redondear antes del cálculo.
- La valuación debe devolver `valuation_trace`.

Ejemplo de trace esperado:

```text
BMA: qty=65, resolved_symbol=BMA.BA, price=10870.00 ARS, market_value=706550.00 ARS, avg_cost=9436.97, cost_basis=613403.05
```

### Fase 5 — Tests de reconciliación Balanz

Crear tests con precios inyectados, sin yfinance.

Casos golden:

#### BMA

```text
quantity = 65
price = 10870.00
avg_cost = 9436.97
market_value esperado = 706550.00
cost_basis esperado = 613403.05
pnl_absolute esperado = 93146.95
pnl_percentage esperado = 15.19
```

#### YPFD

```text
quantity = 15
price = 66425.00
avg_cost = 42089.79
market_value esperado = 996375.00
cost_basis esperado = 631346.85
pnl_absolute esperado = 365028.15
pnl_percentage esperado = 57.82
```

Reglas:

- Si estos tests fallan, corregir ValuationEngine.
- Si pasan, concentrar corrección en PricingEngine / Instrument Identity.
- No usar precios live en estos tests.

### Fase 6 — UI broker-like

Crear o adaptar una pantalla/tabla de cartera que muestre como mínimo:

- Ticker
- Nominales
- Precio
- Fecha
- PPC
- V. Actual
- V. Inicial
- Rendimiento $
- Variación %
- % de cartera
- Estado pricing
- Fuente

Reglas de UI:

- Si `pricing_status != OK`, mostrar advertencia visible.
- Si `valuation_status != OK`, no mostrar señal como válida.
- Las señales BUY/HOLD/SELL deben quedar visualmente subordinadas a la valuación.
- Primero verdad financiera, después inteligencia.

## Criterios de aceptación

Sprint 2 se considera cerrado cuando:

1. BMA BYMA resuelve a BMA.BA.
2. YPFD BYMA resuelve a YPFD.BA.
3. La valuación con precios inyectados coincide con los casos golden tipo Balanz.
4. La UI muestra precio, fecha, PPC, V. Actual, V. Inicial, rendimiento y peso de cartera.
5. Toda posición valuada puede explicar su cálculo mediante `valuation_trace`.
6. No se emiten señales válidas sobre posiciones con valuación dudosa.
7. `pytest -q` pasa sin romper Sprint 1.

## Fuera de alcance

No resolver en este sprint salvo que sea imprescindible:

- Optimización de señales.
- Recomendaciones nuevas.
- CEDEAR avanzado.
- Bonos complejos.
- FX avanzado.
- Fuente alternativa premium a yfinance.

## Validación final esperada

Backend:

```bash
uvicorn src.main:app --reload --port 8800
```

Frontend:

```bash
cd frontend/client
npm run dev
```

Tests:

```bash
pytest -q
```

Output de cierre requerido:

1. Archivos modificados.
2. Tests agregados.
3. Resultado de pytest.
4. Ejemplo de `debug_pricing` para BMA e YPFD.
5. Ejemplo de `valuation_trace` para BMA e YPFD.
6. Descripción o captura de tabla broker-like.
7. Riesgos pendientes: CEDEAR, bonos, FX, fuente alternativa.
