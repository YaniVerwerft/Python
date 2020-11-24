with open('Files Chapter 7/first_names.txt') as file:
    lines = file.readlines()
k = 0

while k < len(lines):
    print(lines[k].rstrip().ljust(13), sep='\t',end='')
    k += 1
    if k % 10 == 0:
        print(lines[k])

