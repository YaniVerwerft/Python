#r0856502
#Verwerft Yani
#1ITF-10
counter = 0

print('Enter 5 codes consisting of a letter and a number:')

for i in range(5):
    print(i+1,end="")
    lookup = input(") ")
    character = lookup[0]
    number = int(lookup[1:])
    if ord(character) != number:
        print(character,'<-->', number)
    else:
        counter +=1
print(counter, 'codes were OK')