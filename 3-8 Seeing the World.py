#Think of at least five places in the world you’d like to visit
locations = ['Spain', 'Dubai', 'Maldives', 'Iceland', 'Russia']
print(locations)

#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(locations))

#Show that your list is still in its original order by printing it.
print("\nHere is the original list again:")
print(locations)

#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print("\nHere is reversed alphabetical list:")
print(sorted(locations, reverse=True))

print("\nOriginal order:")
print(locations)

#Use reverse() to change the order of your list. Print the list to show that its order has changed.
print("\nReversed locations:")
locations.reverse()
print(locations)

#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
print("\nOriginal location order:")
locations.reverse()
print(locations)







