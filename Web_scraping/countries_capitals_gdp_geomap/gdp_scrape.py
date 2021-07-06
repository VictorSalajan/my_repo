from urllib.request import urlopen
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import numpy as np
from os import path
from unidecode import unidecode

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita'
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

trs = soup.find_all('tr')
countries = []
gdp_per_capita = []
for i, tr in enumerate(trs):
    tds = tr.find_all('td')
    for j, td in enumerate(tds):
        # Scrape Countries
        if td.get('scope'):
            country = td.find('a')['title']
            countries.append(country)
        # Scrape GDP
        elif len(countries) > 0 and len(gdp_per_capita) < len(countries):
            if '2019' == td.contents[0]:
                gdp = tds[j-1].contents[0]
                gdp_per_capita.append(gdp)
                break
            elif td == tds[-1]:
                gdp_per_capita.append(np.nan)
                break


d = {'country': countries, 'gdp_per_capita': gdp_per_capita, 'capital': np.nan}
df = pd.DataFrame(data=d)

# Scrape capitals
url = 'https://www.worlddata.info/capital-cities.php'
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

rows = soup.find_all('tr')

df['country'] = df['country'].apply(lambda x: unidecode(x))
df.loc[df['country']=='Macau', ['country']] = 'Macao'
df.loc[df['country']=='Czech Republic', ['country']] = 'Czechia'
df.loc[df['country']=='Georgia (country)', ['country']] = 'Georgia'

countries_and_capitals = []
for row in rows:
    table_data = row.find_all('td')
    try:
        country = table_data[0].find('a').contents[0]
        capital = table_data[1].contents[0]
        if any(country in c for c in df.country.to_list()):
            index = df.index[df['country'].str.contains(country)]
            df.loc[index, 'capital'] = capital
    except:
        pass

pd.set_option('display.max_rows', None)
print(df)

geolocator = Nominatim(user_agent='map_scrape_gdp')
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

if not(path.exists('gdp_per_capita.html')):
    m = folium.Map()
    print('This may take a while, due to the usage policy of the geomapping API...')
    for country, capital, gdp in zip(df.country, df.capital, df.gdp_per_capita):
        location = {'country': country, 'city': capital}
        try:
            coordinates = geocode(location)
            lat, lon = coordinates.point.latitude, coordinates.point.longitude
        except:
            coordinates = geocode(country)
            lat, lon = coordinates.point.latitude, coordinates.point.longitude
        tooltip = f'{country}, {capital}: ${gdp}'
        folium.Marker([lat, lon], tooltip=tooltip).add_to(m)
    m.save('gdp_per_capita.html')

df.to_csv('countries_capitals_gdp_per_capita.csv')
