"""HTTP client for Open Data Zurich: download and JSON parsing only."""

import httpx

from zh_air_quality import config


class OpenDataZurichError(Exception):
    """Raised when data cannot be downloaded from Open Data Zurich catalogue."""


class OpenDataZurichClient:
    """Downloads the metadata file from the Open Data Zurich catalogue."""

    def load_stations(self) -> list[dict]:
        """Return the raw metadata of all measurement stations."""
        metadata = self._get_json(config.METADATA_URL)
        try:
            return metadata["Standorte"]
        except KeyError as exc:
            raise OpenDataZurichError("Metadata has no section 'Standorte'") from exc

    def _get_json(self, url: str) -> dict:
        """Download a JSON document and return it as a dictionary."""
        try:
            response = httpx.get(
                url, timeout=config.REQUEST_TIMEOUT, follow_redirects=True
            )
            response.raise_for_status()
            return response.json()
        except (httpx.HTTPError, ValueError) as exc:
            raise OpenDataZurichError(f"Could not load {url}") from exc
