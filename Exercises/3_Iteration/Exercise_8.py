ending = int(input('What final digit do you want to check the numbers on: '))
counter = 0
for i in range (0, 10):
    digit = int(input('Enter number '+ str(i+1) + ': '))
    if digit % 10 == ending:
        counter += 1
print(counter, 'out of 10 numbers end on', ending)
