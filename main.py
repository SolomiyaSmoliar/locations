# import folium
# file = 'C:/Users/Solomiya/Desktop/list.csv'
# lat = data['lat']
# lon = data['lon']
# m = folium.Map([48.314775, 25.082925],
#                 zoom_start=10)
# fg = folium.FeatureGroup(name='kosiv')

# for lt, ln in zip(lat, lon):
#     fg.add_child(folium.Marker(location=[lt,ln],
#                                 popup='1900',
#                                 icon = folium.Icon()))
# m.add_child(fg)
# m.save('C:/Users/Solomiya/Documents/Visual Studio/location/index.html')

def read_data(file:str) -> list:
    new_list = []
    file_ = open(file, 'r' )
    contents = file_.readlines()
    for line in contents[14:]:
        line_1 = []
        line = line.strip()
        line = line.split(',')
        first_line = line[0].replace('\t','')
        first_line = first_line.replace(') ','.')
        first_line = first_line.replace(')','.')
        first_line = first_line.replace('(','.')
        first_line = first_line.replace('}','.')
        first_line = first_line.replace('{','.')
        first_line = first_line.split('.')
        first_line[0] = first_line[0].replace('#', '')
        first_line[0] = first_line[0].replace(' ', '')
        line_1.append(first_line[0])
        line_1.append(int(first_line[1]))
        line_1.append(first_line[-1])
        new_list.append(line_1)
    return new_list

def similar_year_film(year:int, film_list:list) -> list:
    similar_year = []
    for i in film_list:
        if year in i:
            similar_year.append(i)
    return similar_year

def lenght_calculeting(latitude:float, longitude:float, film_list:list) -> list:


if __name__ == '__main__':
    file = 'C:/Users/Solomiya/Desktop/list.list'
    film_list = read_data(file)
    print(similar_year_film(2014, film_list))