
# Stone, Paper, Scissor Game

import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'p':
            return True
        elif you == 'r':
            return False
    elif comp == 'p':
        if you == 'r':
            return True
        elif you == 's':
            return False
    elif comp == 'r':
        if you == 's':
            return True
        elif you == 'p':
            return False

# print('Comp Turn: Stone(s) Paper(p) Scissor(r)  ')

randno = random.randint(1, 3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 'r'

you = input('Your Turn: Stone(s) Paper(p) Scissor(r)  ')
g = gamewin(comp, you)

print(f'Comp chose: {comp}')
print(f'You chose: {you}')

if g == None:
    print('Tie!')
elif g:
    print('You Win!')
else:
    print('You Lose!')
