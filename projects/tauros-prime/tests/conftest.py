"""TAUROS PRIME - Test Configuration"""
import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    return TestClient(app)
