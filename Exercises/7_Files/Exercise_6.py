import random
file_number = random.randint(1,10) # random = beide zitten erbij (1,10)

with open('Files Chapter 7/wish' + str(file_number) + '.txt') as file:
    print("Wish " + str(file_number), end="\n\n")
    line = file.readline()
    while line: # bij readline() = while line, bij readlines() = for want is list
        print(line.rstrip())
        line = file.readline()