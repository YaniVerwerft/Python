word = input('Enter a word: ')
position = word.find('in')
if position == -1:
    print("this word does not contain 'in'")
elif position in (0,1):
    print("'in' appears in the first or second place")
else:
    print("'in' appears in the ord but not in front")