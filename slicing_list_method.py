#Looping trough a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])

#Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

my_foods.append('cannoli')
friends_foods.append('ice cream')
print("\nMy friend's favorite food are:")
print(friends_foods)