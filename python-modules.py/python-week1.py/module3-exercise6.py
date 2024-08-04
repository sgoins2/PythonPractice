# my code
#python_year_released = 1994
#user_input = int(input('When was Python 1.0 released? '))
#while user_input == 1994:
#    print('Correct!')
#elif user_input < 1994:
#    print('It was later than that!')
#else user_input > 1994:
#   print('It was earlier than that!!')
        

##############################################################

# solution
while True:
    answer = int(input('When was Python 1.0 released? '))
    if answer > 1994:
        print('It was earlier than that!')
    elif answer < 1994:
        print('It was later than that!')
    else:
        print('Correct!')
        break