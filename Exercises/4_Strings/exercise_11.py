text = input("Enter a text: ")

for i in range(len(text)):
    if text[i] == "x":
        last_x = i
    if text[i] == "y":
        last_y = i
if last_y > last_x:
    print("all are followed")
else:
    print('they dont follow')
