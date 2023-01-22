import random

def choice(a):
    if a == 1:
        return('Rock')
    elif a == 2:
        return('Paper')
    elif a == 3:
        return('Scizors')
    else:
        return('lose')

def text():
    print(f'\nHas escogido: {choice(user)}')
    print(f'PC ha usado: {choice(pc)}\n')

print('\nRock, paper, scizors game \n')
user = int(
    input('ingrese: \n 1 --- Rock \n 2 --- Paper \n 3 --- Scizors'))
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

