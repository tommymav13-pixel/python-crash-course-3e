favorite_numbers = {
    'alice': [3, 9, 15],
    'bob': [5, 10, 20],
    'charlie': [6, 12, 18],
    'dave': [12, 24, 36],
    'eve': [7, 14, 21]
    }

for name, numbers in favorite_numbers.items():
    print(
        f"{name.title()}'s favorite number(s) is/are:" 
        f" {', '.join(str(num) for num in numbers)}")  
