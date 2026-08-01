# to copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index. This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# to make sure they are copies, you can add a new item to each list. The two lists should be different after this.
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods) 
