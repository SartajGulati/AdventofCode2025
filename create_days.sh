#!/bin/bash

# Loop from 2 to 25 to create folders
for i in {2..25}; do
    # Create the directory
    mkdir "d$i"
    
    # Create the Python files
    echo "# Solution for Day $i - Part 1" > "d$i/d${i}_1.py"
    echo "# Solution for Day $i - Part 2" > "d$i/d${i}_2.py"
    
    # Create input file
    touch "d$i/input.txt"
    
    echo "Created folder d$i with files d${i}_1.py, d${i}_2.py, and input.txt"
done