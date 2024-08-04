# Example 1: Creating a list of numbers from 1 to 100 using a for loop

# Initialize a list with some numbers
numbers = [1, 2, 3, 4]

# Clear the list by assigning an empty list to 'numbers'
numbers = []

# Use a for loop to iterate over a range of numbers from 1 to 100
for i in range(1, 101):
    # Append each number to the list 'numbers'
    numbers.append(i)

# Print the list of numbers from 1 to 100
print(numbers)

#############################################

# Example 2: Creating a list of numbers from 1 to 100 using list comprehension

# Use list comprehension to generate a list of numbers from 1 to 100
numbers = [i for i in range(1, 101)]

# Print the list of numbers from 1 to 100
print(numbers)

#############################################

# Example 3: Creating a list of numbers from 1 to 100, excluding multiples of 3, using list comprehension

# Use list comprehension to generate a list of numbers from 1 to 100, excluding multiples of 3
numbers = [i for i in range(1, 101) if i % 3 != 0]

# Print the list of numbers from 1 to 100, excluding multiples of 3
print(numbers)
