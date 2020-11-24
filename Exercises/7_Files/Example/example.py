# file = open('schedule.txt')
# print(file)
# print('-'*10)
# print(file.read())
# print('-'*10)
# print(file.read())
# file.close()

# with open('schedule.txt') as file:
#     print(file.read())
#
# print('-'*10)

# with open('schedule.txt') as file:
#     line = file.readline()
#     while line:
#         if line != '\n':
#             print(line)
#         line = file.readline()
#
# print('-'*10)
#
# with open('schedule.txt') as file:
#     line = file.readline()
#     while line:
#         if line != '\n':
#             print(line.rstrip())
#         line = file.readline()
# with open('schedule.txt') as file:
#     line = file.readline()
#     while line:
#         if line != '\n':
#             record = line.split(';')
#             print(record[1])
#         line = file.readline()

# with open('kilometers.txt') as kilometers:
#     line = kilometers.readline().rstrip()
#     smallest = largest = int(line)
#     line = kilometers.readline().rstrip()
#     while line:
#         number = int(line)
#         if number > largest:
#             largest = number
#         else:
#             if number < smallest:
#                 smallest = number
#         line = kilometers.readline().rstrip()
# difference = largest - smallest
# print('The difference between te largest and the smallest number =', largest,'-',smallest,'=',difference)

# with open('schedule.txt') as file:
#     all_lines = file.readlines()
#     for line in all_lines:
#         if line != '\n':
#             print(line, end="")
#
# with open('schedule.txt') as file:
#     all_lines = file.readlines()
#     for line in all_lines:
#         if line != '\n':
#             test = ''.join(line.split())
#             print(test,'| ', end="")

# with open('schedule.txt') as file:
#     all_lines = file.readlines()
#     for line in all_lines:
#         if line != '\n':
#             record = line.split(';')
#             print(record[0], record[2].rstrip(), record[1], sep='\t')



