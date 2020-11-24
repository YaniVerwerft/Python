def press_square(number,character):
    for i in range(number):
        print(character*number)

while True:
    character = input('give character, enter to stop: ')
    if character == "":
        break
    number = int(input('give number: '))
    press_square(number,character)




def loop():
    while True:
        character = input('give character, enter to stop: ')
        if character == "":
            return
        number = int(input('give number: '))
        press_square(number,character)
loop()





