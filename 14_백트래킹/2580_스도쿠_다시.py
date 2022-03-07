# 2580 스도쿠

#%%
import sys
board = [list(map(int, sys.stdin.readline())) for _ in range(9)]
# board = [list(map(int, input().split())) for _ in range(9)]
zero_idx = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def check(x, y):
    numbers = [i+1 for i in range(9)]
    for i in range(9):
        if board[x][i] in numbers:
            numbers.remove(board[x][i])
        if board[i][y] in numbers:
            numbers.remove(board[i][y])
    x = x//3
    y = y//3
    for i in range(x*3, (x+1)*3):
        for j in range(y*3, (y+1)*3):
            if board[i][j] in numbers:
                numbers.remove(board[i][j])
    return numbers

def sdoku(idx):
    if idx == len(zero_idx):
        print(*board)
        sys.exit(0)
    
    x = board[idx][0]
    y = board[idx][1]

    sdoku_nums = check(x, y)

    for num in sdoku_nums:
        board[x][y] = num
        sdoku(idx + 1)
        board[x][y] = 0

sdoku(0)