def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def divide(num1,num2):
    return num1/num2
def multiply(num1,num2):
    return num1*num2

while True:

    print ('PLease select an operation \nA for addition'
        '\nS for subtraction\nM for multiplication\nD for division\nQ to quit')


    select = input('Select operations : ').upper()
    num_1 = int(input('enter the first number'))
    num_2 = int(input('select the second number'))


    if select == 'A':
        print (num_1, '+', num_2,  '=', add(num_1, num_2))

    elif select == 'S':
        print (num_1, '-', num_2, '=',subtract(num_1,num_2))

    elif select == 'M':
        print(num_1, '*', num_2, '=', multiply(num_1,num_2))

    elif select == 'D':
        print(num_1, '/', num_2, '=', divide(num_1,num_2))

    elif select == 'Q':
        print('quitting')
        break









