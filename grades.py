#? lesson 8 - grades
#? lesson 8 - grades project: file 1: part1
winners = ['mohamed', 'ahmed', 'mahmoud' ,'islam', 'hassan', 'israa', 'mariam']

input_name = input('enter the winning name: ')

if input_name.strip().lower() in winners:
    print(f'congratulation {input_name.strip().title()} is a winner!!!')
else:
    print(f'sorry {input_name.strip()} is not a winner!')    

  
#? lesson 8 - grades project: file 1: part2
# data:
first_user = 'islam_hesham@codezilla.com'
first_pass = 'islam_codezilla'
second_user = 'mohamed_gouda@codezilla.com'
second_pass = 'gouda_codezilla'
# plan data if:
data_enter = input('enter username: ').strip()
data_pass = input('enter password: ').strip()

if data_enter == first_user and data_pass == first_pass:
    print('access is allowed')
elif data_enter == second_user and data_pass == second_pass:
    print('access is allowed')
else:
    print('sorry, access is not allowed')        


#? lesson 8 - grades project: file 1: part3
# data:
country_fri_sat = ['egypt', 'saudia arabia', 'ksa', 'kuwait', 'algeria','iraq']

country_sat_sun = ['australia', 'usa', 'united states', 'united kingdom', 'uk']
# input user :
enter_country = input('enter country name: ').strip().lower()
# plan data if :

if enter_country in country_fri_sat:
    print(f'friday and saturday are the weekends in {enter_country.upper()}')
elif enter_country in country_sat_sun:
    print(f'saturday and sunday are the weekends in {enter_country.upper()}')
else:
    print("sorry, a dont't know")
