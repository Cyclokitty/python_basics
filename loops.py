smallest = None
print('Before: ', smallest)
for itervar in [41, 12, 9, 3, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        # break
    print('Loop: ', itervar, smallest)
print('Smallest: ', smallest)