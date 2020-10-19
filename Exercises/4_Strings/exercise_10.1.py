sentence = ''
for i in range(1,6):
    word = input('enter word ' + str(i) + ": ").capitalize()
    sentence = word + ' ' + sentence
print('The words in reverse order: ')
print(sentence)