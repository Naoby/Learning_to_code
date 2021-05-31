#Think of at least three kinds of your favorite pizza. Store these
#names in a list, and then use a for loop to print the name of each pizza.
favorite_pizzas = ['province', 'acapulco', 'santa fe']
for pizza in favorite_pizzas:
        print(pizza)

print("\n")
#Modify your for loop to print a sentence using the name of the pizza 
# instead of printing just the name of the pizza. For each pizza you should
#have one line of output containing a simple statement like I like pepperoni pizza.
for pizza in favorite_pizzas:
    print("I like " + pizza.title() + " pizza")

#Add a line at the end of your program, outside the for loop, that states
#how much you like pizza.
print("\nI really love pizza!")
