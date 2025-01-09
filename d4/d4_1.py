# Solution for Day 4 - Part 1
import csv
from tqdm import tqdm
def check_forward(board, i,j):
    if j + len(word) > width: return False
    if "".join(board[i][j:j+len(word)]) == word: return True 
    return False

def check_backward(board, i,j):
    if (j+1) - len(word) < 0: return False
    if "".join(board[i][j-len(word)+1:j+1])[::-1] == word: return True 
    return False

def transpose_board(board):
    return [[board[i][j] for i in range(len(board))] 
            for j in range(len(board[0]))]

def check_upward(board, i,j):
    new_board = transpose_board(board)
    return check_forward(new_board,i,j)
    
def check_downward(board, i,j):
    new_board = transpose_board(board)
    return check_backward(new_board,i,j)
    
def check_diagonal_down_right(board, i,j):
    if i + len(word) > height or j + len(word) > width: return False
    for h in range(len(word)):
        if board[i+h][j+h] != word[h]: return False
    return True

def check_diagonal_down_left(board, i,j):
    if i + len(word) > height or (j+1) - len(word) < 0: return False
    for h in range(len(word)):
        if board[i+h][j-h] != word[h]: return False
    return True

def check_diagonal_up_right(board, i,j):
    if (i+1) - len(word) < 0 or j + len(word) > width: return False
    for h in range(len(word)):
        if board[i-h][j+h] != word[h]: return False
    return True

def check_diagonal_up_left(board, i,j):
    if (i+1) - len(word) < 0 or (j+1) - len(word) < 0: return False
    for h in range(len(word)):
        if board[i-h][j-h] != word[h]: return False
    return True


board = []
height = 0
width = 0
word = "XMAS"

with open("input.txt") as file: 
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        width = len(row[0])
        board.append(list(row[0]))

height = len(board)
width = len(board[0])

amts = 0

for i in tqdm(range(height), desc="outer"):
    for j in range(width):
        amts += check_forward(board,i,j)
        amts += check_backward(board,i,j)
        amts += check_upward(board,i,j)
        amts += check_downward(board,i,j)
        amts += check_diagonal_down_right(board,i,j)
        amts += check_diagonal_down_left(board,i,j)
        amts += check_diagonal_up_right(board,i,j)
        amts += check_diagonal_up_left(board,i,j)
print(amts)
