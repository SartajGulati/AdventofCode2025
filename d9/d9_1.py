import csv

with open("input.txt") as file:
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        print(row)
