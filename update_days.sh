#!/bin/bash

# The Python code to insert
PYTHON_CODE='import csv

with open("input.txt") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        print(row)'

# Loop through directories d7 to d25
for i in {6..25}; do
    dir="d$i"
    if [ -d "$dir" ]; then
        # Loop through the Python files in each directory
        for pyfile in "$dir"/d${i}_[12].py; do
            if [ -f "$pyfile" ]; then
                # Check if file is empty before writing
                echo "$PYTHON_CODE" > "$pyfile"
                echo "Added code to $pyfile"
            fi
        done
    fi
done
