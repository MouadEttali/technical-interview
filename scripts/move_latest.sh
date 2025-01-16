#!/bin/bash

# Set source directory (Windows Downloads folder)
SOURCE_DIR="/mnt/c/Users/metta/Downloads"

# Set destination directory (Linux directory)
DEST_DIR="/home/mouad/personal/technical-interview/problem_statement_files"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Find the latest file in the source directory
LATEST_FILE=$(ls -t "$SOURCE_DIR" 2>/dev/null | head -n 1)

# Check if a file was found
if [ -z "$LATEST_FILE" ]; then
  echo "No files found in $SOURCE_DIR."
  exit 1
fi

# Full path to the latest file
LATEST_FILE_PATH="$SOURCE_DIR/$LATEST_FILE"

# Function to extract compressed files
extract_file() {
  case "$1" in
    *.tar.gz | *.tgz) tar -xzf "$1" -C "$DEST_DIR" ;;
    *.tar.bz2 | *.tbz2) tar -xjf "$1" -C "$DEST_DIR" ;;
    *.tar.xz) tar -xJf "$1" -C "$DEST_DIR" ;;
    *.zip) unzip "$1" -d "$DEST_DIR" ;;
    *.rar) unrar x "$1" "$DEST_DIR" ;;
    *.7z) 7z x "$1" -o"$DEST_DIR" ;;
    *) return 1 ;;  # Not a supported archive
  esac
  return 0
}

# Check if the file is a compressed file
if extract_file "$LATEST_FILE_PATH"; then
  echo "Extracted the archive '$LATEST_FILE' to '$DEST_DIR'."
  # Optionally, delete the archive after extraction
  # rm "$LATEST_FILE_PATH"
else
  # Move the file if it's not an archive
  mv "$LATEST_FILE_PATH" "$DEST_DIR"
  if [ $? -eq 0 ]; then
    echo "Moved the file '$LATEST_FILE' to '$DEST_DIR'."
  else
    echo "Failed to move the file. Please check permissions."
    exit 1
  fi
fi
