my_address = "Kleinhoefstraat 4 Geel"
address_string = []
#

for i in range (0, len(my_address), 5):
    if my_address[i] != ' ' and my_address[i] not in address_string:
        address_string.append(my_address[i].lower())
print(address_string)

while len(address_string) > 0:
    guessing = input('Still ' + str(len(address_string)) + ' letters to go: ')
    if guessing  in address_string:
        address_string.remove(guessing)

# j = 0
# what_to_guess = []
# while j < len(adress_string):
#     if adress_string[j] == " ":
#         what_to_guess = what_to_guess
#     else:
#         if what_to_guess.count(adress_string[j]) == 0:
#             what_to_guess += adress_string[j]
#     j += 5
#

# while len(what_to_guess) != 0:
#     if guessing not in what_to_guess:
#         guessing = input('Still ' + str(len(what_to_guess)) + ' letters to go: ')
#     else:
#         del what_to_guess[what_to_guess.index(guessing)]
#         guessing = input('Still ' + str(len(what_to_guess)) + ' letters to go: ')