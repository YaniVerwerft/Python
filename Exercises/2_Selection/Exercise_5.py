number = int(input('Enter a number: '))

if number <= 0:
    print('Negative number will not be tested')
else:
    digit  = int(input('what final digit do you want to test'))
    if number % 10 == digit:
        print(number,'ends with, digit')
    else:
        print(number,'does not end with',digit)