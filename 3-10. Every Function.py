rivers = ['nemunas', 'neris', 'liffey']
print(rivers)

#Accessing Element in a List
print(rivers[0].title())
print(rivers[2].title())
print(rivers[1].title())

#Using Individual Values from a List
message = f"I live near {rivers[0].title()} river."
print(message)

#Appending Elements
rivers.append('volga')
print(rivers)

empty_list = []
empty_list.append('nemunas')
empty_list.append('neris')
empty_list.append('liffey')
print(empty_list)

#Inserting Element into List
vegetables = ['carrot', 'apple', 'lettuce']
vegetables.insert(3, 'brocoli')
vegetables.insert(0, 'cucumber')
print(vegetables)

#Removing Element from a List
vegetables = ['carrot', 'apple', 'lettuce']
del vegetables[1]
print(vegetables)

#pop() Method
vegetables = ['carrot', 'apple', 'lettuce']
popped_vegatables = vegetables.pop()
print(vegetables)
print(popped_vegatables)


