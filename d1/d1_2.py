import csv


l = [] 
r = {}

with open("input.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        l.append(row[0])
        if row[3] not in r:
            r[row[3]] = 1
        else:
            r[row[3]] += 1

l.sort()


sum = 0

for i in range(len(l)):
    sum += 0 if l[i] not in r else int(l[i]) * r[l[i]]

print(sum)