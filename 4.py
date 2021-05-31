#4-4 One Million: Make a list of the numbers from one to one million, and then
#use a for loop to print the numbers. 

List = []
for million in range (0, 10):
    print(million)

#4-5 Summing a Million : Make a list of the numbers from one to one million,
#and then use min(), max() ans sum()  

numbers = list(range(1, 1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6. Odd Numbers: 
even_numbers = list(range(2, 21, 2))
print(even_numbers)

#4-7 Threes
threes = list(range(3, 31, 3))

for number in threes:
    print(number)
