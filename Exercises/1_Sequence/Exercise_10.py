#input
day_consumption = int(input('Power consumption during the day (kilowatt per hour): '))
night_consumption = int(input('Power consumption at night (kilowatt per hour): '))
#calcs
fixed_costs = 83.6
price_day = day_consumption * 0.068
price_night = night_consumption * 0.035
total_ex_vat = price_day + price_night + fixed_costs
total_inc_vat = total_ex_vat*1.21
#prints
print('invoice')
print('*'*7)
print('Fixed costs: € ' + str(fixed_costs))
print('Day consumption: € ' + str(price_day))
print('night consumption: € ' + str(price_night))
print('Total excluding VAT: € ' + str(total_ex_vat))
print('Total including VAT: € ' + str(total_inc_vat))