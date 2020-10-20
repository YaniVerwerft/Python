user_input = input('Enter a text:' )
input_list = []

for i in user_input:
    if i != " ":
        input_list.append(i)

print(input_list)

for i in input_list:
    print(i, end=" ")
print()

for i in input_list:
    print(i, '\t', end=" ")
print()




