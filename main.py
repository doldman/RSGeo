

from geopy.geocoders import GeoNames


geolocator = GeoNames(country_bias=None,username='', timeout=1, proxies=None)
geo = geolocator.geocode(query='French Equatorial Africa')

lat = geo.latitude
long = geo.longitude

print(lat,long,'\n')
print(geo.address)
