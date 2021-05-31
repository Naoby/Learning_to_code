#If you could invite anyone, living or deceased, to dinner, who
#would you invite? Make a list that includes at least three people you’d like to
#invite to dinner. Then use your list to print a message to each person, inviting
#them to dinner.

guests = ['Toma', 'Paul', 'Leonid']
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

#Start with your program from Exercise 3-4. Add a print() call at the end
#of your program stating the name of the guest who can’t make it.
name = guests[1].title()
print("Sorry, " + name + " can't make it t come.")

#Modify your list, replacing the name of the guest who can’t make it with
#the name of the new person you are inviting
guests = ['Toma', 'Paul', 'Leonid']
del (guests[1])
guests.insert(1, 'Vilis')

#Print a second set of invitation messages, one for each person who is still
#in your list.

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")





