
# Section 8: Python Conditionals & Lists
#list & string methods part 3

#! data user:
word_user = input('Enter a word: ')
print("-"*20)

#! use list:
lis_word = list(word_user)

#! use new method:
lis_word.reverse()

#! output:
list_to_str = ''.join(lis_word)
print(f'your reverse word is: {list_to_str}')

n = 4
if n == 8 and 9:
    print(1)
elif n == 3 or 6:
    print(2)
else:
    print(3)        