def make_car(manufacturer, model, **car_info):
    """Return a dictionary of information about a car."""
    car = {
        'manufacturer': manufacturer, 
        'model': model,
    }
    
    for key, value in car_info.items():
        car[key] = value
    return car

car_1 = make_car(
    'subaru',
    'outback',
    color='blue',
    tow_package=True,
)

car_2 = make_car(
    'audi',
    'hatchback',
    color='green',
)

car_3 = make_car(
    'tesla',
    'model 3',
    color='red',
    electric=True,
    doors=4,
    autopilot=True,
)

print(car_1)
print(car_2)
print(car_3)