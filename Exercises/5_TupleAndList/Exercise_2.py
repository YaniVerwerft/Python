mylist = [9, 17, 25, 4, 12, 7]
newlist = []


# for i in range (len(mylist)):
#     if mylist[i] % 2 != 0:
#         newlist.append(mylist[i])
#     else:
#         newlist.insert(0,mylist[i])
# print(newlist)

for digit in mylist:
    if digit % 2 != 0:
        newlist.append(digit)
    else:
        newlist.insert(0,digit)
print(mylist,'becomes',newlist)