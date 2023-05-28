##!string indexing
##!lesson 13- string indexing - project part 01
name_user = input('Enter your full name: ').title().strip()
edit_name_user = name_user.index(' ')
#print intro
print(f'Hello, {name_user[:edit_name_user]}!\nWelcome at codezilla!')

##! string indexing:
##! lesson 13- string indexing - project part 02:

#user data
#! line1===>line5:
name_user = input('Enter your name: ').strip().title()
cmopany_name = input('Enter your company name: ').strip().title()
birth_year = input('Enter your birth year: ')
email_client = input('Enter your email: ')
print('-'*45)

#! line6===>line8:
edit_name_user = name_user.index(' ')
# print intro
print(f'Hello, {name_user[:edit_name_user]}!\nWelcome at {cmopany_name}!')
print('-'*45)

#! line9===>line10:
id_user = cmopany_name[:3].lower() + '-' +name_user[-2:]+ birth_year
print(f'Your id is: {id_user}')
find_alt = email_client.index('@')
edit_email_user = f'Your email is: {email_client[:find_alt]}@{cmopany_name.lower()}.com'
print(edit_email_user)
