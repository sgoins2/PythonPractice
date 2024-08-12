# Example 1: Adding entries to a dictionary

# Create an empty dictionary to store grades
grades = {}

# Add a grade for 'john'
grades['john'] = 'A-'

# Add a grade for 'lisa'
grades['lisa'] = 'B'

# Print the dictionary with the added grades
print(grades)


#############################

# Example 2: Updating an entry in a dictionary

# Update the grade for 'lisa'
grades['lisa'] = 'A'

# Print the dictionary after updating 'lisa's grade
print(grades)


#############################

# Example 3: Updating an entry using the update method

# Update the grade for 'john' using the update method
grades.update({'john': 'A'})

# Print the dictionary after updating 'john's grade
print(grades)


#############################

# Example 4: Getting the number of entries in a dictionary

# Print the number of entries in the dictionary
print(len(grades))


#############################

# Example 5: Checking if a key exists in a dictionary

# Check if 'john' is in the dictionary and print his grade
if 'john' in grades:
    print('John got a(n):', grades['john'])


#############################

# Example 6: Deleting an entry from a dictionary

# Delete the entry for 'john'
del grades['john']

# Print the dictionary after deleting 'john's entry
print(grades)


#############################

# Example 7: Iterating over dictionary keys

# Recreate the dictionary with grades for 'john' and 'lisa'
grades = {}

grades['john'] = 'A-'
grades['lisa'] = 'B'

# Iterate over the keys (student names) in the dictionary and print them
for students in grades:
    print(students)


#############################

# Example 8: Iterating over dictionary keys using the keys() method

# Iterate over the keys (student names) using the keys() method and print them
for students in grades.keys():
    print(students)


#############################

# Example 9: Iterating over dictionary values

# Iterate over the values (grades) in the dictionary and print them
for students in grades.values():
    print(students)


#############################

# Example 10: Iterating over dictionary items

# Iterate over the items (key-value pairs) in the dictionary and print them
for person, grade in grades.items():
    print(person, 'got a(n)', grade)





