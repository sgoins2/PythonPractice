# while loop example
# often used when the number of executions is unknown

counter = 1
while counter < 11:
    print(counter)
    counter += 1
print("Finished!")    



# example 2

secret_number = 14
user_input = int(input('Try to guess the secret number from 0 to 20: '))
while user_input != secret_number:
    print('Wrong, try again')
    user_input = int(input('Try to guess the secret number from 0 to 20: '))
print('Perfect! that\'s the correct answer')
