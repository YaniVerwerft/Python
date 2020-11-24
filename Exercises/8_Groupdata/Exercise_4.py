with open('sponsors.txt') as file:
    lines = file.readlines()
lines.sort()
print('Overview gifts')
print('Number \t Sponsor')
i=0
taxcounter = 0
record = lines[i].rstrip().split('*')
while i < len(lines):

    number = record[0]
    print(number, '\t', record[1], record[2], end='')
    total_donation = 0

    while i < len(lines) and number == record[0]:
        i += 1
        total_donation += int(record[3])
        if i < len(lines):
            record = lines[i].rstrip().split('*')
    if total_donation >= 40:
        print('\t',total_donation,'*'*2)
        taxcounter += 1
    else:
        print('\t',total_donation)

print('there are',taxcounter,'tax certificates to be sent.')





