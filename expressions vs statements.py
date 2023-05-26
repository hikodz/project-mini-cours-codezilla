# ? lesson 5 - expressions vs statements

hours_per_month = float(input("enter the number of hours per month: "))
rate_hours = float(input("enter your hourly rate: "))
print('-'*30)

result_price = hours_per_month * rate_hours

new_price_hour = ((rate_hours * 2) * (hours_per_month - 100)) + (100 * rate_hours)

if hours_per_month <= 100:
    print(f'you have worked {hours_per_month} hours this month, your salery is {result_price: ,}$')
else:
    print(f'you have worked {hours_per_month} hours this month, your salery is {new_price_hour: ,}$')    