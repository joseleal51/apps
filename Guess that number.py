import random

print('-------------------------------------')
print('      GUESS THAT NUMBER GAME')
print('-------------------------------------')
print()

the_number = random.randint(0, 10)

guess = -1
name = input ('Player what is your name?')
while guess != the_number:
    guess_text=input('Guess a number between 0 and 10: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {1}, your guess of {0} was too low.'.format(guess, name))
    elif guess > the_number:
        print('Sorry {1}, your guess of {0} was too high.'.format(guess, name))
    else:
        print('Excellent work {}, you won, it was {}!'.format(name, guess))

print ('done')