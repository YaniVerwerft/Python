number = int(input("Enter a number: "))

for i in range (number, 0, -1):
    print(number, '...', end=" ")
    number -= 1
print(number)