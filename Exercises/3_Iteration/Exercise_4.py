import random
number = random.randint(0,100)
hints = 0
guess = int(input('Enter a positive number: '))

while guess != number:
    hints += 1
    if guess < number:
        print('Higher!')
    else:
        print('Lower!')
    guess = int(input('Enter a positive number: '))
print('You have guessed the number',number,'in', hints,'turns')
