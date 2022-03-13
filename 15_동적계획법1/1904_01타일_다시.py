# 01 타일 다시

#%%
N = int(input())
l = [0] * 1000001

l[1] = 1
l[2] = 2

for i in range(3, N+1):
    l[i] = l[i-1] + l[i-2]

print(l[N])
# %%
