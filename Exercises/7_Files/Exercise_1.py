with open('Files Chapter 7/first_names.txt') as file:
    line = file.readline()
    name_count = 0
    z_count = 0
    while line:
        name_count += 1
        if line.lower().count('z') > 0:
            print(line.rstrip())
            z_count += 1
        line = file.readline()
print('There are', name_count, 'first names')
print('There are',z_count,'of which contain a letter z.')