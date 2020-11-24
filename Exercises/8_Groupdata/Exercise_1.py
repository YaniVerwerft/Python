with open('classrooms.txt') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        klas = record[2]
        llncounter = 0
        print(klas)
        while line and record[2] == klas:
            llncounter += 1
            naam = record[1] + ' ' + record[0]
            print('\t',naam)
            line = file.readline().rstrip()
            record = line.split(';')
        print('number of students in classroom',klas,'=', llncounter)



