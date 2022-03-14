# RGB 거리

#%%
N = int(input())
log = []

for i in range(N):
    log.append(list(map(int, input().split())))

for i in range(1, len(log)):
    log[i][0] = min(log[i-1][1], log[i-1][2]) + log[i][0]
    log[i][1] = min(log[i-1][0], log[i-1][2]) + log[i][1]
    log[i][2] = min(log[i-1][0], log[i-1][1]) + log[i][2]

print(min(log[-1][0], log[-1][1], log[-1][2]))
# %%
