# Section 8: Python Conditionals & Lists
#list & string methods part 1
# list of available vegetables
vegetables = ['broccoli', 'eggplant', 'carrot', 'cabbage',
'cucumber', 'potato', 'garlic', 'pepper']

#? intro user:
intro_user = 'Welcome at Codezilla Vegetables!'
print(intro_user)
veg_user = input('Enter the vegetable you want to get: ')
print("-"*40) 
#! use new method: 
convert_list = ', '.join(vegetables[:-1])
#! if data user:
if veg_user.lower() in vegetables:
    amount_veg = input('Enter the amount in kg: ')
    print(f'we wil get you {amount_veg} kg of {veg_user} very soon.')
else:
    print(f'sorry, we only have {convert_list} and {vegetables[-1]}')

