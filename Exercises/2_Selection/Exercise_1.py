user_input = int(input('Enter a number: '))
division_check = user_input%3

if division_check == 0:
    print(str(user_input) + ' is a triple')
else:
    print(str(user_input) + ' is not divisable by 3')