#Input
digit_input = int(input("Enter a three-digit number: "))
#Calculations
half = digit_input / 2
double = digit_input * 2
third_power = digit_input ** 3
tenfold = digit_input * 10
#split
first_digit = digit_input // 100
second_digit = (digit_input - (first_digit*100)) // 10 #(number % 100) //10
third_digit = (digit_input%10) # (number % 100) % 10
#print
print('Half = ' + str(half))
print('Double = ' + str(double))
print('Third power = ' + str(third_power))
print('Tenfold = ' + str(tenfold))
print('The digits are:')
print(first_digit)
print(second_digit)
print(third_digit)