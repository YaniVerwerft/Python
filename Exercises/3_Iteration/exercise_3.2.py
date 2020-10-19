your_age = int(input("How old are you: "))
fathers_age = int(input("How old is your father: "))
counter = 0

if your_age > fathers_age / 2:
    print("This situation is no longer possible for your ages")
while your_age * 2 != fathers_age:
    your_age += 1
    fathers_age += 1
    counter += 1
print("Within", counter, "years your father will have twice your age")
print("Your father will be", fathers_age, "and you will be", your_age)