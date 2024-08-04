# example 1: using multiple operators

user_age = int(input('How old are you? '))
user_country = input('What country are you from? ')

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchange program')
else: 
    print('Sorry, you do not qualify')


#example 2: using the 'or' operator
user_country == input('What is your country?')

if user_country == 'Sweden' or user_country == 'Demark' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange program')
else:
    print('Sorry, you do not qualify')


#example 3: using the 'if not' operator
user_country = input('Where do you coome from? ')
if not user_country == 'Germany':
    print('You are not from Germany')
else:
    print('You are from Germany')
