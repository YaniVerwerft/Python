text = input("Enter a text: ")
gevolg = True
for i in range(len(text)):
    if text[i] == 'x':
        if text[i:].find("y") == -1:
            gevolg = False
if not gevolg:
    print('not')
else:
    print('yes')

