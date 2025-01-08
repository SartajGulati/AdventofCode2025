# Solution for Day 3 - Part 2
import csv
import re

def mult_string(s):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    sum_temp = 0
    matches = re.findall(pattern, s)
    for match in matches:
        nums = re.findall(r"\d{1,3}", match)
        sum_temp += int(nums[0]) * int(nums[1])
    return sum_temp

instruction = ""

with open("input.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        new_row = ''.join(row)
        instruction += new_row

instruction = "do()" + instruction
sum = 0
split_instruction = re.split(r"don't\(\)", instruction)
for i in split_instruction:
    do_section = re.split(r"do\(\)",i, maxsplit=1)
    if len(do_section) == 2: sum+= mult_string(do_section[1])

print(sum)

#This was a good lesson in simplifying my input