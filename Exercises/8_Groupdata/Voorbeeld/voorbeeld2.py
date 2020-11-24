# Voorbeeld 2: we drukken de state af en voor elke stad het aantal inwoners.
# Op het einde van elke state vermelden we het grootst aantal inwoners in die state.
print('Top 50 cities in USA')
with open('US cities.csv') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        stateind = record[1]
        population_max = int(record[2])
        print(stateind)
        while line and record[1] == stateind:
            print('\t', record[0].ljust(20), record[2])  # ljust is een tip bij oefening 3 van Text files
if int(record[2]) > population_max:  # opgelet: int niet vergeten want hij vergelijkt ze anders als strings!
    population_max = int(record[2])
line = file.readline().rstrip()
record = line.split(';')
print('\t', 'Largest population in', stateind, '=', population_max)
