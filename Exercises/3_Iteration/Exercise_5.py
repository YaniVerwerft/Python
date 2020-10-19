number = int(input('Enter a number:'))
smallest = False
biggest = False
while number != 'Done':
    if number == 0:
        number = 'Done'
    else:
        if (number > biggest or biggest == False) or (number < smallest or number == False):

            if number > biggest or biggest == False:
                biggest = number
            else:
                smallest = number

        number = int(input('Enter a number:'))

if number == 'Done' and smallest == False:
    print('no numbers entered')
else:
    print('The difference between the largest number',biggest, 'and the smallest number',smallest, '=', biggest-smallest)

