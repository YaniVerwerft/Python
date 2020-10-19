first = int(input('Number 1 (0, 1 or 2): '))
second = int(input('Number 2 (0, 1 or 2): '))
third = int(input('Number 3 (0, 1 or 2): '))

if first == second == third == 2:
    print("10")
else:
    if first == second and first == third:
        print('5')
    else:
        if second != first and third != first:
            print("1")
        else:
            print("0")