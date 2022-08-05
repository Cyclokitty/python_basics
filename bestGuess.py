# This is a guessing game. Player has 6 tries to get the 
# correct answer from the computer.

import random

secretNum = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1, 7):
    print('Take a guess: ')
    guess = int(input())

    if guess < secretNum:
        print('Your number is too low.')
    elif guess > secretNum:
        print('Your guess is too high.')
    else:
        break

if guess == secretNum:
    print(f'Good job! You guessed my number in {guessesTaken} guesses.')
else:
    print(f'Nope. The number I was thinking of was {secretNum}.')