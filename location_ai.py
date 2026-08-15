import json
from urllib.request import Request, urlopen


# Used only when the online location service is unavailable.
MANUAL_LATITUDE = 23.0225
MANUAL_LONGITUDE = 72.5714
MANUAL_PLACE = "Manual / demo location"


def get_location():
    """
    Gets an approximate current location from the internet connection.
    Falls back safely to the manual location if unavailable.
    """

    try:
        request = Request(
            "https://ipapi.co/json/",
            headers={"User-Agent": "OmniAI/1.0"}
        )

        with urlopen(request, timeout=8) as response:
            data = json.loads(response.read().decode("utf-8"))

        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if latitude is None or longitude is None:
            raise ValueError("Location coordinates were not received.")

        city = data.get("city", "Unknown city")
        region = data.get("region", "")
        country = data.get("country_name", "Unknown country")

        place_parts = [city, region, country]
        place = ", ".join(part for part in place_parts if part)

        location = {
            "latitude": latitude,
            "longitude": longitude,
            "place": place,
            "mode": "APPROXIMATE NETWORK LOCATION",
            "maps_link": (
                f"https://www.google.com/maps?q={latitude},{longitude}"
            )
        }

        print("📍 Emergency Location")
        print("Place:", place)
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print("🗺️ Maps:", location["maps_link"])
        print("⚠️ Location mode: APPROXIMATE NETWORK LOCATION")

        return location

    except Exception as error:
        print("⚠️ Could not get online location:", error)
        print("⚠️ Using manual/demo location.")

        return {
            "latitude": MANUAL_LATITUDE,
            "longitude": MANUAL_LONGITUDE,
            "place": MANUAL_PLACE,
            "mode": "DEMO / MANUAL",
            "maps_link": (
                f"https://www.google.com/maps?q="
                f"{MANUAL_LATITUDE},{MANUAL_LONGITUDE}"
            )
        }