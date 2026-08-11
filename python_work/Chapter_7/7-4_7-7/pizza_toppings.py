prompt = "\nPlease a topping you would like  on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"We will add {toppings.title()} to your pizza!")