def press_square(number,character):
    for i in range(number):
        print(character*number)

character = input("Which character must be used to form a square (ENTER = stop): ")

if character == "":
    print()
else:
    while character != "":
        number = int(input("Number of characters per line and number of lines: "))
        press_square(number, character)
        character = input("Which character must be used to form a square (ENTER = stop): ")