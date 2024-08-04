# Example 1: Modifying a string variable

# Assign the original name to the variable 'name_original'
name_orginal = 'Jon Smith'

# Assign the value of 'name_orginal' to 'new_name'
new_name = name_orginal

# Change the value of 'name_orginal' to a new name
name_orginal = 'Peter Pan'

# Print the modified 'name_orginal' and the unchanged 'new_name'
print(name_orginal, new_name)

#######################################

# Example 2: Modifying a list through a reference

# Assign a list to 'list_original'
list_original = [1, 2, 3]

# Assign the reference of 'list_original' to 'list_new'
list_new = list_original

# Change the first element of 'list_original'
list_original[0] = 5

# Print both lists to show that both have changed
print('Original: ', list_original, '\nNew: ', list_new)

#######################################

# Example 3: Modifying a list through a shallow copy

# Assign a list to 'list_original'
list_original = [1, 2, 3]

# Create a shallow copy of 'list_original' and assign it to 'list_new'
list_new = list_original[:]

# Change the first element of 'list_original'
list_original[0] = 5

# Print both lists to show that only 'list_original' has changed
print('Original: ', list_original, '\nNew: ', list_new)

#######################################

# Example 4: Creating a partial copy of a list

# Assign a list to 'list_original'
list_original = [1, 2, 3]

# Create a partial shallow copy of the first two elements of 'list_original' and assign it to 'list_new'
list_new = list_original[:2]

# Change the first element of 'list_original'
list_original[0] = 5

# Print both lists to show the difference
print('Original: ', list_original, '\nNew: ', list_new)


