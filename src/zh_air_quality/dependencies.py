"""Shared FastAPI dependencies."""

from typing import Annotated

from fastapi import Depends

from zh_air_quality.clients.accessdata import OpenDataZurichClient


def get_client() -> OpenDataZurichClient:
    """Return the client used to access Open Data Zurich."""
    return OpenDataZurichClient()


ClientDep = Annotated[OpenDataZurichClient, Depends(get_client)]
