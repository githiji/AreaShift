
import phonenumbers
from phonenumbers import geocoder
import subprocess
import geopy.distance

from dicts import STATE_COORDS, MULLVAD_CITIES, STATE_TO_MULLVAD




def find_nearest_mullvad_city(state: str):
    if state not in STATE_COORDS:
        print("State coordinates not found.")
        return None

    state_coords = STATE_COORDS[state]
    nearest_city = None
    min_distance = float('inf')

    for city_code, city_coords in MULLVAD_CITIES.items():
        distance = geopy.distance.distance(state_coords, city_coords).km
        if distance < min_distance:
            min_distance = distance
            nearest_city = city_code

    return nearest_city
# Get state from area code using phonenumbers library
def get_state_from_area_code(area_code: str):
    # phonenumbers needs a full phone number, so we fake the last digits
    fake_number = f"+1{area_code}5559999"

    try:
        parsed = phonenumbers.parse(fake_number, "US")
        state = geocoder.description_for_number(parsed, "en")
        return state if state else print("State not found for this area code.")
    
    except:
        print("Error parsing phone number.")
        return None
    
# Set Mullvad VPN location using subprocess
def set_mullvad_location(state: str):
    # 1. Check direct match first (do NOT overwrite the original state)
    mullvad_code = STATE_TO_MULLVAD.get(state)

    # -----------------------------------------
    # CASE 1: State has a direct Mullvad region
    # -----------------------------------------
    if mullvad_code:
        print(f"Setting Mullvad location to: {mullvad_code}")
        result = subprocess.run(
            ["mullvad", "relay", "set", "location", ]+ mullvad_code.split(),
            capture_output=True, text=True
        )

        if result.returncode != 0:
            print(f"Error setting Mullvad location: {result.stderr}")
        else:
            print("Mullvad location set successfully.")
        return

    # -----------------------------------------
    # CASE 2: No direct match → use nearest city
    # -----------------------------------------
    nearest_city = find_nearest_mullvad_city(state)

    if not nearest_city:
        print(f"No Mullvad region found for state '{state}', and no fallback match exists.")
        return

    print(f"No Mullvad region for {state}. Using nearest city → {nearest_city}")

    result = subprocess.run(
        ["mullvad", "relay", "set", "location", nearest_city],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        print(f"Error setting Mullvad location: {result.stderr}")
    else:
        print(f"Mullvad location successfully set to nearest city: {nearest_city}")
