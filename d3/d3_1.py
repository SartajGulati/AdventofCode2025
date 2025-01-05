# Solution for Day 3 - Part 1
import csv



with open("input.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        print(row)