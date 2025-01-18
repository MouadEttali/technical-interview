#!/bin/bash

echo "copying data from download to workspace"

sh  ./scripts/move_latest.sh

echo "Data copied successfully"

# Define the command to execute the Python script
PYTHON_COMMAND="/home/mouad/personal/technical-interview/.venv/bin/python /home/mouad/personal/technical-interview/src/main.py"

# Execute the Python script
$PYTHON_COMMAND

# Check if the Python script execution was successful
if [ $? -eq 0 ]; then
  echo "Python script executed successfully."
else
  echo "Error: Failed to execute the Python script."
  exit 1
fi
