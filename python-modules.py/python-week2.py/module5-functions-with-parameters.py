
def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum/ len(input_numbers)
    print(average)

get_average([3.2, 4.1, 7.4, 8.9, 10.0])    

######################################################

def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
print_letter_count('Welcome', 'e')


print_letter_count('People say nothing is impossible, but I do nothing everyday', 'a')
            
     
