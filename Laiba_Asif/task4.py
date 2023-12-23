#R00201303
import os
import shutil

# Create a function to read and display selected lines from a file
def readAndDisplay(myfilePath):
    try:
        # Check if the file exists
        if not os.path.exists(myfilePath):
            print(f"File '{myfilePath}' does not exist.")
            return
        
        # Define keywords to search for at the beginning of lines
        keywords = ["Imagine", "we", "How"]
        
        # Open the file and read its content
        with open(myfilePath, 'r') as file:
            lines = file.readlines()
        
        print(f"Selected lines from '{myfilePath}':")
        for line in lines:
            # Check if the line starts with any of the keywords
            if any(line.strip().startswith(keyword) for keyword in keywords):
                print(line.strip())
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Create a folder named "my_folder" (delete if it already exists)
    folder_name = "my_folder"
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
    os.makedirs(folder_name)
    
    # Create four empty files
    files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
    for file in files:
        open(file, 'a').close()
    
    # Write content to one of the files
    with open("file1.txt", 'w') as file:
        file.write("I was told how brave he fought the COVID-19 sickness\n")
        file.write("Imagine how life would be without you by his side\n")
        file.write("we are destined for greatness if we could just understand each other\n")
        file.write("How do you find this philosophy?\n")
        file.write("imagine that things could get worse\n")
        file.write("We will definitely be saved at the end.\n")

    for file in files[1:]:
        shutil.move(file, os.path.join(folder_name, file))

    print(f"Current working directory: {os.getcwd()}")
    
    readAndDisplay("file1.txt")

if _name_ == "_main_":
    main()
