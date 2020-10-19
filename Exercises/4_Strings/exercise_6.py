word = input('Enter a word: ')
word_length = len(word)
for i in range (0,word_length-2,3):
    print(word[i+1] + word[i+2] + word[i+0], end="" )

if word_length % 3 == 2:
    print(word[-2:])
else:
    if word_length % 3 == 1:
        print(word[-1])