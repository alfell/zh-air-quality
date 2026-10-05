"""Endpoint for stations metadata."""

from fastapi import APIRouter

from zh_air_quality.dependencies import ClientDep
from zh_air_quality.schemas import Station
from zh_air_quality.services.stations import build_stations

router = APIRouter(prefix="/stations", tags=["Stations"])


@router.get("")
def list_stations(client: ClientDep) -> list[Station]:
    """Return all stations"""
    raw_stations = client.load_stations()
    return build_stations(raw_stations)
