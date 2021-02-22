import folium
from geopy.geocoders import Nominatim
from haversine import haversine
import math
geolocator = Nominatim(user_agent='Location')

tooltip = 'Click fot more info'


def read_data(file: str) -> list:
    '''
    Reads the file and returns a list of movies.
    '''
    new_list = []
    file_ = open(file, 'r')
    contents = file_.readlines()
    for line in contents[14:]:
        line_1 = []
        line = line.strip()
        line = line.split(',')
        first_line = line[0].replace('\t', '')
        first_line = first_line.replace(') ', '.')
        first_line = first_line.replace(')', '.')
        first_line = first_line.replace('(', '.')
        first_line = first_line.replace('}', '.')
        first_line = first_line.replace('{', '.')
        first_line = first_line.split('.')
        first_line[0] = first_line[0].replace('#', '')
        first_line[0] = first_line[0].replace(' ', '')
        line_1.append(first_line[0])
        line_1.append(int(first_line[1]))
        line_1.append(line[1])
        new_list.append(line_1)
    return new_list


def similar_year_film(year: int, film_list: list) -> list:
    '''
    Finds movies with the same year of release.
    >>> similar_year_film(2015, [['"Elmira"', 2015, ' New York'], ['"ATown"', 2014, ' Austin']])
    [['"Elmira"', 2015, ' New York']]
    '''
    similar_year = []
    for i in film_list:
        if year in i and i not in similar_year:
            similar_year.append(i)
    return similar_year


def lenght_calculeting(latitude: float, longitude: float, film_list: list) -> list:
    '''
    The distance between the location where the movie was shot and the person.
    And returns the first ten that are the shortest.
    >>> lenght_calculeting(49.83826, 24.02324, [['"Elmira"', 2014, ' New York']])
    [['"Elmira"', 2014, ' New York', (40.7127281, -74.0060152), 7174.30658729592]]
    '''
    location = (latitude, longitude)
    for i in film_list:
        adress = coordinates(i[-1])
        location_2 = (adress[0], adress[1])
        i.append(adress[-1])
        lenght = haversine(location, location_2)
        i.append(location_2)
        i.append(lenght)
    film_list.sort(key=lambda x: x[-1])
    return film_list[:10]


def coordinates(city: str) -> list:
    '''
    Returns the coordinates of the city where the movie was shot.
    >>> coordinates(' New York')
    (40.7127281, -74.0060152)
    '''
    location = geolocator.geocode(city)
    adress = location.address
    adress = adress.split(',')
    return location.latitude, location.longitude, adress[-1]


def map_generator(latitude: float, longitude: float, year: int, file_: str):
    '''
    Generates a map and places markers on it with cities where movies were shot.
    '''
    colors = ['red', 'blue', 'purple', 'orange', 'darkblue',
              'darkgreen', 'cadetblue', 'darkpurple', 'pink', 'lightblue']
    film_list = read_data(file_)
    similar = similar_year_film(year, film_list)
    result = lenght_calculeting(latitude, longitude, similar)
    m = folium.Map()

    first_layear = folium.FeatureGroup(name='first_layear')

    first_layear.add_child(folium.Marker(location=[latitude, longitude],
                                         popup='I am hear',
                                         tooltip=tooltip,
                                         icon=folium.Icon(color='green', icon="home", prefix='fa')))

    for i in range(len(result)):
        col = colors[i]
        lt, ln = result[i][4]
        first_layear.add_child(folium.Marker(location=[lt, ln],
                                             popup=result[i][0],
                                             tooltip=tooltip,
                                             icon=folium.Icon(color=col, icon='cloud')))
    m.add_child(first_layear)

    second_layer = folium.FeatureGroup(name="Countries")
    second_layer.add_child(folium.GeoJson(data=open('C:/Users/Solomiya/Desktop/World_Countries__Generalized_.geojson', 'r',
                                                                                            encoding='utf-8-sig').read(),
                                                                                            style_function=lambda x: {'fillColor':'green'
                                                                                            if x['properties']['COUNTRY'] in result[i][3]
                                                                                            else 'blue'}))
    m.add_child(second_layer)
    m.save('index.html')
    pass


if __name__ == '__main__':
    file_ = 'location.list'
    year = int(input('Please enter a year you would like to have a map for: '))
    lat = float(input('Please enter your latitude: '))
    lon = float(input('Please enter your longitude: '))
    print('Map is generating...')
    print('Please wait ...')
    map_generator(lat, lon, year, file_)
    print('Finished. Please have look at the map index.htm')


