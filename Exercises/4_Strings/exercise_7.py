word = input('Enter a text: ')
word_length = len(word)
counter = 1
highest = 1
for i in range(word_length-1):
    if word[i] == word[i+1]:
        counter += 1
        if counter > highest:
            highest = counter
    else:
        counter = 1

print('The length of the largest block in this text is',highest)