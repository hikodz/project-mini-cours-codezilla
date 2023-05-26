#? lesson 8 - grades
#? lesson 8 - grades project: file 2: part1
#data
#? calculate BMI
# BMI = weight (kg) / height (m)²
#? ratings BMI
#Underweight: BMI less than 18.5
#Normal weight: BMI between 18.5 and 24.9
#Overweight: BMI between 25 and 29.9
#Obesity (Class 1): BMI between 30 and 34.9
#Obesity (Class 2): BMI between 35 and 39.9
#Extreme obesity (Class 3): BMI of 40 or higher
#data user
height_cm = float(input('enter height in cm: '))
weight_kg = float(input('enter weight in kg: '))
print('-'*25)
# calculate BMI
result_BMI = weight_kg / ((height_cm/100)**2)
#if data
if 0 <= result_BMI < 18.5:
    rating_BMI = 'Underweight'
elif 18.5 <= result_BMI <=24.9:
    rating_BMI = 'Normal weight'
elif 25 <= result_BMI <=29.9:
    rating_BMI = 'Overweight' 
elif 30 <= result_BMI <=34.9:
    rating_BMI = 'Obesity (Class 1)'
elif 35 <= result_BMI <=39.9:
    rating_BMI = 'Obesity (Class 2)'
else:
    rating_BMI = 'Extreme obesity (Class 3)'
print(f'your BMI is {result_BMI: .2f} which is considered as {rating_BMI}')

#lesson 8 - grades project: file 2: part2
#*data shop
sales_70 = ['070', '170', '270', '370', '470']
sales_50 = ['050', '150', '250', '350', '450']
sales_30 = ['030', '130', '230', '330', '430']
# input
code_items = input('enter the code of the item: ')
price_items = float(input('enter the price of the item: '))

#* result sold
sold_70 = price_items - (price_items * 0.7) 
sold_50 = price_items - (price_items * 0.5)
sold_30 = price_items - (price_items * 0.3)
# if result user
if code_items in sales_70:
    sold = '70.0%'
    price = sold_70
    code_print = code_items
elif code_items in sales_50:
    sold = '50.0%'
    price = sold_50
    code_print = code_items
elif code_items in sales_30:
    sold = '30.0%'
    price = sold_30
    code_print = code_items        
else:
    sold = '0%'
    price = price_items
    code_print = code_items
print(f'the final price of item code-{code_print} after {sold} sale is {price:,.2f} EGY')    



#?lesson 8 - grades project: file 2: part3
extremely_hot = """When the degree is 40 or more
We could say that the weather is extremely hot 🔥🔥♨
we should avoid direct exposure to The Sun ☀☀
We should also remember to drink a lot of water 💦
"""
very_hot = """When the degree is 30 or more
We could say that the weather is very hot 🔥♨
we should be careful about direct exposure to The Sun ☀ We should also remember to drink a lot of water 💦
"""
moderate = """When the degree is between 20 and 30
We could say that we have moderate or good weather 🌞🌞
We should not go with too heavy nor too light clothes 👕 """
cold = """When the degree is between 10 and 20 We could say that we have cold weather ❄❄
We should not go with pretty heavy clothes 👕
"""
very_cold = """When the degree is between 0 and 10 We could say that we have very cold weather ❄❄❄ We should go with pretty heavy clothes 👕
"""
extremely_cold = """When the degree is less than 0
We could say that we have extremely cold weather ❄🧊🧊☃ We should avoid getting out as possible 🧊🧊
We should go with really heavy clothes 👕
Never forget your Heavy Jacket 🧥 wheny you are going out 🧊🥶 """
#star programe
intro_byo = " let's see how we could deal with the weather🌞"
print(f'{intro_byo}\n{"-"*25}')
#input
qs_boy = float(input('enter the degree in celsius: '))
print('-'*25)

#if bot
if qs_boy >= 40:
    massege = extremely_hot
elif qs_boy >= 30:
    massege = very_hot
elif 20 <= qs_boy < 30:     
    massege = moderate
elif 10 <= qs_boy < 20:
    massege = cold
elif 0 <= qs_boy < 10:
    massege = very_cold  
else:
    massege = extremely_cold
print(massege)                 
