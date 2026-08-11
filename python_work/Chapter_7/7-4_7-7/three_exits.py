# version 1
prompt = "\nPlease enter a type of meat you would like on your pizza:"
prompt += "\n(Enter 'next' for cheese.) "

toppings = ""
while toppings != 'next':
    toppings = input(prompt)

    if toppings != 'next':
        print(f"We will add {toppings.title()} to your pizza!")

# version 2
prompt = "\nPlease enter a type of cheese you would like on your pizza:"
prompt += "\n(Enter 'next' for vegetables.) "

active = True
while active:
    toppings = input(prompt)

    if toppings == 'next':
        active = False
    else:
        print(f"We will add {toppings.title()} to your pizza!")


# version 3
prompt = "\nPlease enter a type of vegetable you would like  on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        print(f"Thank you! Your pizza will be ready.")
        break
    else:
        print(f"We will add {toppings.title()} to your pizza!")
