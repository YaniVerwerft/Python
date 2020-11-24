with open('weather_2018 10.csv', encoding='UTF-8') as file:
    for i in range(0,2):
        line = file.readline().rstrip()
    record = line.split(';')
    print('average temperatures: ')

    while line:
        amount_counter = 0
        total_temperature = 0
        split_first_field = record[0].split(' ')
        indicator = split_first_field[0]

        while line and indicator == split_first_field[0]:
            total_temperature += float(record[1])
            amount_counter += 1
            line = file.readline().rstrip()
            record = line.split(';')
            split_first_field = record[0].split(' ')
        average = total_temperature / amount_counter
        print(indicator, 'number of measurements = ', amount_counter,'\taverage = ',average)
    print('>' * 75)