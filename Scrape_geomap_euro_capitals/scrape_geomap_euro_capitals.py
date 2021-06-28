from urllib.request import urlopen
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
from folium.plugins import MarkerCluster


url = 'https://en.wikipedia.org/wiki/Template:Capital_cities_of_European_Union_member_states'
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

tbodies = soup.find_all('tbody')    # get all <tbody> tags)

countries_and_capitals = []
for i, tbody in enumerate(tbodies):
    if i == 0:
        pass
    else:
        tds = tbody.find('td')  # get 1st td from each tbody
        ahrefs = tds.find_all('a')  # get all <a> tags
        country = ahrefs[0]['title']
        capital = ahrefs[1]['title']
        print(country, capital)
        countries_and_capitals.append((country, capital))

geolocator = Nominatim(user_agent='map_scraped_capitals')

m = folium.Map()
for loc_tuple in countries_and_capitals:
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    country, capital = loc_tuple[0], loc_tuple[1]
    location = {'country': country, 'city': capital}
    coordinates = geocode(location)
    lat, lon = coordinates.point.latitude, coordinates.point.longitude
    tooltip = f'{country}: {capital}'
    folium.Marker([lat, lon], tooltip=tooltip).add_to(m)
m.save('european_capitals.html')
