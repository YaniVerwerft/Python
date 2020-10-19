my_tuple = (1, 4, 3, 3, 5, 4, 6, 7, 8)
last_four_location = -1
for find_four in range (len(my_tuple)):
    if my_tuple[find_four] == 4:
        last_four_location = find_four

print(my_tuple)
if last_four_location == -1:
    print('The number 4 does not appear in the Tuple')
else:
    new_tuple = my_tuple[last_four_location + 1:]
    print(new_tuple)


#original solution: no new tuple

# print(my_tuple)
# if  last_four_location == -1:
#     print('The number 4 does not appear in the Tuple')
# else:
#     print(my_tuple[last_four_location + 1::])


# or use 'if 4 in my_tuple' print else...

# numbers = (1, 2, 3, 4, 5, 4, 6, 7, 8)
# index = 0
# print(numbers)
# if 4 in numbers:
#     for i in range(0,len(numbers)-1):
#         if numbers[i] == 4:
#             index = i
#     print(numbers[index + 1:])
# else:
#     print("the number 4 does not appear in the tuple")