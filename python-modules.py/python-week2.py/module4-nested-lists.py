
# Example 1: Accessing elements in a nested list

# Define a nested list representing cells in a table
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

# Print the first sublist (row) in the 'cells' list
print(cells[0])

##############################################

# Define the nested list again
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

# Print the first element of the first sublist (A1)
print(cells[0][0])

# Define the nested list again
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

# Print the third element of the second sublist (B3)
print(cells[1][2])

# Define the nested list again
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

# Print the second element of the second sublist (B2)
print(cells[1][1])

##############################################

# Define the nested list again
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

# Iterate over each sublist in 'cells'
for x in cells:
    # Iterate over each element in the current sublist
    for y in x:
        # Print each element in the sublist
        print('Elements:', y)

##############################################

# Define a nested list representing a table
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]

# Iterate over each row in the 'table'
for row in table:
    # Iterate over each cell in the current row
    for cell in row:
        # Print each cell in the row, followed by a space
        print(cell, '', end='')
    # Print a newline after each row
    print()    

##############################################

# Create a table with 4 rows, each containing numbers from 1 to 5
table = [[i for i in range(1, 6)] for j in range(4)]

# Print the generated table
print(table)
