# Solution for Day 2 - Part 1
import csv


def check_report(report):
    increasing = report[0] < report[1]
    if report[0] == report[1]: return False

    for i in range(1,len(report)):
        diff = abs(report[i-1] - report[i])
        if diff > 3 or diff < 1: return False 
        if increasing: 
            if report[i-1] > report[i]: return False 
        else: 
            if report[i-1] < report[i]: return False 

    return True

num_safe = 0

with open("input.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        safe = check_report([int(i) for i in row])
        if not safe:
            for i in range(len(row)):
                row_temp = row.copy()
                del row_temp[i]
                if check_report([int(i) for i in row_temp]):
                    num_safe += 1
                    break
        else: num_safe += 1

print(num_safe)

