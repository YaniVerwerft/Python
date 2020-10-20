user_input = input('Enter a text:' )
input_list = []

for i in user_input:
    if i != " ":
        if i not in input_list:
            input_list.append(i)


input_list = sorted(input_list)
print(input_list)


for i in input_list:
    print(i, end=" ")
print()

for i in input_list:
    print(i, '\t', end=" ")
print()




