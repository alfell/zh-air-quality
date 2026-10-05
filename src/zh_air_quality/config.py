"""Central configuration: data source URLs, CSV format and constants."""

from importlib.metadata import version

APP_VERSION = version("zh_air_quality")

BASE_URL = "https://data.stadt-zuerich.ch/dataset/ugz_luftschadstoffmessung_stundenwerte/download"
METADATA_URL = f"{BASE_URL}/uzg_ogd_metadaten.json"

REQUEST_TIMEOUT = 10.0
