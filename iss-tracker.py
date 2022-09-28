import requests
import datetime


URL = "http://api.open-notify.org/iss-now.json"
def main():
    resp = requests.get(URL).json()
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]

    ts = resp["timestamp"]
    ts = datetime.datetime.fromtimestamp(ts)

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Timestamp: {ts}
    Lon: {lon}
    Lat: {lat}
    """)
if __name__ == "__main__":
    main()

