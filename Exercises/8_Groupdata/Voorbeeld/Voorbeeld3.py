# Voorbeeld 3: als je het overzicht per state toch wil sorteren op het einde voor je print
print('Largest population (order by state name)')
states = []
with open('US cities.csv') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        stateind = record[1]
        population_max = int(record[2])
        while line and record[1] == stateind:
            if int(record[2]) > population_max:
                population_max = int(record[2])
            line = file.readline().rstrip()
            record = line.split(';')
        states.append(stateind + ': '+ str(population_max))
states.sort()
for state in states:
    print('\t'+state)