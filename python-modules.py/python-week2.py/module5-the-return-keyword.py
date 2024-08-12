# Define a function named 'get_average' that calculates the average of a list of numbers
def get_average(input_numbers):
    # Initialize the sum to 0.0
    sum = 0.0
    # Iterate over each number in the input list
    for number in input_numbers:
        # Add the current number to the sum
        sum += number
    # Calculate the average by dividing the sum by the number of elements in the list
    average = sum / len(input_numbers)
    # Return the calculated average
    return average

# Call the 'get_average' function with a list of numbers and print the result
print('The average is: ', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))


# Assign the result of 'get_average' function to the variable 'average'
average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
# Check if the average is greater than 5.0
if average > 5.0:
    # Print a message if the condition is met
    print('The average is too high!')


# Define a function named 'is_first_last_equal' that checks if the first and last elements of a list are equal
def is_first_last_equal(number_list):
    # Check if the list is empty
    if len(number_list) == 0:
        # Return None if the list is empty
        return
    # Check if the first and last elements of the list are equal
    if number_list[0] == number_list[-1]:
        # Return True if they are equal
        return True
    else:
        # Return False if they are not equal
        return False

# Call the 'is_first_last_equal' function with a list and print the result
print(is_first_last_equal([10, 20, 30, 40, 10]))

# Call the 'is_first_last_equal' function with another list and print the result
print(is_first_last_equal([10, 20, 30, 40, 17]))