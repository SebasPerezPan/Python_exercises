## dimensions: Height rooms, Width rooms, Bathrooms dimensions,total room dimensions, total bathroom dimensions, total dimensions

import functools
import matplotlib.pyplot as mp

name = []
size = []
price_part = []
price_graph = []

def list_names (number_elements,element):
    for i in range (number_elements):
        if number_elements > 1:
            name.append(f'{element} {i + 1}')
        else:
            name.append(f'{element}')

def max_rooms (rooms , bathrooms):
    quantity_rooms = lambda x : max(min(x,3),1)
    list_names (quantity_rooms(rooms),'room')
    list_names (quantity_rooms(bathrooms),'bathroom')
    return quantity_rooms(rooms), quantity_rooms(bathrooms)

def rooms_dimensions(quantity_room, quantity_bathroom):
    # height_rooms = []
    # width_rooms = []
    bathrooms = []
    for i in range(quantity_room):
        height_cycle = int(input(f'Height room {i+1} value:'))
        width_cycle = int(input(f'Witdh room {i+1} value:'))
        value = lambda x: max(min(x, 10), 2)
        # height_rooms.append(value(height_cycle))
        # width_rooms.append(value(width_cycle))
        size.append(value(height_cycle)+value(width_cycle))
    total_rooms = functools.reduce(lambda counter, item: counter + item, size)
    if quantity_bathroom == 1:
        bathrooms.append(9)
    else:
        for i in range(quantity_bathroom):
            bathrooms_cycle = input(f'Bathroom {i+1} is premium or regular?').strip().lower()
            if bathrooms_cycle == 'premium':
                bathrooms.append(9)
            else:
                bathrooms.append(6)
    size.extend(bathrooms)
    total_bathrooms = functools.reduce(lambda counter, item: counter + item , bathrooms)
    total = total_bathrooms + total_rooms
    ## height_rooms,width_rooms,bathrooms,total_rooms,total_bathrooms, 
    return total

def outside_values(social_area,garage,yard):
    if social_area == 'premium':
        pref_social_area = 'premium'
        social_area = 40
    else: 
        pref_social_area = 'regular'
        social_area = 20
    if garage == 'double':
        pref_garage = 'double'
        garage = 40
    else:
        pref_garage = 'single'
        garage = 20
    if yard == 'yes':
        yard_width = int(input('Insert the width'))
        yard_height = int(input('Insert the height'))
        yard = yard_height + yard_width
    else:
        yard = 0
    total_out = yard + social_area
    name.extend([f'social area {pref_social_area}','yard',f'garage {pref_garage}'])
    size.extend([social_area,yard,garage])
    return total_out , garage

def list_values(value):
    for i in range(len(size)):
        if int(i) == len(size) - 1:
            price_part.append(f'${size[i]*5000000:,}')
            price_graph.append(size[i] *5000000 )
        else:
            price_part.append(f'${size[i] * value:,}')
            price_graph.append(size[i] *value )
    return price_part, price_graph

def pricing (total_meters, garage):
    if total_meters > 100:
        value_meter = 9000000
    else:
        value_meter = 8000000
    return ((total_meters * value_meter) +(garage * 500000) * 1.25) , value_meter 

def discount (price_nodiscount):        
    if price_nodiscount > 1000:
        final_price = price_nodiscount * 0.95
    else:
        final_price = price_nodiscount
    return final_price

def grafico_pie(labels, values):
    fig, ax = mp.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    mp.show()
