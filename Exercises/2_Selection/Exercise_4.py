first = int(input("number 1 :"))
second = int(input("number 2 :"))
third = int(input("number 3 :"))

if first + second == third:
    print('this works')
else:
    if first + third == second:
        print('this works')
    else:
        if second + third == first:
            print('this works')
        else:
            print("This won't work")
