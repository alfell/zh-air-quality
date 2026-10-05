"""FastAPI application: creates the app and registers the routers."""

from fastapi import FastAPI

from zh_air_quality import config
from zh_air_quality.routers import health, stations

app = FastAPI(
    title="Air Quality API for the City of Zurich",
    description="App that shows air quality for the measurement stations in Zurich",
    version=config.APP_VERSION,
    contact={
        "name": "Alessandro Feller",
        "email": "aless.feller@gmail.com",
    },
)
app.include_router(health.router)
app.include_router(stations.router)
