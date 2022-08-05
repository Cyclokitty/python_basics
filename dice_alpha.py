import random

player = random.randint(1, 6)
ai = random.randint(1, 6)

print(f'Player rolls: {player}')
print(f'Ai rolls: {ai}')

if player > ai:
    print('You win!')
elif player == ai:
    print('You tied.')
else:
    print('You lose.')

