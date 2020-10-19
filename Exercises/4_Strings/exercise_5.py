word = input('Enter a text: ')
word_length = len(word)-2
counter = 0
for i in range(0,word_length):
    if word[i] == word [i+1] and word[i] == word[i+2]:
        counter += 1
if counter == 0:
    print('There are no triples in this text')
else:
    if counter == 1:
        print('There is 1 triple in this text')
    else:
        print('There are',counter,'triples in this text')
