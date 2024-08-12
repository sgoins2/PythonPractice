# Define a function named 'get_average' that calculates and prints the average of a list of numbers
def get_average(input_numbers):
    # Initialize the sum to 0.0
    sum = 0.0
    # Iterate over each number in the input list
    for number in input_numbers:
        # Add the current number to the sum
        sum += number
    # Calculate the average by dividing the sum by the number of elements in the list
    average = sum / len(input_numbers)
    # Print the calculated average
    print(average)

# Call the 'get_average' function with a list of numbers
get_average([3.2, 4.1, 7.4, 8.9, 10.0])    

######################################################

# Define a function named 'print_letter_count' that counts and prints the occurrences of a specific letter in a text
def print_letter_count(text, letter):
    # Initialize the counter to 0
    counter = 0
    # Iterate over each character in the text
    for char in text:
        # Check if the current character is equal to the specified letter
        if char == letter:
            # Increment the counter if the letter is found
            counter += 1
    # Print the number of occurrences of the specified letter
    print('Number of', letter, 'is', counter)

# Call the 'print_letter_count' function with a text and a letter
print_letter_count('Welcome', 'e')

# Call the 'print_letter_count' function with another text and a different letter
print_letter_count('People say nothing is impossible, but I do nothing everyday', 'a')

