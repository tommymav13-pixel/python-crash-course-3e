#here are three different ways to generate a list of the first 10 multiples of 3, using a for loop, a for loop with append(), and a list comprehension.
threes = []
for value in range(3, 31):
    three = value * 3
    threes.append(three)
print(threes)

threes = []
for value in range(3, 31):
    threes.append(value * 3)
print(threes)   

threes = [value * 3 for value in range(3, 31)]
print(threes)   
