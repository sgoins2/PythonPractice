
input_numbers = [8.2, 3.5, 7.12, 9.16, 10.0, 12.20]

def get_average(input_numbers):
    sum = 0.0
    for numbers in input_numbers:
        sum += numbers
        average = sum / len(input_numbers)
        print(average)


##########################################################################

def get_average(input_numbers):
    sum = 0.0
    for numbers in input_numbers:
        sum += numbers
    average = sum / len(input_numbers)
    print(average)

get_average([8.2, 3.5, 7.12, 9.16, 10.0, 12.20])



##########################################################################


def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter )  

print_letter_count('Welcome', 'e')        

print_letter_count('People say nothing is impossible, but I do nothing everyday', 'e')

print_letter_count('e', 'Welcome')

print_letter_count(text='Welcome', letter='e')

##########################################################################

