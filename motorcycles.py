#Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

#Appending Elements to the End of a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

#Appending Elements to the Empty List
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles)

#Removing Elements from a List
motorcycles = ['honda','yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

#Removing an Item Using the pop() Method
motorcycles = ['honda','yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#Popping Items from any Position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('suzuki')
print(motorcycles)

#remove () method to work with a value

motorcycles = ['honda','yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is to expensive for me")
