age = input("We will tell you the price of the ticket. How old are you? ")
age = int(age)

if age >= 12:
    print("\nThe ticket is €15!")
elif age >= 3:
    print("\nThe ticket is €10")
else:
    print("\nThe ticket is free")