# Solution for Day 5 - Part 1
import csv


rules = {}
updates = []

def prosses_update(update):
    #iterate through them backwards, if anything in seen is in key, it's a fail
    seen = []
    for u in update:
        if u in rules:
            if len(list(set(rules[u]) & set(seen))) != 0:
                return False
        seen.append(u)
    return True

with open("input.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        if row: line = row[0]
        else: continue
        if '|' in line:
            nums = line.split('|')
            rules.setdefault(nums[0], []).append(nums[1])
        else:
            updates.append(line)


middle = []
for up in updates:
    lst = up.split(',')
    if prosses_update(lst):
        middle.append(int(lst[len(lst)//2]))


print(sum(middle))