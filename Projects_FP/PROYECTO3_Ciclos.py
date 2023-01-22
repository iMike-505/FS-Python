import getpass
import random

choice = {1: 'Piedra', 2: 'Papel', 3: 'Tijeras'}
draw = True


def text():
    print(f'\nHas escogido: {choice.get(user)}')
    print(f'PC ha usado: {choice[pc]}\n')


while draw == True:

    print('\nRock, paper, scizors game \n')
    user = int(
        input('ingrese: \n 1 --- Rock \n 2 --- Paper \n 3 --- Scizors ->'))
    pc = random.randint(1,4)
    if pc == user:
        text()
        draw = True
        print('Draw!')
    elif(user == 1 and pc == 3) or (user == 2 and pc == 1) or (user == 3 and pc == 2):
        text()
        draw = False
        print('Win')
    elif user not in range(1,4):
        text()
        draw = False
        print('You Lose')
    else:
        text()
        draw = False
        print('Defeat')

getpass.getpass('press enter')
