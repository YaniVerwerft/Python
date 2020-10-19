amount_of_inputs = 1
words = input("Enter word " + str(amount_of_inputs) + ":")
newstring = words.capitalize()

for amount_of_inputs in range(1,5):
    amount_of_inputs += 1
    newstring = input("Enter word " + str(amount_of_inputs) + ":").capitalize() + " " + newstring
print('The words in reverse order: ')
print(newstring)