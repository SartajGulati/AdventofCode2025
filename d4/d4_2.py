# Solution for Day 4 - Part 2
# Solution for Day 4 - Part 1
import csv
from tqdm import tqdm


def check_diagonals(board,i,j):
    left = {} 
    right = {}
    truth = {'M':1,"A":1,"S":1}
    dirs = [-1,0,1]
    for d in dirs:
        left[board[i+d][j+d]] = 1
        right[board[i-d][j+d]] = 1
    return (left == right and left == truth)


board = []
height = 0
width = 0

with open("input.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        board.append(list(row[0]))

height = len(board)
width = len(board[0])
amts = 0
for i in tqdm(range(1,height-1)):
    for j in range(1,width-1):
        if(board[i][j] == 'A'): amts += check_diagonals(board,i,j)
        
print(amts)
