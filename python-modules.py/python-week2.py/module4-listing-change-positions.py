# Example 1: Swapping two numbers entered by the user

# Get the first number from the user
first = input('Enter the first number: ')

# Get the second number from the user
second = input('Enter the second number: ')

# Display the numbers before swapping
print('Before swapping', first, second)

# Swap the values of first and second
first, second = second, first

# Display the numbers after swapping
print('After Swapping', first, second)


########################################################

# Example 2: Swapping the positions of specific elements in a list

# List of top cities
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 'Atlanta', 'Las Vegas']

# Swap the first and fifth elements in the list
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]

# Print the modified list
print(top_cities)

########################################################

# Example 3: Sorting a list of city names in alphabetical order

# List of top cities
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 'Atlanta', 'Las Vegas']

# Sort the list in alphabetical order
top_cities.sort()

# Print the sorted list
print(top_cities)

########################################################

# Example 4: Sorting a list of random numbers in ascending order

# List of random numbers
random_number = [0, 10, 3, 7, 12, 9]

# Sort the list in ascending order
random_number.sort()

# Print the sorted list
print(random_number)

########################################################

# Example 5: Sorting a list of random numbers in descending order

# List of random numbers
random_number = [0, 10, 3, 7, 12, 9]

# Sort the list in descending order
random_number.sort(reverse=True)

# Print the sorted list
print(random_number)

########################################################
# Example 5: sorting a random list and keeping the original list
# List of top cities
top_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 'Atlanta', 'Las Vegas']

# Print the sorted list of cities without modifying the original list
print(sorted(top_cities))

# Print the original list to show it remains unchanged
print(top_cities)
