#  intro to Lists lesson 9 :
# employees and their ids
juniors = ['1111', '1113', '1115', '1117',
'1119', '1121']
mid_level = ['1311', '1313', '1315', '1317',
'1319', '1321', '1323', '1325']
seniors = ['1519', '1521', '1523', '1525']

# input user:
id_user = input('enter employee id: '.title())
hours_rate = float(input('enter hourly rate: '.title()))
worked_month = float(input('enter hours worker this month: '.title()))
print("-"*32)
juniors_bouns = (hours_rate*worked_month)*3
mid_level_bouns = (hours_rate*worked_month)*6
seniors_bouns = (hours_rate*worked_month)*9
# if data user 
if id_user in juniors:
    bouns = juniors_bouns
elif id_user in mid_level:
    bouns = mid_level_bouns
elif id_user in seniors:
    bouns = seniors_bouns
else:
    bouns = None
    print('not an employee')
if bouns != None:
    print(f'employee id: {id_user} gets a bonus of {bouns:,.2f}EGP')    










