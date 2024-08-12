# Print a message with custom end and separator
# 'Hello,' and 'How are you?' will be joined with '-' and will end with '.'
print('Hello,', 'How are you?', end='.', sep='-')


# Define a function named 'print_letter_counter' with default arguments
def print_letter_counter(text='This is the default string to search', letter='a'):
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

# Call the 'print_letter_counter' function with a custom text
print_letter_counter('How many letters a are here?')

# Call the 'print_letter_counter' function with default arguments
print_letter_counter()
