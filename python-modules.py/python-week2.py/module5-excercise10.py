
def unique(input_list=[]):
  to_return = []
  for el in input_list:
    if el not in to_return:
      to_return.append(el)
  return to_return


############################################################

#solution
#Define a function named 'unique' that returns a list of unique elements from the input list
def unique(input_list=[]):
    # Initialize an empty list to store unique elements
    unique_list = []
    # Iterate over each element in the input list
    for i in input_list:
        # Check if the current element is not already in the 'unique_list' list
        if i not in unique_list:
            # Append the unique element to the 'unique_list' list
            unique_list.append(i)
    # Return the list of unique elements
    return unique_list

# Example usage:
# unique_list = unique([1, 2, 2, 3, 4, 4, 5])
# print(unique_list)  # Output: [1, 2, 3, 4, 5]
