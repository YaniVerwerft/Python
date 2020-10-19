mylist = ['cat', 'dog', 'mouse', 'rat', 'squirel']

first = mylist[0]

mylist[0] = mylist[len(mylist)-1]
mylist[len(mylist)-1] = first

print(mylist)
