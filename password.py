print('input password if it matches mine you win')
user_input = input('write your password: ')
my_passwd = 'abrakadabra'
if user_input == my_passwd:
    print("you win!")
else:
    print("try again")