
### Section 8: Python Conditionals & Lists
#! Reversed word Game project :
# list of words
words = [
'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will',
'there',
'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into',
'could'
]
from random import randint
from time import time
# use method and data user from list game : 
intro_game = print(f'Welcome to the Reserved Words Game!\n{"-"*22}')

# use method randint in libery random:
take_word = randint(0, len(words)-1)
word_select = words[take_word]
lst_word = list(words[take_word])
lst_word.reverse()
join_word = ''.join(lst_word)
#----------------------
#use method time in libery time
star_time = time()
show_word = print(f'The reversed word is: {join_word}')
zone_user = input('The word is: ')
end_time = time()
print('-'*22)
result_time = end_time - star_time
#----------------------
# ! IF DATA USER : 
#! check if word user enter is correct : 
if zone_user != word_select:
    print('Worng word!')

#! check if time user < 6 : 
if result_time > 20:
    print('You took too long!')

#! result data won and lost user :
if zone_user == word_select and result_time <= 20:
    print('You won!')
else:
    print('You lost!')     