import random

guess = ''
randomNum = random.randint(1, 100)

## print(randomNum)

print('Guess my secret number!')
## textGuess = input('Guess: ')
guess = int(input('Guess: '))

## print(guess)

if guess == randomNum:
    print(f'You are correct! Congrats! The secret number was {randomNum}')
else:
    print(f'Sorry, you are incorrect. The secret number is {randomNum}!')


