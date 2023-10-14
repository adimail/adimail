import os

# Get the current directory
directory_path = os.getcwd()

# List all the .jpg files in the directory
jpg_files = [f for f in os.listdir(directory_path) if f.endswith('.jpg')]

# Sort the files to ensure consistent numbering
jpg_files.sort()

# Initialize a counter for renaming
counter = 1

# Rename the files
for old_name in jpg_files:
    extension = os.path.splitext(old_name)[1]  # Get the file extension (e.g., '.jpg')
    new_name = f'img{counter}{extension}'  # Create the new name
    old_path = os.path.join(directory_path, old_name)  # Full path of the old file
    new_path = os.path.join(directory_path, new_name)  # Full path of the new file

    # Rename the file
    os.rename(old_path, new_path)

    # Increment the counter
    counter += 1

print("All .jpg files have been renamed.")

