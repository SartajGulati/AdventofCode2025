# Solution for Day 5 - Part 2
import csv


rules = {}
updates = []

def prosses_update(update):
    seen = []
    for u in update:
        if u in rules:
            if len(list(set(rules[u]) & set(seen))) != 0:
                return False
        seen.append(u)
    return True


def order_update(update):
    new_update = [update[0]]
    for u in range(1,len(update)):
        if update[u] not in rules:
            new_update.append(update[u])
        else:
            if (len(list(set(rules[update[u]]) & set(new_update))) == 0):
                new_update.append(update[u])
            else:
                #place as left as needed
                min_index = len(update)
                for r in rules[update[u]]:
                    if r in new_update:
                        min_index = min(min_index, new_update.index(r))
                new_update.insert(min_index, update[u])
    return new_update

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
        # middle.append(int(lst[len(lst)//2]))
        pass
    else:
        middle.append([int(x) for x in order_update(lst)][len(lst)//2] )


print(sum(middle))

#So for part two, you need to correclty order the values?