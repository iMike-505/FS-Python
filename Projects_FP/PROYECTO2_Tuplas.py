import getpass
import random


choice = ('Piedra', 'Papel', 'Tijeras')


def text():
    print(f'\nHas escogido: {choice[user - 1]}')
    print(f'PC ha usado: {choice[pc - 1]}\n')


print('\nRock, paper, scizors game \n')
user = int(
    input('ingrese: \n 1 --- Rock \n 2 --- Paper \n 3 --- Scizors ->'))
pc = random.randint(1,4)
if pc == user:
    text()
    print('Draw!')
elif(user == 1 and pc == 3) or (user == 2 and pc == 1) or (user == 3 and pc == 2):
    text()
    print('Win')
elif user not in range(1,4):
    text()
    print('You Lose')
else:
    text()
    print('Defeat')

getpass.getpass('press enter')
