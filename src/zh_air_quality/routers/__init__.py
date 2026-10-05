"""Endpoint for health check of the API."""

from fastapi import APIRouter

from zh_air_quality import config
from zh_air_quality.schemas import Health

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
def get_health() -> Health:
    return Health(
        status="ok",
        version=config.APP_VERSION,
    )
