mylist = ['cat', 'dog', 'horse', 'monkey', 'turtle', 'rabbit']
print('Original list:', mylist)
buffer = mylist[0]
del mylist[0]
mylist.append(buffer)

print('After sliding:', mylist)
