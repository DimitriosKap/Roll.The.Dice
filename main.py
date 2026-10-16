import random

while True:
    X = input('Roll a dice ? (yes/no); ').lower()
    if X == 'yes':
        dice = random.randint(1, 6)
        print(f'You rolled {dice} ')
    elif X == 'no':
        print('Maybe next time')
        break
    else:
        print('Please write yes or no')
