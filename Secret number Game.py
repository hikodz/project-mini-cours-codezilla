# Section 8: Python Conditionals & Lists
# Secret number Game project part 1 :

# ! Before chatgpt: 
from random import randint
# use method randint() :
winner_number_1 = randint(1, 20)
winner_number_2 = randint(1, 20)
winner_number_3 = randint(1, 20)
winner_number_4 = randint(1, 20)
list_winner = [winner_number_1, winner_number_2, winner_number_3, winner_number_4]
print(list_winner)
num_user = int(input('Enter a number between \'1 and 20\': '))

# if data user
if 1 <= num_user <= 20:
    if num_user in list_winner:
        print('You won!')
    else:
        print('You lost!')
else:
    print('Please nter a number between \'1 and 20\'!') 

# ! After use chatgpt   
winners = []
for i in range(4):
    winner = randint(1, 20)
    winners.append(winner)  

print(winners)
num_user = int(input('Enter a number between \'1 and 20\': '))

# if data
if 1 <= num_user <= 20:
    if num_user in winners:
        print('You won!')
    else:
        print('You lost!')
else:
    print('Please nter a number between \'1 and 20\'!')

# Section 8: Python Conditionals & Lists
# Secret number Game project part 1 :

# ! Before chatgpt:
from random import randint
# use method randint() :
winner_number_1 = randint(1, 20)
winner_number_2 = randint(1, 20)
winner_number_3 = randint(1, 20)
winner_number_4 = randint(1, 20)
list_winner = [winner_number_1, winner_number_2, winner_number_3, winner_number_4]
print(list_winner)
num_user = int(input('Enter a number between \'1 and 20\': '))

# if data user
if 1 <= num_user <= 20:
    if num_user in list_winner:
        print('You won!')
    else:
        print('You lost!')
else:
    print('Please nter a number between \'1 and 20\'!')

## Section 8: Python Conditionals & Lists
## Secret number Game project part 1 :
from random import randint
# input user data
coin_guess = randint(1, 2)
print(coin_guess)
user_choose = int(input('Guess the coin flip!\nEnter\n1 for Heads\n2 for Tails\n'))
print('-'*20)
# if data
if 1 <= user_choose<= 2:
    if coin_guess == 1 and coin_guess == user_choose:
        print('the coin is Heads\nYou Won!')
    elif coin_guess == 2 and coin_guess == user_choose:
        print('the coin is Tails\nYou Won!')
    elif coin_guess == 2 and coin_guess != user_choose:
        print('the coin is Tails\nYou Lost!')
    elif coin_guess == 1 and coin_guess != user_choose:
        print('the coin is Heads\nYou Lost!')     
else:
    print('Please enter 1 or 2')               


### Section 8: Python Conditionals & Lists
### Secret number Game project part 1 :
from random import randint
# ! USE METHOD RANDINT():
user_guess = randint(1, 6)
print(user_guess)
messege_user = '''Guess the Roll Dice!
Enter a number between 1 and 6
'''
guess = int(input(messege_user))
print('-'*20) 

# !IF DATA:
if 1 <= guess <= 6:
    print(f'The Dice is {user_guess}') 
    if user_guess == guess:
        print('YOU WON!')
    else:
        print('YOU LOST!')      
else:
    print('Please Enter a number between 1 and 6')
