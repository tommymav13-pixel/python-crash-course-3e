# to copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index. This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
my_foods = ['pizza', 'falafel', 'carrot cake', 'chicken wings', 'noodles', 'custard']
friend_foods = my_foods[:]

# to make sure they are copies, you can add a new item to each list. The two lists should be different after this.
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods) 

# Assignment 4-10
# Print slices of the list
print("\nThe first three items in my list are:")
print(my_foods[:3])

print("\nThree items from the middle of my list are:")
print(my_foods[2:5])

print("\nThe last three items in my list are:")
print(my_foods[-3:])    

# Assignment 4-12
# Write a for loop to print the items in each list. Make sure each food is printed in title case.
print("\nMy favorite foods are:")
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food.title()) 