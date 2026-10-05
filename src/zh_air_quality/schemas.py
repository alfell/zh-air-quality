"""Pydantic models that define the JSON responses of the API."""

from pydantic import BaseModel


class Health(BaseModel):
    """A health check."""

    status: str
    version: str


class Station(BaseModel):
    """A measurement station."""

    code: str
    name: str
    address: str
    latitude: float
    longitude: float
    altitude_m: float
    description: str
