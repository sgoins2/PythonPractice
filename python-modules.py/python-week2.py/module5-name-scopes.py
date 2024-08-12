# Example 1: Local vs. Global Variables

# Define a function named 'show_truth'
def show_truth():
    # Inside the function, a new local variable 'mysterious_var' is created and assigned a value
    mysterious_var = 'New Surprise!'
    # Print the local 'mysterious_var' within the function
    print(mysterious_var)

# Outside the function, create a global variable 'mysterious_var' and assign a value
mysterious_var = 'Surprise!'
# Print the global 'mysterious_var'
print(mysterious_var)
# Call the 'show_truth' function, which prints the local 'mysterious_var'
show_truth()
# Print the global 'mysterious_var' again, which remains unchanged
print(mysterious_var)

# Hint: Local variables inside functions do not affect global variables outside the function.

####################################################

# Example 2: Using the global keyword

# Define a function named 'show_truth'
def show_truth():
    # Declare 'mysterious_var' as a global variable to modify the global variable inside the function
    global mysterious_var
    # Assign a new value to the global variable 'mysterious_var'
    mysterious_var = 'New Surprise!'
    # Print the modified global 'mysterious_var'
    print(mysterious_var)

# Outside the function, create a global variable 'mysterious_var' and assign a value
mysterious_var = 'Surprise!'
# Print the global 'mysterious_var'
print(mysterious_var)
# Call the 'show_truth' function, which modifies and prints the global 'mysterious_var'
show_truth()
# Print the global 'mysterious_var' again, which is now modified by the function
print(mysterious_var)

# Hint: Using the 'global' keyword allows a function to modify a global variable.

####################################################

# Example 3: Modifying a mutable global variable

# Define a function named 'show_truth'
def show_truth():
    # Append a new value to the global list 'mysterious_var'
    mysterious_var.append('New Surprise!')
    # Print the modified global list 'mysterious_var'
    print(mysterious_var)

# Outside the function, create a global list 'mysterious_var' and assign initial values
mysterious_var = ['Surprise!']
# Print the global list 'mysterious_var'
print(mysterious_var)
# Call the 'show_truth' function, which modifies and prints the global list 'mysterious_var'
show_truth()
# Print the global list 'mysterious_var' again, which is now modified by the function
print(mysterious_var)

# Hint: Modifying a mutable global variable (like a list) inside a function affects the variable outside the function.