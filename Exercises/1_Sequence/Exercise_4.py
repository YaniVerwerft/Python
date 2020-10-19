#inputs
first_name = input('Enter the first name: ')
second_name = input('Enter the second name: ')
#print original values
print('Before changing: ' + first_name + ' ' + second_name)
#swap
buffer = first_name
first_name = second_name
second_name = buffer
#print swapped values
print('After changing: ' + first_name + ' ' + second_name)

# first_name, second_name = second_name, first_name | Alleen in python