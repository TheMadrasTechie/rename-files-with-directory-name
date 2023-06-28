import os

# Get the current directory
current_directory = os.getcwd()

# Loop through all the items in the directory
for item in os.listdir(current_directory):
    # Construct the full path of the item
    item_path = os.path.join(current_directory, item)
    
    # Check if the item is a directory
    if os.path.isdir(item_path):
        # Loop through all the files in the directory
        for file_name in os.listdir(item_path):
            # Construct the full path of the file
            file_path = os.path.join(item_path, file_name)
            
            # Check if it is a file and not a subdirectory
            if os.path.isfile(file_path):
                # Construct the new file name
                new_file_name = item + "_" + file_name
                
                # Construct the full path of the new file name
                new_file_path = os.path.join(item_path, new_file_name)
                
                # Rename the file
                os.rename(file_path, new_file_path)
                print(f'Renamed {file_name} to {new_file_name}')
