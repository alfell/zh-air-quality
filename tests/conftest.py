"""Shared test fixtures: a test API client."""

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from zh_air_quality.main import app

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def api():
    """API test client."""
    return TestClient(app)
