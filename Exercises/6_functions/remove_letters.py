#r0856502
#Verwerft Yani
#1ITF-10

names = ['Yani', 'Jan', "Piet", "Joris", "Bobbie"]
print(names)
print()
to_be_removed = input('Enter the letter you want to remove. Press enter if you want to stop: ')

while to_be_removed != "":
    for i in range (len(names)):
        buffer = names[i]
        buffer = buffer.replace(to_be_removed, '')
        names[i] = buffer
    print(names)
    to_be_removed = input('Enter the letter you want to remove. Press enter if you want to stop: ')

