my_pizzas = ['pepperoni', 'mushroom', 'cheese']
for pizza in my_pizzas:
    print(pizza)
    print(f"I like {pizza} pizza.")
print("I really love pizza!")

#assignment 4-11
friends_pizzas = my_pizzas[:]

my_pizzas.append('hawaiian')  
friends_pizzas.append('veggie')

print("\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)