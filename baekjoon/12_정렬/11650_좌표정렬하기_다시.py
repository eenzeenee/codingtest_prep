# 좌표 정렬하기

#%%
N = int(input())
answer = list()

for _ in range(N):
    answer.append(list(map(int, input().split())))

answer = sorted(answer)

for x, y in answer:
    print(x, end = ' ')
    print(y)
# %%
