import csv


l = [] 
r = []

with open("input.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        l.append(row[0])
        r.append(row[3])

l.sort()
r.sort()

sum = 0

for i in range(len(l)):
    sum += abs(int(r[i]) - int(l[i]))

print(sum)