import geopy
from geopy.geocoders import Nominatim
import pandas
import pprint
import time

df = pandas.read_csv("Resources/Calendar_ROA_2_20_2020.csv")
df["Address"] = df["MapLocation"] + ", " + df["Country"]

for address in df["Address"][1:]:
    try:
        locator = Nominatim(user_agent="myGeocoder")
        location = locator.geocode(address)
        df["Longitude"] = location.longitude
        df["Latitude"] = location.latitude
        time.wait(3)

    except:
        df["Longitude"] = "Error"
        df["Latitude"] = "Error" 

print(df.head())