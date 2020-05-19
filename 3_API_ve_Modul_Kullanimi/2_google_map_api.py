################################################################
apiKey = "AIzaSyANfma6z67rXYaJHJhZgs0Zx2-hqs0kBo4"
################################################################
#https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood&key=YOUR_API_KEY
################################################################
# Şehir ismi verip, detaylı bilgiler almak
################################################################

# import googlemaps

# apiKey = "AIzaSyANfma6z67rXYaJHJhZgs0Zx2-hqs0kBo4"
# gm = googlemaps.Client(key = apiKey)
# geocode_result = gm.geocode('New York')[0]  # listedeki ilk sonucu al
# print(geocode_result)

################################################################
# This example uses the Geocoding API and the Directions API with an API key
################################################################
# import googlemaps
# from datetime import datetime
#
# gmaps = googlemaps.Client(key=apiKey)
#
# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# print("geocode_result:",geocode_result)
#
# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
# print("reverse_geocode_result:", reverse_geocode_result)
#
# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
# print(directions_result)

################################################################
#  Depremlerin koordinatları ve şiddetini listele
################################################################
# import gmaps.datasets
#
# gmaps.configure(api_key = apiKey)
# earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
# print(earthquake_df.head())

