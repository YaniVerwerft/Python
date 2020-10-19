word = input('Enter a word: ')
number = int(input('Enter a number: '))

first_letter = word[0]
last_letter = word[-number:]
print(first_letter + last_letter)