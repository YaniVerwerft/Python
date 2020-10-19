print('Please give me 3 numbers.')
first = int(input('Number 1: '))
second = int(input('Number 2: '))
third = int(input('Number 3: '))
running_lowest = first
if second < running_lowest:
    running_lowest = second
if third < running_lowest:
    running_lowest = third

#if first < second:
#   running_lowest = first
#else:
#    if second < third:
#        running_lowest = second
#    else:
#        running_lowest = third


print('The smallest number is: ' + str(running_lowest))
