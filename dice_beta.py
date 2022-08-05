import random
import time


def dice():
    player = random.randint(1, 6)
    ai = random.randint(1, 6)

    print(f'Player rolled: {player}')
    time.sleep(2)
    print(f'The computer rolled: {ai}')
    time.sleep(1)

    if player > ai:
        print(f'Player wins!')
        print()
    elif player == ai:
        print(f'Player and Computer have a tie.')
        print()
    else:
        print(f'Player loses.')
        print()

    print('Quit? Y/N')
    keepPlaying = input()

    if keepPlaying == 'Y' or keepPlaying == 'y':
        exit()
    elif keepPlaying == 'N' or keepPlaying == 'n':
        pass
    else:
        print('I do not understand. Playing again.')

while True:
    print('Press return to roll your dice.')
    roll = input()
    dice()

# scoring does not work correctly.

# probably need a system to keep track outside of the the function

# maybe a class for the player, a class for scoring, and a class for actual game play