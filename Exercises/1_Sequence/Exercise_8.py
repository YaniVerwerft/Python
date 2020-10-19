current_hour  = int(input('Enter the current hour: '))
waittime  = int(input('How long do you want to wait: '))
alarm = (current_hour+waittime)%24
print('The alarm will sound at ' + str(alarm) + 'h')