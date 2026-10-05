def build_stations(raw_stations: list[dict]) -> list[dict]:
    """Return air quality stations with English field names.

    Stations without a code are skipped.
    """
    stations = []
    for raw in raw_stations:
        if not raw.get("Code"):
            continue
        stations.append(
            {
                "id": raw["ID"],
                "code": raw["Code"],
                "name": raw["Name"],
                "address": raw.get("Adresse"),
                "latitude": raw["Koordinaten_WGS84_lat"],
                "longitude": raw["Koordinaten_WGS84_lng"],
                "altitude_m": raw.get("Höhe [M.ü.M.]"),
                "description": raw.get("Beschreibung"),
            }
        )
    return stations


if __name__ == "__main__":
    from pprint import pprint

    from zh_air_quality.clients.accessdata import OpenDataZurichClient

    pprint(build_stations(OpenDataZurichClient().load_stations()))
