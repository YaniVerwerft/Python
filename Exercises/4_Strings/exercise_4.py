word = input('Enter a word: ')
backwards = word[::-1]

if word == backwards:
    print(word,'is a palindrome.')
else:
    print(word,'is not a palindrome.')
