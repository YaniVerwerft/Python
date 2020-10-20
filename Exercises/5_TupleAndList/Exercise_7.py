user_input = input('Enter a list of numbers: ')
number_list = []
final_list = []
for i in user_input:
    number_list.append(i)

for i in range (len(number_list)-1):
    for j in range (0, 2):
        final_list.append("0")
final_list.append("0")
final_list.append(user_input[-1:-2:-1])

print(final_list)