"""
TAUROS PRIME - Entry Point
"""
from fastapi import FastAPI

app = FastAPI(
    title="TAUROS PRIME",
    description="Control de Gestión Financiera - SANARTE",
    version="0.1.0"
)

@app.get("/health")
async def health():
    return {"status": "ok", "system": "tauros-prime"}
