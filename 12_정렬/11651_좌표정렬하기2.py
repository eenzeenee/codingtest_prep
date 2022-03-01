# 좌표 정렬하기 2

#%%
N = int(input())
answer = []
for _ in range(N):
    [x, y] = list(map(int, input().split()))
    answer.append([y, x])

answer = sorted(answer)

for y, x in answer:
    print(x, end = ' ')
    print(y)
# %%
