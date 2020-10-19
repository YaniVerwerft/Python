start = int(input('Initial limit: '))
end = int(input('Final limit: '))
if start > end:
    print('The initial limit must be smaller than the final limit!')
else:
    print('Sum of numbers from', start, 'till', end)
if start == end:
    print(start)
else:
    for i in range (start + 1 ,end + 1):
        print(i,'-->', start + i)
        start = start + i