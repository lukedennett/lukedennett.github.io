import pandas

df = pandas.read_csv("Resources/Calendar_ROA_2_20_2020.csv")


df["Js"] = 'L.marker([' + str(df["Longitude"]) + ',' + str(df["Latitude"]) + ']).addTo(mymap).bindPopup("<b>' + df["Name"] + '</b><br />' + df["MapLocation"] + ', ' + df["Country"] + '").openPopup();'



    
df.to_csv("Resources/Js.csv")