first = int(input("First number: "))
second = int(input("Second number: "))
five = False
same_number = False

if first < 0:
    first = -first
if second < 0:
    second = -second
if first % 5 == 0 and second % 5 == 0:
    five = True

if first > second:
    biggest = first
    smallest = second
else:
    if second > first:
        biggest = second
        smallest = first
    else:
        same_number = True


if same_number == True:
    print('The answer for the numbers ' + str(first) + ' and ' + str(second) + ' = 0')
else:
    if five == True:
        print('The answer for the numbers ' + str(first) + ' and ' + str(second) + ' = ' + str(smallest))
    else:
        print('The answer for the numbers ' + str(first) + ' and ' + str(second) + ' = ' + str(biggest))





