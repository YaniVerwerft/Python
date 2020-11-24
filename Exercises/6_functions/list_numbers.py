#r0856502
#Verwerft Yani
#1ITF-10

first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
my_list = []
if first_number == second_number:
    print('Sorry, we can not create a list for you?')
else:
    if second_number < first_number:
        buffer = second_number
        second_number = first_number
        first_number = buffer
    for i in range(first_number,second_number):
        my_list.append(i)
    print(my_list)

