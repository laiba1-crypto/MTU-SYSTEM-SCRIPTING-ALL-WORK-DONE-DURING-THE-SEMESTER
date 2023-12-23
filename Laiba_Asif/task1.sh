#R00201303
#!/bin/bash

# Check if the threshold argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <threshold>"
    exit 1
fi

# Function to count regular files in a directory
countingRegFiles() {
    local dir="$1"
    local threshold="$2"
    local fileCount=$(find "$dir" -type f | wc -l)
    
    # Compare the file count against the threshold
    if [ "$fileCount" -gt "$threshold" ]; then
        echo "Directory: $dir"
        echo "File Count: $fileCount"
        echo "Threshold: $threshold"
        echo "Timestamp: $(date)"
    fi
}

# Main script
threshold="$1"
targetDirectory="/content/drive/MyDrive/Bash&Python/target"

# Check if the target directory exists
if [ ! -d "$targetDirectory" ]; then
    echo "Error: The target directory does not exist."
    exit 1
fi

# Loop through subdirectories in the target directory
for subdir in "$targetDirectory"/*; do
    if [ -d "$subdir" ]; then
        # Call the function to count regular files in the subdirectory
        countingRegFiles "$subdir" "$threshold"
    fi
done

exit 0
