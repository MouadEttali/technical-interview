#!/bin/bash

WATCH_DIR="/mnt/c/Users/metta/Downloads"  # Path to the Windows Downloads folder in WSL
SCRIPT1="./scripts/run_main_script.sh"
# Function to count the files in the directory

count_files() {
  find "$WATCH_DIR" -type f | wc -l
}

# Track the number of files at the first launch
INITIAL_FILE_COUNT=$(count_files)
echo "Initial file count at launch: $INITIAL_FILE_COUNT"

# Periodically check every 3 minutes
while true; do
  # Get the current file count
  CURRENT_FILE_COUNT=$(count_files)
  
  # Compare the current file count with the initial one
  if [ "$CURRENT_FILE_COUNT" -gt "$INITIAL_FILE_COUNT" ]; then
    # New files have been added
    NEW_FILES=$(($CURRENT_FILE_COUNT - $INITIAL_FILE_COUNT))
    echo "$NEW_FILES new files detected. Current count: $CURRENT_FILE_COUNT"

    # Trigger your scripts for new files
    sh "$SCRIPT1"

    break
    # Update the initial file count to the current count
    INITIAL_FILE_COUNT=$CURRENT_FILE_COUNT
  fi
  
  sleep 3
done
