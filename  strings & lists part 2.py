#Section 8: Python Conditionals & Lists
#lesson 15 - strings & lists part 2
#! strings & lists project part 2:
# input user data
full_name = input('Enter your full name: ').strip().title()
birth_date = input('Enter your birth date (dd-mm-yyyy): ')
current_year = int(input('Enter the current year: '))
print('-'*30)

#edit name user
edit_name_user = full_name.index(' ')
# print intro
print(f'Hello, {full_name[:edit_name_user]}!\nWelcome at age calculator') 
print('-'*30)

# calculator age:
cal_age =  current_year - int(birth_date[-4:])
print(f'your age is: {cal_age}')
#*-----------------------------------------------
#Section 8: Python Conditionals & Lists
#lesson 15 - strings & lists part 2
#! strings & lists project part 3:
# getting inputs
first_num, operator, second_num = input('Enter The Operation: ').split()
print('-'*20)
# convert to float
first_num = float(first_num)
second_num = float(second_num)
# check the operator and do the operation
if operator=='+':
    operation_name = 'Addition'
    result = first_num + second_num
elif operator=='-':
    operation_name = 'Subtraction'
    result = first_num - second_num
elif operator=='*':
    operation_name = 'Multiplication'
    result = first_num * second_num
elif operator=='/':
    operation_name = 'Division'
    result = first_num / second_num
elif operator=='**':
    operation_name = 'Power'
    result = first_num ** second_num
# print the result
print(f'{operation_name} result is {result:,.2f}')