# 2580 스도쿠

#%%
import sys
board = []
zero_idx = []
for i in range(9):
    tmp = list(map(int, input().split()))
    # tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    if 0 in tmp:
        zero_idx.append([i, tmp.index(0)])

    board.append(tmp)

# %%
board
# %%
zero_idx

#%%

def check_row(x, num):

def check_col(x, num):

def check_square(x, num):
