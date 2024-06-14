import utils_parcial_a as utils

print('Calculator TuttiCuadrati')

rooms = int(input('How many rooms does the property have?\n'))
bathrooms = int(input('How many bathrooms does the property have?\n'))
rooms ,bathrooms = utils.max_rooms (rooms , bathrooms)
inside_dimensions = utils.rooms_dimensions(rooms ,bathrooms)

social_area = input('Is the Social Area regular or premium? Enter "regular" or "premium":\n').strip().lower()
garage = input('Is the garage single or double? Enter "single" or "double":\n').strip().lower()
yard = input('Does the property have a yard? Enter "yes" or "no":\n').strip().lower()
outside_dimensions, garage = utils.outside_values(social_area,garage,yard)
price ,value_meter= utils.pricing (inside_dimensions + outside_dimensions, garage)
final_price = utils.discount(price)
house_dictionary = {key: [value1, value2] for key, value1, value2 in zip(utils.name,utils.size,utils.list_values(value_meter))}
price_dictionary = {}

price_dictionary['Inside'] = inside_dimensions * value_meter
price_dictionary['Outside'] = outside_dimensions * value_meter

print(final_price)
print(house_dictionary)
print(price_dictionary)