# 체스판 다시 칠하기

#%%

N, M = map(int, input().split())

board = []
for _ in range(N):
    line = list(input())
    board.append(line)

count = []
for a in range(N-7):        # 행 시작점
    for b in range(M-7):    # 열 시작점
        w_index = 0         # w로 시작하는 경우 변경해야 하는 자리 수
        b_index = 0         # b로 시작하는 경우 변경해야 하는 자리 수
        # 시작 문자가 w이면 행 + 열 이 짝수인 경우 모두 w이어야 함
        # 시작 문자가 b이면 행 + 열 이 짝수인 경우 모두 b이어야 함
        
        for i in range(a, a+8):     # 체스판 행
            for j in range(b, b+8): # 체스판 열
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W': 
                        w_index += 1
                    if board[i][j] != 'B':
                        b_index += 1
                else:
                    if board[i][j] != 'B':
                        w_index += 1
                    if board[i][j] != 'W':
                        b_index += 1
        count.append(min(w_index, b_index))

print(min(count))

# %%
