# Example 1: Checking if a name is in the VIP list

# List of VIP names
VIP_list = ['Sean, Mac, Tasha, Ricky, Jasmine, Kayla, Steph, Lisa']

# Get the user's name
name = input('What is your name? ')

# Check if the name is in the VIP list
if name in VIP_list:
    # If the name is in the VIP list, print a welcome message
    print('Welcome!')
else:
    # If the name is not in the VIP list, print a message indicating they are not invited
    print('You are not invited!')    


#######################################################################

# Example 2: Checking if a name is not in the VIP list

# List of VIP names
VIP_list = ['Sean, Mac, Tasha, Ricky, Jasmine, Kayla, Steph, Lisa']

# Get the user's name
name = input('What is your name? ')

# Check if the name is not in the VIP list
if name not in VIP_list:
    # If the name is not in the VIP list, print a welcome message
    print('Welcome!')
else:
    # If the name is in the VIP list, print a message indicating they are not invited
    print('You are not invited!')
     