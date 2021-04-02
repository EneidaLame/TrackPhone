import phonenumbers
import folium
from myNumber import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
Key = "825fa16307ea45209b19c40f99abfab7"

samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)

#print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(lacation = [lat, lng], zoom_start = 9)

folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

myMap.save("myLocation.html")
