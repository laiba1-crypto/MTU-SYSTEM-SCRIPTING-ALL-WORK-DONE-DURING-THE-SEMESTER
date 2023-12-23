#R00201303
#!/bin/bash

# Check if the file size argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <sizeOfFile_in_bytes>"
    exit 1
fi

# Function to copy a file
copyMyFile() {
    local filename="$1"
    read -p "Enter a new name for copying \"$filename\": " new_name
    cp "$filename" "$new_name"
}

# Function to delete a file
deleteMyFile() {
    local filename="$1"
    rm -i "$filename"
}

# Get the specified file size
sizeOfFile="$1"

# List all files in the "input" folder
inputFolder="/content/drive/MyDrive/Bash&Python/input"
inputFiles=("$inputFolder"/*)

# Process each file
for file in "${inputFiles[@]}"; do
    # Check if the file size exceeds the specified size
    size=$(wc -c < "$file")
    if [ "$size" -gt "$sizeOfFile" ]; then
        echo "File: $file"
        read -p "Do you want to copy or delete this file? (c/d): " choice
        case "$choice" in
            c|C)
                copyMyFile "$file"
                ;;
            d|D)
                deleteMyFile "$file"
                ;;
            *)
                echo "Invalid choice. Skipping the file."
                ;;
        esac
    fi
done

# List the content of the working directory and the "input" folder
echo "Content of the working directory:"
ls -l

echo "Content of the input folder:"
ls -l "$inputFolder"
