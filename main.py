

from geopy.geocoders import GeoNames


geolocator = GeoNames(country_bias=None,username='', timeout=1, proxies=None)
geo = geolocator.geocode(query='nubia')

lat = geo.latitude
long = geo.longitude

print(lat,long,'\n')
print(geo.address)


#Note that in wikidata the instance of (P31) is geographic region which has sub properties classes (P279) of geographic location and geographic object
#note that Egyptian place hierarchies use physical things as locations - for example tomb of. In addition some locations are not properely separated, like nubia africa > africa.
# e.g why is africa repeated at the region level when it is at the country level.