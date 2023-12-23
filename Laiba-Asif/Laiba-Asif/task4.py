import os
import shutil
import zipfile

def create_folder_structure(folder_name):
    # Check if the folder exists, delete it if it does
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
    
    # Create the top-level folder
    os.mkdir(folder_name)
    
    # Create subfolders
    os.mkdir(os.path.join(folder_name, "backup"))
    os.mkdir(os.path.join(folder_name, "working"))
    os.mkdir(os.path.join(folder_name, "working", "pics"))
    os.mkdir(os.path.join(folder_name, "working", "docs"))
    os.mkdir(os.path.join(folder_name, "working", "docs", "school"))
    os.mkdir(os.path.join(folder_name, "working", "docs", "party"))
    os.mkdir(os.path.join(folder_name, "working", "movie"))
    
    # Create files
    file_names = ["SCREENTIME.txt", "DANGEROUS.txt", "KEEPSAFE.txt", "CONCENTRATE.txt", "SUCCEED.txt"]
    for file_name in file_names:
        with open(os.path.join(folder_name, "working", "docs", file_name), "w") as f:
            f.write("This is some content for {}".format(file_name))

def rename_docs_files(folder_name):
    docs_dir = os.path.join(folder_name, "working", "docs")
    for file_name in os.listdir(docs_dir):
        if file_name.endswith(".txt"):
            # Rename file to lowercase with uppercase extension
            new_file_name = file_name.lower().replace(".txt", ".TXT")
            os.rename(os.path.join(docs_dir, file_name), os.path.join(docs_dir, new_file_name))

def backup_docs(folder_name):
    docs_dir = os.path.join(folder_name, "working", "docs")
    backup_dir = os.path.join(folder_name, "backup")
    
    # Create five backup archives
    for i in range(5):
        zip_file_name = os.path.join(backup_dir, "docs_backup_{}.zip".format(i))
        with zipfile.ZipFile(zip_file_name, "w") as zip_file:
            for root, dirs, files in os.walk(docs_dir):
                for file in files:
                    zip_file.write(os.path.join(root, file), arcname=file)
    
    # Print the contents of the backup folder
    print("Backup folder contents:")
    for file_name in os.listdir(backup_dir):
        print(os.path.join(backup_dir, file_name))
    
    # Print the contents of the first backup archive for verification
    print("Contents of first backup archive:")
    with zipfile.ZipFile(os.path.join(backup_dir, "docs_backup_0.zip"), "r") as zip_file:
        for file_name in zip_file.namelist():
            print(file_name)
folder_name = input("Enter the name of the top-level folder: ")
create_folder_structure(folder_name)
rename_docs_files(folder_name)
backup_docs(folder_name)
