# strings & lists project part 1:
#!teste user :
word_user = input('Enter a word: ')
print('Does the word start with a vowel??🤨🤨🤨')
input_qs = input('').lower()

#!vowels: U,A,E,I,O :
vowels_ln = ['U', 'A', 'E', 'I', 'O']
print('-'*30)

#! if data user :
if word_user[0].upper() in vowels_ln and input_qs == 'yes':
    print(f'Bravoooo!👌👌👌\n{word_user} starts with a vowel')
elif not word_user[0].upper() in  vowels_ln and input_qs == 'no':
    print(f'Bravoooo!👌👌👌\n{word_user} does not start with a vowel')
else:
    print('Lets try again😀😀😀')    