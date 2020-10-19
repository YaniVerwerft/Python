price1 = 20
price12 = 50
price18 = 95

for i in range (0,4):
    print('Information for member',i+1)
    name = input('Name: ')
    age = int(input('Age: '))
    membertime = int(input('Member for how many years: '))
    if membertime >= 5:
        discount = 0.90
    else:
        discount = 1
    if age < 12:
        price = price1
    else:
        if age <= 18:
            price = price12
        else:
            price = price18
    print('Member fee for', name,'=',price*discount)
    print(' ')
