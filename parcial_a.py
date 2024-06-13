import functions.utils_parcial_a as utils

print('Calculator TuttiCuadrati')

inside_house_dimensions = utils.inhouse()
outside_house_dimensions, garage_dimension = utils.outhouse()
value_meter = 0
equisde = inside_house_dimensions + outside_house_dimensions
if (inside_house_dimensions + outside_house_dimensions) > 100:
    value_meter = 9
else:
    value_meter = 8
price_before_discount = ((inside_house_dimensions + outside_house_dimensions) * value_meter) + (garage_dimension * 5)     
    
if price_before_discount > 1000:
    final_price = price_before_discount * 0.95
else:
    final_price = price_before_discount
print(f'Final price is: ${final_price}.000.000')