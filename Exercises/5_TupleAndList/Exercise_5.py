my_list = [42, 18,17, 0, 37, 0, 2, 19, 20, 5, 14,0]

print(my_list)

for i in range(len(my_list)-1):
    if my_list[i] == 0:
        largest_odd = 0
        my_list[i] = largest_odd
        for j in range(i+1,len(my_list)-1):
            if my_list[j] > largest_odd and my_list[j] %2 != 0:
                largest_odd = my_list[j]
        my_list[i] = largest_odd

print(my_list)


# # numbers = [42, 18, 0, 37, 0, 2, 19, 20, 5, 14]
# numbers = [42, 18, 17, 0, 2, 19, 0]
# print(numbers)
# for index in range(len(numbers) - 1):
#     if numbers[index] == 0:
# # search largest_odd
# largest_odd = 0
# for i in range(index + 1, len(numbers) - 1):
#     if numbers[i] > largest_odd and numbers[i] % 2 != 0:
#         largest_odd = numbers[i]
# numbers[index] = largest_odd
# print(numbers)
