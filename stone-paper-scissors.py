import random
my_list=['stone','paper','scissors']
my_action=random.choice(my_list)

print('stone-paper-scissors\n')
print('*you will get 3 chances in that you have to beat me\n')
my_wincount=0
your_wincount=0


for i in range(0,3):
    my_action=random.choice(my_list)
    your_action=input('>>>Enter your action\n')
    print(f'{my_action}\n')
    if my_action==your_action:
        my_wincount=1
        your_wincount=1
        print('its a tie\n')
    elif my_action=='stone' and your_action=='scissors':
        my_wincount=1
        your_wincount=0
        print('you lost')
    elif my_action=='paper' and your_action=='stone':
        my_wincount=1
        your_wincount=0
        print('you lost')
    elif my_action=='scissors' and your_action=='paper':
        print('you lost')
        my_wincount=1
        your_wincount=0
    elif your_action not in my_list:
        print('you input is not valid')
    else:
        print('you won')
        my_wincount=0
        your_wincount=1


if my_wincount>your_wincount:
    print('OOPS..you lost')

elif my_wincount<your_wincount:
    print('HURREY..you won')

else:
    print('HMM..its a tie')
