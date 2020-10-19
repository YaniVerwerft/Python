my_age = int(input("Hold old are you: "))
father_age = int(input('How old is your father: '))

doubled = False
running_count = 0

while doubled == False:
    running_count += 1
    my_age += 1
    father_age +=1
    if father_age == my_age * 2:
        doubled = True
        print('Within', running_count, 'years your father will have twice your age')
        print('Your father will be',father_age,'and you will be', my_age)
    else:
        if my_age > father_age / 2:
            doubled = True
            print('The situation is no longer possible for your ages')

# if my age > father_age / 2 op voorhand doen zodat je dat meteen kan uitsluiten