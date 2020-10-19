number = int(input('Enter a number: '))
zeros = 0
sixes = 0
while number > 0:
    rest = number % 10
    number //= 10
    if rest == 0:
        zeros += 1
    else:
        if rest == 6:
            sixes += 1
print('The number consists of',zeros, 'zeros and', sixes, 'sixes')
