# Example 1: Accessing characters in a string

# Define a favorite artist
fav_artist = 'J Cole'

# Print the fifth character in the string 'fav_artist' (index 4)
print(fav_artist[4])


# Define the favorite artist again
fav_artist = 'J Cole'

# Print the first five characters in the string 'fav_artist'
print(fav_artist[:5])


# Define the favorite artist again
fav_artist = 'J Cole'

# Print the characters in the string 'fav_artist' starting from the fourth character (index 3)
print(fav_artist[3:])


#############################################

# Example 2: Converting a string to uppercase

# Define a text string
text = 'Please capitalize me'

# Convert the text to uppercase
cap_text = text.upper()

# Print the uppercase text
print(cap_text)


#############################################

# Example 3: Checking if user input is numeric

# Prompt the user to input a number
user_name = input('Please input a number')

# Check if the user input is numeric
if user_name.isnumeric():
    # If the input is numeric, print a thank you message
    print('Thank you for following instructions')
else:
    # If the input is not numeric, print an error message with the invalid input
    print('You did not follow instructions,', user_name, 'is not a number, please try again')
