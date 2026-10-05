"""Pydantic models that define the JSON responses of the API."""

from pydantic import BaseModel


class Health(BaseModel):
    """A Health Check."""

    status: str
    version: str