# input user:
first_number = float(input("enter the first number: "))
second_number = float(input("enter the second number: "))
operator = input('enter the operater: ')

# if data:
if  operator in ('+', '-', '*', '/', '**'):
    if operator == '+':
        operation_name = 'Addition'
        result = first_number + second_number
    elif operator == '-':
        operation_name = 'Subtraction'
        result = first_number - second_number
    elif operator == '*':
        operation_name = 'Multiplication'
        result = first_number * second_number
    elif operator == '/':
        operation_name = 'Division'
        result = first_number / second_number
    else:
        operation_name = 'Power'
        result = first_number ** second_number
    print(f'{operation_name} result is {result}')    
else:
    print('sorry, please enter valid inputs')

# input user:
first_number = float(input("enter the first number: "))
second_number = float(input("enter the second number: "))
operator = input('enter the operater: ')

# if data:
if  operator in ('+', '-', '*', '/', '**'):
    if operator == '+':
        operation_name = 'Addition'
        result = first_number + second_number
    elif operator == '-':
        operation_name = 'Subtraction'
        result = first_number - second_number
    elif operator == '*':
        operation_name = 'Multiplication'
        result = first_number * second_number
    elif operator == '/':
        operation_name = 'Division'
        result = first_number / second_number
    else:
        operation_name = 'Power'
        result = first_number ** second_number
    print(f'{operation_name} result is {result}')
else:
    print('sorry, please enter valid inputs')

#? lesson 8 - grades project: file 3: part3
#? part 3 
#* A	90–100%	
# *B	80–89%	
# *C	70–79%	
# *D	60–69%	
# *F	0–59%	
#!intro:
intro = 'please enter score between 0 and 100'
print(f'{intro}\n{"-"*30}')
#!input:
score_arabic = float(input('enter arabic score: '))
score_english = float(input('enter english score: '))
score_math = float(input('enter math score: '))
score_physics = float(input('enter physics score: '))
score_sport = float(input('enter sport score: '))
score_islamic = float(input('enter islamic score: '))

# !cal score:
result_score = (score_arabic+score_english+score_islamic+score_math+score_physics+score_sport)/6
#! IF DATA:
check = 0<=score_arabic<=100 and 0<=score_physics<=100 and 0<=score_islamic<=100 and 0<=score_sport<=100 and 0<=score_math<=100 and 0<=score_english<=100
if check:
    if 90<=result_score<=100:
        grade = 'A'
    elif 80<=result_score<=89: 
        grade = 'B'
    elif 70<=result_score<=79:
        grade = 'C'
    elif 60<=result_score<=69:          
        grade = 'D'
    else:
        grade = 'F'
    print(f'{"-"*30}\nyour score is {result_score: .2f}%\nyour grade is {grade}')     
else:
    # Print error message for invalid scores
    if not 0 <= score_arabic <= 100:
        print("Error: Invalid score entered for Arabic. Please enter a score between 0 and 100.")
    if not 0 <= score_english <= 100:
        print("Error: Invalid score entered for English. Please enter a score between 0 and 100.")
    if not 0 <= score_math <= 100:
        print("Error: Invalid score entered for Math. Please enter a score between 0 and 100.")
    if not 0 <= score_physics <= 100:
        print("Error: Invalid score entered for Physics. Please enter a score between 0 and 100.")
    if not 0 <= score_sport <= 100:
        print("Error: Invalid score entered for Sport. Please enter a score between 0 and 100.")
    if not 0 <= score_islamic <= 100:
        print("Error: Invalid score entered for Islamic. Please enter a score between 0 and 100.")
   













