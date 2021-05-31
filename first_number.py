for value in range(1, 6):
    print(value)

#Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

#even_numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#squares function
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)
