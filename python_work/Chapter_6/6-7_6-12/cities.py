cities = {
    'amsterdam': {
        'population': 930_000,
        'country': 'netherlands',
        'fact': 'The Royal Palace on Dam Square alone is held up by 13,659 '
        'wooden poles.'
    },
    'london': {
        'population': 9_000_000,
        'country': 'engeland',
        'fact': 'The London Underground is the oldest underground railway '
        'system in the world.'
    },
    'madrid': {
        'population': 3_500_000,
        'country': 'spain',
        'fact': 'Madrid is the highest capital city in Europe, sitting 650 '
        'meters (2,133 feet) above sea level on a central plateau.'
    }
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation: {city_info['population']:,}")
    print(f"\tFact: {city_info['fact']}")
