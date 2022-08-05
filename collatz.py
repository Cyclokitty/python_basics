# This program explores the Collatz Sequence

def collatz(num):
    if num == 0:
        print(1)
        return 1
    if num % 2 == 0:
        print(num // 2)
        return num // 2
    else:
        print(3 * num + 1)
        return 3 * num + 1
            
while True:    
    try:
        number = int(input('Enter a number: '))
        break
    except ValueError:
        print('You must enter a number. Try again.')


isit1yet = collatz(number)

while True:
    if isit1yet == 1:
        break
    else:
        isit1yet = collatz(isit1yet)
