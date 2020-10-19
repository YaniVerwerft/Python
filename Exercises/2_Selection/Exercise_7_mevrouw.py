number1 = int(input("First number: "))
number2 = int(input("Second number: "))

if number1 < 0:
    number1 = -number1

if number2 < 0:
    number2 = -number2

if number1 == number2:
    answer = 0
else:
    if number1 % 5 == 0 and number2 % 5 == 0:
        if number1 < number2:
            answer = number1
        else:
            answer = number2
    else:
        if number1 > number2:
            answer = number1
        else:
            answer = number2
print('The answer for the numbers', number1, 'and', number2, '=', answer)