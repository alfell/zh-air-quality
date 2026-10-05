"""Integration tests for the health endpoint."""

from zh_air_quality import config


def test_health_returns_ok(api):
    """Health endpoint responds with status ok."""
    response = api.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "version": config.APP_VERSION,
    }
