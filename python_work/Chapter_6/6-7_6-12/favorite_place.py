favorite_places = {
    'luffy': {
    'country': 'japan',
    'restaurant': 'AYCE',
    'city': 'amsterdam',
    },

    'zoro': {
    'country': 'germany',
    'restaurant': 'greek',
    'city': 'london',
    },

    'nami': {
    'country': 'america',
    'restaurant': 'chinese hotpot',
    'city': 'madrid',
    },

    'sanji': {
    'country': 'france',
    'restaurant': 'korean bbq',
    'city': 'new york',
    }
}

for username, user_info in favorite_places.items():
    print(f"\nName: {username.title()}")
    country = f"{user_info['country']}"
    restaurant = f"{user_info['restaurant']}"
    city = user_info["city"]

    print(f"\tFavorite country: {country.title()}")
    print(f"\tFavorite restaurant: {restaurant.title()}")
    print(f"\tFavorite city: {city.title()}")
