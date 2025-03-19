import os
import shutil
from tqdm import tqdm

def find_files(base_path, prefix):
    matching_files = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.startswith(prefix):
                matching_files.append(os.path.join(root, file))
    return matching_files

def copy_zte_survey_files(base_path, destination_folder, prefix):
    # Search for files in the entire computer
    print("Searching for files. This may take some time...")
    files = find_files(base_path, prefix)
    
    if not files:
        print("No matching files found.")
        return
    
    # Ensure destination folder exists
    os.makedirs(destination_folder, exist_ok=True)
    
    # Copy files with progress bar
    for file_path in tqdm(files, desc="Copying files"):
        destination_path = os.path.join(destination_folder, os.path.basename(file_path))
        shutil.copy2(file_path, destination_path)
    
    print("File copying process completed.")

if __name__ == "__main__":
    destination_directory = r"D:\\XXXX\\XXXXX\\PO2\\Files Collection"
    file_prefix = "Survey 19-3-2025"
    base_directory = "D:\\"  # Start searching from the entire C drive
    
    copy_zte_survey_files(base_directory, destination_directory, file_prefix)
