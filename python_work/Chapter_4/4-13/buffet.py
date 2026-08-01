buffet_tuple = ('salad', 'soup', 'bread', 'pasta', 'dessert')
print("Original buffet menu:")
for item in buffet_tuple:
    print(item)

# buffet_tuple[0] = 'fruit'  # This will raise an error because tuples are immutable

buffet_tuple = ('fruit', 'soup', 'meat', 'pasta', 'dessert')  # Create a new tuple with the modified item
print("\nModified buffet menu:")
for item in buffet_tuple:
    print(item)

