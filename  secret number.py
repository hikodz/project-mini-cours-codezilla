#? lesson 6 - secret number
# ? part1: tall

intro_1 = 'it is the time to see height differently'
print(intro_1)
h_cm = float(input('enter the height in cm: '))
print('-'*25)
if h_cm > 200:
    print(f'{h_cm} cm is considered very tall')
elif 180 < h_cm <200:
    print(f'{h_cm} cm is considered tall')
elif 160 < h_cm <180:
    print(f'{h_cm} cm is considered normal')
elif 150 < h_cm < 160:
    print(f'{h_cm} cm is considered short')
elif 150 > h_cm:
    print(f'{h_cm} cm is considered very short')


#? lesson 6 - secret number
# ? part2: game number
intro_2 = 'it is the time to see if we could do better'
print(intro_2)
print('-'*25)

number_kids = float(input('enter the number: '))
qs_kids = input(f'{number_kids} is even or odd?\n')

if number_kids % 2 == 0:
    if qs_kids == 'even':
        print('Bravoooooo')
    else:
        print("no probleme, let's try again")
else:
    if qs_kids == 'odd':
        print('Bravooooo')
    else:
        print("no probleme, let's try again")    