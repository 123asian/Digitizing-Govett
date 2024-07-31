import os

folder = "extraction/output/pdf_images"
find = "1ffadcb1-1788-4ab1-86d3-c1f814c122fa"
replace = "Govett-The-Apocalypse"

# List all files in the directory
for filename in os.listdir(folder):
    # Filter the files you want to rename (e.g., you can use conditional statements)
    if find in filename:
        # Define the new file name (you can customize this based on your requirements)
        new_name = filename.replace(find, replace)

        # Create the full paths to the old and new file names
        old_file_path = os.path.join(folder, filename)
        new_file_path = os.path.join(folder, new_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {filename} to {new_name}')