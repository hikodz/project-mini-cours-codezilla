#?
#? lesson 7 - secret name

#qs_client = input('enter the name: ').lower()

#if qs_client.endswith('d'):
 #   print('you winnnn')
#else:
   # print('sorry your lost try again')    

#? lesson 7 - secret name part 2

intro_3 = 'it is the time to see is we could do better'
print(f'{intro_3}\n{"-"*30}')
number = float(input('enter the number: '))
divide = float(input('enter the number to divide by: '))

answer_client = input(f'{number} is divisible by {divide} yes or no?\n')
print('-'*30)

if (number % divide == 0 and answer_client == 'yes') or (number % divide != 0 and answer_client == 'no'): 
    print('Bravooooo')
else:
    print("no problem,let's try again")    
