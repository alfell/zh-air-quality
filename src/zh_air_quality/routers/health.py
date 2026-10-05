"""Endpoint for health check / status of the API."""

from fastapi import APIRouter

from zh_air_quality import config
from zh_air_quality.schemas import Health

router = APIRouter(prefix="/health", tags=["API Status"])


@router.get("")
def get_status() -> Health:
    return Health(
        status="ok",
        version=config.APP_VERSION,
    )
