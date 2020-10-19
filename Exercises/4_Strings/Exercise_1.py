color = input('What is your favorite colour: ')
color_length = len(color)
counter = 0

print(color[0:3:2])

print('The colour consists of',color_length,'letters \n')

for i in range(0,color_length):
    print(color[i],'=', ord(color[i]))

print('\n')

while counter < color_length:
    if counter%2 != 0:
        print('**' + color[counter] + '**')
    else:
        print('#' + color[counter] + '#')
    counter += 1
