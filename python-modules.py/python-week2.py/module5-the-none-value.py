# Example 1: Understanding the return value of print()

# Call the print function, which prints 'Hello world!' and returns None
print_return = print('Hello world!')
# Print the return value of the previous print function call, which is None
print(print_return)

# Hint: The print() function always returns None.

#############################################################

# Example 2: Checking the truthiness of None

# Assign None to variable x
x = None

# Check if x is truthy; since None is falsy, this block will not execute
if x:
    print('None is true')
# Check if x is explicitly False; since x is None, this block will not execute
elif x is False:
    print('None is false')
# If none of the above conditions are met, this block will execute
else:
    print('None is neither true nor false, none is just none')    

# Hint: None is a special constant in Python that is neither true nor false, but is considered falsy.

#############################################################

# Example 3: Checking if a variable is None using 'is' and '=='

# Assign None to variable x
x = None

# Check if x is None using 'is' keyword
if x is None: 
    print('yes')

# Check if x is equal to None using '=='
if x == None:
    print('it does')

# Hint: 'is' checks for identity (if both sides are the same object), while '==' checks for equality.

#############################################################

# Example 4: Understanding the return value of a function that does not explicitly return

# Define a function named 'greet'
def greet():
    # Print a greeting message
    print('hello!')

# Call the 'greet' function and assign its return value to x
x = greet()
# Print the return value of the 'greet' function, which is None
print(x)

# Hint: Functions that do not explicitly return a value will return None by default.

#############################################################
