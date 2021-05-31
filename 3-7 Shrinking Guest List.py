# Invite some people to dinner.
guests = ['Toma By', 'Paul Reynold', 'Leonid Leonidovic']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry, " + name + " can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1, 'Eugenija An')

# Print the invitations one more time.
name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

# We got a bigger table. Add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'greta garbo')
guests.insert(2, 'reinhold messner')
guests.append('edith piaf')

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")

# You just found out that your new dinner table won’t
#arrive in time for the dinner, and you have space for only two guests.
print("\nI'm sorry, we can  invite only two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " I can’t invite you to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " I can’t invite you to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " I can’t invite you to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " I can’t invite you to dinner.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)

