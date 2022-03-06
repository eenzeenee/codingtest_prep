# 2580 스도쿠

#%%
import sys
board = []
zero_idx = []
for i in range(9):
    # tmp = list(map(int, input().split()))
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    board.append(tmp)

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero_idx.append((i,j))

def check_row(x, num):
    for i in range(9):
        if num == board[x][i]:
            return False
    return True

def check_col(y, num):
    for i in range(9):
        if num == board[i][y]:
            return False
    return True

def check_row_col(x, y, num):
    for i in range(9):
        if num == board[x][i] or num == board[i][y]:
            return False
    return True

def check_square(x, y, num):
    tmp_x = (x//3)*3
    tmp_y = (y//3)*3
    for i in range(3):
        for j in range(3):
            if num == board[tmp_x+i][tmp_y+j]:
                return False
    return True

def check_row_col(x, y, num):
    for i in range(9):
        if num == board[x][i] or num == board[i][y]:
            return False
    return True

def check(x, y, num):
    tmp_x = (x//3)*3
    tmp_y = (y//3)*3
    for i in range(9):
        if num == board[x][i] or num == board[i][y]:
            return False
        if i <= 2:
            for j in range(3):
                if num == board[tmp_x+i][tmp_y+j]:
                    return False
    return True

def sdoku(idx):
    if idx == len(zero_idx):
        for i in range(9):
            print(*board[i])        # * -> unpacking list
        return

    for i in range(1, 10):
        x = zero_idx[idx][0]    # 채워야 하는 위치의 행
        y = zero_idx[idx][1]    # 채워야 하는 위치의 열
        if check(x, y, i):
            board[x][y] = i
            sdoku(idx+1)
            board[x][y] = 0

sdoku(0)

#### 시간 초과 
#### -> 해결 위해 row, col 확인 함수 합침 (check_row_col) -> 여전히 시간초과
#### -> 해결 위해 row, col, square 확인 함수 합침 (check) -> 여전히 시간초과

    
# %%
import sys
board = [list(map(int, input().split())) for _ in range(9)]
# board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
zero_idx = [(i,j) for i in range(9) for j in range(9) if board[i][j] == 0]

def check(x, y):
    numbers = [i for i in range(1, 10)]
    
    for i in range(9):
        if board[x][i] in numbers:
            numbers.remove(board[x][i])
        if board[i][y] in numbers:
            numbers.remove(board[i][y])

    nx = x//3
    ny = y//3
    for i in range(nx * 3, (nx+1) * 3):
        for j in range(ny * 3, (ny+1) * 3):
            if board[i][j] in numbers:
                numbers.remove(board[i][j])
    return numbers

def sdoku(idx):
    if idx == len(zero_idx):
        for line in board:
            print(' '.join(map(str, line)))
        sys.exit(0)         ## 답 하나 제출하고 멈추도록!
    
    x, y = zero_idx[idx]

    sdoku_nums = check(x, y)

    for num in sdoku_nums:
        board[x][y] = num
        sdoku(idx+1)
        board[x][y] = 0

sdoku(0)

#### 시간 초과 
#### PyPy3로 제출 시 30%에서 계속 오류 -> 여러 개의 정답 출력하는 경우 발생
#### 해결 위해 end_func 변수 추가하여 한번 출력하면 함수 멈추도록
####    end_func 변수 넣을 때 재귀함수 주의 -> 얘도 여전히 오답
#### 해결 위해 return 대신 sys.exit(0) 사용하여 한번 정답 출력하면 시스템 멈추도록 강제
# %%
