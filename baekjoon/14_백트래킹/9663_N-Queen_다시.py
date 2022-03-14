# N-Queen

#%%
# import sys
# N = int(sys.stdin.readline())
N = int(input())
rows = [0] * N
visited = [False] * N
answer = 0

def cannot_attack(x):
    for i in range(x):
        if abs(rows[x] - rows[i]) == abs(x-i):
            return False        # 공격 가능
    return True                 # 공격 불가    

def Queen(x):
    global answer
    if x == N:
        answer += 1
        return
    for i in range(N):
        if visited[i]:
            continue
        rows[x] = i
        if cannot_attack(x):
            visited[i] = True
            Queen(x+1)
            visited[i] = False


Queen(0)
print(answer)
# %%
