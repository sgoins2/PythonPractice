import os

# Retrieve current working directory
current_directory = os.getcwd()

def data_extractor(directory):
    file_data = []
    
    # Iterate over each item in the directory
    for file in os.listdir(directory):
        # Create the full path
        path = os.path.join(directory, file)
        # Verify file present
        if os.path.isfile(path):
            # Get file size
            size = os.path.getsize(path)
            # Append file information to the list
            file_data.append({'file_name': file, 'size': size})
    
    return file_data

# Get the list of dictionaries with file information
file_data = data_extractor(current_directory)

# Print list of dictionaries
for data in file_data:
    print(data)
