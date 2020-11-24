with open('first_names.txt') as file_in:
    lines = file_in.readlines()

lines.reverse()
for line in lines:
    print(line.rstrip())