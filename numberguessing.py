#use ctrl + shift + M....to find problems in vs code workspace
import random

print('**Here is the NNUMBER GUESSING GAME \n')
print('you have to guess a number that is in range 1 to 50 and if teh number is same to the random number generated, the game ends....\n')
print('Game will continue till you guess the no correctly....\n')
print('if you want to quit enter "quit" ')


print('So lets BEGIN')

while True: 
    original=random.randint(1,51)
    guess=input('Enter your guess\n')
    print(f'\n my guess is {original}')
    if guess==original:
        print('you won\n')

    elif int(guess)>50:
        print('enter the number in range\n')

    elif guess != original:
        print('try again \n')

    else:
        print('entera valid input\n')
    


