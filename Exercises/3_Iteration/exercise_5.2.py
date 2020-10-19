number = int(input('Enter a number:'))
smallest = number
biggest = number

if number == 0:
    print('No numbers entered')
while number != 0:
    if number < smallest:
        smallest = number
    else:
        if number > biggest:
            biggest = number
    number = int(input('Enter a number:'))
else:
    print('The difference between the largest number', biggest, 'and the smallest number', smallest, '=', biggest - smallest)