bottle = int(input("How many bottles of wine are there: "))
pizza = int(input("How many pizzas are there: "))

if bottle < 5 or pizza < 5:
    print('This is just a stupid party')
else:
    if bottle / pizza > 2 or pizza / bottle > 2:
        print("This is a fantastic party")
    else:
        print('This is a good party')