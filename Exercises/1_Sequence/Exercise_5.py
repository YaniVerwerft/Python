#input
exchange_rate = float(input('Enter the current exchange dollar rate (€ -> $): '))
amount_of_euro = float(input('Enter your amount in euro: '))
#calculation
amount_of_dollar = amount_of_euro * exchange_rate
#print
print(str(amount_of_euro) + ' € = ' + str(amount_of_dollar) + ' $')
