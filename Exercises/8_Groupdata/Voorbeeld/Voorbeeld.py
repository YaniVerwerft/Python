print('Top 50 cities in USA')
with open('US cities.csv') as file:
    line = file.readline().rstrip()
    record = line.split(';')
    while line:
        stateind = record[1]
        city_counter = 0
        print(stateind)
        while line and record[1] == stateind:
            city_counter += 1
            print('  ' + str(city_counter) + ') ' + record[0])
            line = file.readline().rstrip()
            record = line.split(';')