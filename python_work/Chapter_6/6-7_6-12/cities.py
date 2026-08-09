cities = {
    'amsterdam': {
        'population': 'high',
        'country': 'netherlands',
        'fact': 'The Royal Palace on Dam Square alone is held up by 13,659 '
        'wooden poles.'
    },
    'london': {
        'population': 'normal',
        'country': 'engeland',
        'fact': 'The London Underground is the oldest underground railway '
        'system in the world.'
    },
    'madrid': {
        'population': 'normal',
        'country': 'spain',
        'fact': 'Madrid is the highest capital city in Europe, sitting 650 '
        'meters (2,133 feet) above sea level on a central plateau.'
    }
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    population = f"{city_info['population']}"
    country = f"{city_info['country']}"
    fact = city_info["fact"]

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population.title()}")
    print(f"\tFact: {fact.title()}")
