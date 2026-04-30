import random
import logging
guess = ''
toss=''
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
options= ('tails','heads')
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = str(input())

    toss = options[random.randint(0, 1)] # 0 is tails, 1 is heads
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guesss = str(input())
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')