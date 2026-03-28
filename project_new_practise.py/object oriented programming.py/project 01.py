import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}: '))
        if guess < random_number:
            print ('sorry, a number is low. please trry again')
        elif guess > random_number:
            print ('oh, number is higher. try again')


    print('yay, you have guessed the {random_number} correctly.')

guess(10)
