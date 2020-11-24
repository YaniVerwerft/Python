#0          1           2               3           4           5
# z-code;course name;student group;student nummer;surname;first name
output_file = open('students.csv', 'w', encoding='UTF-8')
with open('courses.csv') as file:
    for i in range(0,2):
        line = file.readline().rstrip()
    record = line.split(';')
    while line:
        snum =  record[3]
        whattowrite = snum+';'+record[4]+';'+record[5]
        while line and snum == record[3]:
            whattowrite += ';' + record[1]+' ('+record[2]+')'
            line = file.readline().rstrip()
            record = line.split(';')
        output_file.write(whattowrite+'\n')
output_file.close()




