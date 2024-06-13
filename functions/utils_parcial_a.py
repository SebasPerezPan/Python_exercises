## inside: Quantity rooms, Quantity bathrooms.
## dimensions: Height rooms, Width rooms, Bathrooms dimensions,total room dimensions, total bathroom dimensions, total dimensions

import functools

def inhouse():
    inside = inside_house()
    room, bathroom = inside
    dimensions = rooms_dimensions(room, bathroom)
    return dimensions[5]

def inside_house ():
    quantity_rooms = lambda x : max(min(x,3),1)
    rooms = int(input('How many rooms does the property have?\n'))
    bathrooms = int(input('How many bathrooms does the property have?\n'))
    return quantity_rooms(rooms), quantity_rooms(bathrooms)
    
def rooms_dimensions(quantity_a, quantity_b):
    height_rooms = []
    width_rooms = []
    bathrooms = []
    for i in range(quantity_a):
        height_cycle = int(input(f'Height room {i+1} value:'))
        width_cycle = int(input(f'Witdh room {i+1} value:'))
        value = lambda x: max(min(x, 10), 2)
        height_rooms.append(value(height_cycle))
        width_rooms.append(value(width_cycle))
    
    if quantity_b == 1:
        bathrooms.append(9)
    else:
        for i in range(quantity_b):
            bathrooms_cycle = input(f'Bathroom {i+1} is premium or regular?').strip().lower()
            if bathrooms_cycle == 'premium':
                bathrooms.append(9)
            else:
                bathrooms.append(6)

    total_bathrooms = functools.reduce(lambda counter, item: counter + item , bathrooms)
    height_width = height_rooms + width_rooms
    total_rooms = functools.reduce(lambda counter, item: counter + item, height_width)
    total = total_bathrooms + total_rooms

    return height_rooms,width_rooms,bathrooms,total_rooms,total_bathrooms, total

def outhouse():
    social_area = input('Is the Social Area regular or premium? Enter "regular" or "premium":\n').strip().lower()
    garage = input('Is the garage single or double? Enter "single" or "double":\n').strip().lower()
    yard = input('Does the property have a yard? Enter "yes" or "no":\n').strip().lower()

    if social_area == 'premium':
        social_area = 40
    else: 
        social_area = 20
    if garage == 'double':
        garage = 40
    else:
        garage = 20
    if yard == 'yes':
        yard_width = int(input('Insert the width'))
        yard_height = int(input('Insert the height'))
        yard = yard_height + yard_width
    else:
        yard = 0
    total_out = yard + social_area
    
    return total_out , garage