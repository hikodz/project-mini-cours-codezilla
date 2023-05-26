#number_client = float(input("enter a number: "))
#divide_number = float(input('enter the number yo divide by: '))
#result = number_client / divide_number
#space = "-"*25
#print(f'{space}\nthe division result is {result: .3f}')
#if number_client % divide_number == 0:
    #print(f'{number_client} is divisible by {divide_number}')
#else:
    #print(f'{number_client} is not divisible by {divide_number}')

#? part 2 
#intro = 'please, enter the number you want to compare'
#space = '-' * 15
#print(f'{intro}\n{space}\n')
#first_number = float(input('enter the first number: '))    
#second_number = float(input('enter the second number: '))
#third_number = float(input('enter the third number: '))  
#print(space)

#if first_number > second_number and first_number > third_number:
#    print(f'{first_number} is the greatest number')
#elif second_number > first_number and second_number > third_number:
#    print(f'{second_number} is the greatest number')
#else:
#    print(f'{third_number} is the greatest number')    

# ? part 3

amount_of_money = float(input("enter the amount of money you have: "))
space = '-'*20

print(space)
first_items = float(input("enter the price of the first item: "))
second_items = float(input("enter the price of the second item: "))
third_items = float(input("enter the price of the third item: "))
print(space)

remaining_amount_client_card = amount_of_money - (first_items + second_items + third_items)
money_extra = (first_items+second_items+third_items) - amount_of_money


if first_items + second_items + third_items <= amount_of_money:
    print(f"items have been purchased successfuly\nthe remaining amount is {remaining_amount_client_card}$")
else:
    print(f"sorry, you dont't have enough balance\nyou need to add extra {money_extra: .2f}$")    





