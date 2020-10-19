number = int(input('Enter a number, stop by entering a zero: '))
product = 1
count = 0
while number != 0:
    product *= number
    count += 1
    number = int(input('Enter a number, stop by entering a zero: '))
print('The product of the ' + str(count) + ' numbers is ' + str(product))

