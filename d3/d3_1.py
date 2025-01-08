# Solution for Day 3 - Part 1
import csv
import re


pattern = r"mul\(\d{1,3},\d{1,3}\)"
sum = 0

with open("input.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        for col in row:
            matches = re.findall(pattern, col)
            for match in matches:
                p = r"\d{1,3}"
                nums = re.findall(p, match)
                sum += int(nums[0]) * int(nums[1])
print(sum)

