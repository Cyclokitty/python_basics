import random

secretNum = random.randint(1, 100)
guess = 0
guessing = 1

print(secretNum)

print('Welcome to Keep Guessing game. You have 5 tries to guess our Secret Number.')

guess = int(input('Make your guess: '))
while guessing < 5:    
    if guess != secretNum:
        print('Sorry that is incorrect.')
        print(f'You have {5 - guessing} tries left.')
        guess = input('Try another guess: ')
        guessing = guessing + 1
    elif guess == secretNum:
        print(f'Yes! The secret number is {secretNum}! Congrats!!')
        break
else:
        print(f'Sorry! You have used up your 5 tries. The secret number is {secretNum}.')
    


